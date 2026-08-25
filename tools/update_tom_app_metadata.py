#!/usr/bin/env python3
"""Build TOM's shared Quest app metadata index without copying Lightning Launcher/MetaMetadata code.

The collector deliberately combines independent sources:
  * current Meta Store sections for discovery;
  * SideQuest for preferred third-party package/ID discovery and fallback artwork;
  * OculusDB for lower-priority historical/delisted package <-> Meta app-ID gap filling;
  * Meta GraphQL / public experience pages for official names/artwork when a Meta ID is known;
  * the prior TOM index, which is never discarded merely because an app disappears today.

The Android app does not need this job to function. It can resolve targeted installed apps itself.
This job exists so many TOM users can share discovery work and so endpoint/doc-ID fixes can be
published centrally through metadata/resolver-config.json without shipping a new APK.
"""
from __future__ import annotations

import concurrent.futures
import datetime as dt
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
META_DIR = ROOT / "metadata"
APPS_DIR = META_DIR / "apps"
CONFIG_PATH = META_DIR / "resolver-config.json"
INDEX_PATH = META_DIR / "tom-app-index.json"
DIAGNOSTICS_PATH = META_DIR / "collector-diagnostics.json"
USER_AGENT = "TheOcularMigraineNative-metadata-collector/1"
MAX_WORKERS = 8
SIDEQUEST_ORIGIN = "https://sidequestvr.com"


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _response_content_type(headers) -> str | None:
    if headers is None:
        return None
    try:
        return headers.get_content_type()
    except AttributeError:
        raw = headers.get("Content-Type") if hasattr(headers, "get") else None
        return clean(raw.split(";", 1)[0]) if isinstance(raw, str) else None


def _body_preview(raw: bytes, limit: int = 240) -> str:
    text = raw[:limit].decode("utf-8", errors="replace")
    return " ".join(text.split())


def request_response(
    url: str,
    *,
    data: bytes | None = None,
    headers: dict[str, str] | None = None,
    timeout: int = 20,
) -> tuple[bytes, int, str | None]:
    merged = {"User-Agent": USER_AGENT, "Accept": "application/json,text/html;q=0.8,*/*;q=0.5"}
    if headers:
        merged.update(headers)
    req = urllib.request.Request(url, data=data, headers=merged, method="POST" if data is not None else "GET")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read()
            status = int(getattr(resp, "status", 200) or 200)
            return raw, status, _response_content_type(resp.headers)
    except urllib.error.HTTPError as exc:
        raw = exc.read(512)
        content_type = _response_content_type(exc.headers)
        preview = _body_preview(raw)
        raise RuntimeError(
            f"HTTP {exc.code} {exc.reason}; content-type={content_type or 'unknown'}; body={preview!r}"
        ) from exc


def request(url: str, *, data: bytes | None = None, headers: dict[str, str] | None = None, timeout: int = 20) -> bytes:
    raw, _, _ = request_response(url, data=data, headers=headers, timeout=timeout)
    return raw


def get_json(url: str, *, headers: dict[str, str] | None = None, provider: str = "JSON endpoint") -> object:
    raw, status, content_type = request_response(url, headers=headers)
    text = raw.decode("utf-8", errors="replace")
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            f"{provider} returned non-JSON response; status={status}; "
            f"content-type={content_type or 'unknown'}; body={_body_preview(raw)!r}"
        ) from exc


def post_form_json(url: str, fields: dict[str, object], headers: dict[str, str] | None = None) -> dict:
    encoded = urllib.parse.urlencode({k: v if isinstance(v, str) else json.dumps(v, separators=(",", ":")) for k, v in fields.items()}).encode()
    raw = request(url, data=encoded, headers={"Content-Type": "application/x-www-form-urlencoded", **(headers or {})})
    text = raw.decode("utf-8", errors="replace")
    # Meta's web GraphQL endpoint may append streaming chunks; first complete JSON object is enough.
    if "}\r\n" in text:
        text = text.split("}\r\n", 1)[0] + "}"
    return json.loads(text)


def post_json(url: str, payload: dict) -> dict:
    raw = request(url, data=json.dumps(payload, separators=(",", ":")).encode(), headers={"Content-Type": "application/json"})
    return json.loads(raw.decode("utf-8"))


def load_json(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def clean(value):
    return value.strip() if isinstance(value, str) and value.strip() else None


def first_https(*values):
    for value in values:
        value = clean(value)
        if value and value.lower().startswith("https://"):
            return value
    return None


def merge_record(dst: dict, src: dict, source: str, seen: str):
    existing_hints = set(dst.get("sourceHints") or [])
    has_official_history = bool(existing_hints & {"meta", "meta-public"})
    hints = set(existing_hints)
    hints.add(source)
    dst["sourceHints"] = sorted(hints)
    dst["lastSeen"] = seen
    official = source in {"meta", "meta-public"}
    sidequest_preferred = source == "sidequest" and not has_official_history
    for key in ("name", "metaAppId", "landscape", "icon", "hero"):
        value = clean(src.get(key))
        if not value:
            continue
        if key in {"landscape", "icon", "hero"} and not value.lower().startswith("https://"):
            continue
        # Meta is authoritative. Among third-party discovery sources SideQuest is preferred over
        # OculusDB; OculusDB is historical gap-fill only. This also upgrades old collector records
        # that previously learned a field from OculusDB when SideQuest now has a usable value.
        if official or sidequest_preferred or not clean(dst.get(key)):
            dst[key] = value


def fetch_oculusdb(cfg: dict, records: dict, seen: str) -> int:
    print("Fetching OculusDB…")
    data = get_json(cfg["oculusDbUrl"], provider="OculusDB")
    if not isinstance(data, list):
        raise RuntimeError("OculusDB allapps response was not a list")
    for item in data:
        if not isinstance(item, dict):
            continue
        package = clean(item.get("packageName"))
        if not package or "rift" in package.lower():
            continue
        rec = records.setdefault(package, {})
        merge_record(rec, {"name": item.get("appName"), "metaAppId": str(item.get("id") or "")}, "oculusdb", seen)
    print(f"OculusDB contributed {len(data)} records")
    return len(data)


def fetch_sidequest(cfg: dict, records: dict, seen: str) -> tuple[set[str], dict]:
    print("Fetching SideQuest…")
    page = 0
    meta_ids: set[str] = set()
    total = 0
    while True:
        params = urllib.parse.urlencode({
            "search": "", "page": page, "order": "created", "direction": "desc",
            "app_categories_id": 1, "limit": 100, "device_filter": "all",
            "license_filter": "all", "download_filter": "all",
        })
        root = get_json(
            cfg["sideQuestUrl"] + "?" + params,
            headers={"Origin": SIDEQUEST_ORIGIN, "Accept": "application/json"},
            provider=f"SideQuest page {page}",
        )
        items = root.get("data") if isinstance(root, dict) else None
        if not items:
            break
        for item in items:
            if not isinstance(item, dict):
                continue
            package = clean(item.get("packagename"))
            if not package:
                continue
            labrador = clean(item.get("labrador_url")) or ""
            match = re.search(r"/(?:quest/)?(\d{8,})(?:/|$)", labrador)
            meta_id = match.group(1) if match else None
            if meta_id:
                meta_ids.add(meta_id)
            rec = records.setdefault(package, {})
            merge_record(rec, {
                "name": item.get("name"),
                "metaAppId": meta_id,
                "landscape": item.get("image_url"),
                "hero": item.get("app_banner"),
            }, "sidequest", seen)
            total += 1
        page += 1
        if page > 250:
            raise RuntimeError("SideQuest pagination safety limit reached")
    if total == 0:
        raise RuntimeError("SideQuest returned zero app records")
    print(f"SideQuest contributed {total} records across {page} pages ({len(meta_ids)} Meta IDs)")
    return meta_ids, {"status": "ok", "records": total, "pages": page, "metaIds": len(meta_ids)}


def fetch_meta_section_ids(cfg: dict) -> set[str]:
    print("Fetching current Meta Store sections…")
    found: set[str] = set()
    endpoint = cfg["metaGraphqlEndpoint"]
    doc_id = cfg["metaStoreSectionDocId"]
    lsd = cfg["metaStoreLsd"]
    for section in cfg.get("metaStoreSectionIds", []):
        cursor = "0"
        pages = 0
        while True:
            variables = {
                "ageRatingFilter": [], "controllerFilter": [], "cursor": cursor, "first": 100,
                "interactionModeFilter": [], "languageFilter": [], "playerModeFilter": [],
                "priceRangeFilter": [], "ratingAboveFilter": 0, "saleTypeFilter": [],
                "sortOrder": "release_date", "topicIdFilter": [], "id": section,
                "__relay_internal__pv__MDCAppStoreShowRatingCountrelayprovider": False,
            }
            root = post_form_json(endpoint, {"lsd": lsd, "variables": variables, "doc_id": doc_id}, {"X-FB-LSD": lsd})
            all_items = (((root.get("data") or {}).get("node") or {}).get("all_items") or {})
            edges = all_items.get("edges") or []
            for edge in edges:
                app_id = clean(((edge or {}).get("node") or {}).get("id"))
                if app_id:
                    found.add(app_id)
            page_info = all_items.get("page_info") or {}
            if not page_info.get("has_next_page"):
                break
            cursor = str(page_info.get("end_cursor") or "")
            pages += 1
            if not cursor or pages > 20:
                break
    print(f"Meta Store sections exposed {len(found)} unique IDs")
    return found


def resolve_package_from_meta_id(cfg: dict, app_id: str) -> str | None:
    details = post_form_json(cfg["oculusGraphqlEndpoint"], {
        "doc_id": cfg["appDetailsDocId"],
        "access_token": cfg["appDetailsAccessToken"],
        "variables": {"applicationID": app_id},
    })
    node = (details.get("data") or {}).get("node") or {}
    channels = ((node.get("release_channels") or {}).get("nodes") or [])
    binary = (channels[0].get("latest_supported_binary") if channels else None) or {}
    version_code = binary.get("version_code")
    if not version_code:
        return None
    query = """query ($params: AppBinaryInfoArgs!) { app_binary_info(args: $params) { info { binary { ... on AndroidBinary { package_name version_code } } } } }"""
    payload = {
        "doc": query,
        "variables": json.dumps({"params": {"app_params": [{"app_id": app_id, "version_code": version_code}]}}),
        "access_token": cfg["appBinaryAccessToken"],
    }
    result = post_json(cfg["oculusGraphqlEndpoint"], payload)
    info = (((result.get("data") or {}).get("app_binary_info") or {}).get("info") or [])
    if not info:
        return None
    return clean(((info[0] or {}).get("binary") or {}).get("package_name"))


def fetch_meta_details(cfg: dict, app_id: str) -> dict:
    root = post_form_json(cfg["oculusGraphqlEndpoint"], {
        "doc_id": cfg["storeDetailsDocId"],
        "access_token": cfg["storeAccessToken"],
        "variables": {"applicationID": app_id},
    })
    node = (root.get("data") or {}).get("node") or {}
    if not node:
        raise RuntimeError("empty Meta node")
    result = {"name": clean(node.get("display_name")), "metaAppId": app_id}
    mapping = {
        "APP_IMG_COVER_LANDSCAPE": "landscape",
        "APP_IMG_ICON": "icon",
        "APP_IMG_HERO": "hero",
    }
    revisions = []
    for revision_key in ("lastRevision", "firstRevision"):
        revisions.extend(((node.get(revision_key) or {}).get("nodes") or []))
    for revision in revisions:
        translations = (((revision.get("pdp_metadata") or {}).get("translations") or {}).get("nodes") or [])
        for translation in translations:
            if translation.get("locale") != "en_US":
                continue
            result["name"] = clean(translation.get("display_name")) or result.get("name")
            images = (((translation.get("images") or {}).get("nodes") or []))
            for image in images:
                key = mapping.get(image.get("image_type"))
                uri = first_https(image.get("uri"))
                if key and uri:
                    result[key] = uri
    return result


def fetch_public_experience(cfg: dict, app_id: str) -> dict:
    url = cfg["experienceUrlTemplate"].replace("{id}", app_id)
    text = request(url, headers={"Accept": "text/html"}).decode("utf-8", errors="replace")
    match = re.search(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', text, re.I | re.S)
    if not match:
        return {}
    payload = json.loads(html.unescape(match.group(1)))
    image = payload.get("image")
    if isinstance(image, list):
        image = next((x for x in image if isinstance(x, str) and x.startswith("https://")), None)
    elif isinstance(image, dict):
        image = image.get("url")
    return {"name": payload.get("name"), "landscape": first_https(image), "metaAppId": app_id}


def enrich_meta(cfg: dict, records: dict, meta_ids: set[str], seen: str) -> dict:
    id_to_package = {clean(v.get("metaAppId")): k for k, v in records.items() if clean(v.get("metaAppId"))}
    known_before = len(id_to_package)
    unresolved = sorted(app_id for app_id in meta_ids if app_id not in id_to_package)
    print(f"Resolving {len(unresolved)} Meta IDs that lack a known package mapping…")
    no_package_ids: list[str] = []
    mapping_errors: list[dict[str, str]] = []

    def map_one(app_id):
        try:
            return app_id, resolve_package_from_meta_id(cfg, app_id), None
        except Exception as exc:
            return app_id, None, str(exc)

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        for app_id, package, error in pool.map(map_one, unresolved):
            if package:
                id_to_package[app_id] = package
                merge_record(records.setdefault(package, {}), {"metaAppId": app_id}, "meta", seen)
            elif error:
                print(f"WARN package mapping failed for {app_id}: {error}", file=sys.stderr)
                mapping_errors.append({"appId": app_id, "error": error})
            else:
                no_package_ids.append(app_id)

    if no_package_ids:
        print(
            f"WARN Meta package mapping returned no package for {len(no_package_ids)} IDs; "
            f"see metadata/{DIAGNOSTICS_PATH.name}",
            file=sys.stderr,
        )
    if mapping_errors:
        print(
            f"WARN Meta package mapping raised errors for {len(mapping_errors)} IDs; "
            f"see metadata/{DIAGNOSTICS_PATH.name}",
            file=sys.stderr,
        )

    targets = [(app_id, package) for app_id, package in id_to_package.items() if package]
    print(f"Fetching official Meta details for {len(targets)} mapped apps…")

    def details_one(pair):
        app_id, package = pair
        try:
            return package, fetch_meta_details(cfg, app_id), "meta"
        except Exception:
            try:
                return package, fetch_public_experience(cfg, app_id), "meta-public"
            except Exception as exc:
                print(f"WARN Meta details failed for {package}/{app_id}: {exc}", file=sys.stderr)
                return package, {}, "meta"

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        for package, details, source in pool.map(details_one, targets):
            if details:
                merge_record(records.setdefault(package, {}), details, source, seen)

    return {
        "candidateMetaIds": len(meta_ids),
        "knownPackageMappingsBeforeRun": known_before,
        "packageMappingAttempts": len(unresolved),
        "packageMappingNoResultIds": no_package_ids,
        "packageMappingErrors": mapping_errors,
        "mappedAppsEnriched": len(targets),
    }


def write_diagnostics(diagnostics: dict):
    DIAGNOSTICS_PATH.write_text(
        json.dumps(diagnostics, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote collector diagnostics to metadata/{DIAGNOSTICS_PATH.name}")


def write_outputs(records: dict, seen: str) -> int:
    APPS_DIR.mkdir(parents=True, exist_ok=True)
    index_apps = {}
    valid_packages = re.compile(r"^[A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)+$")
    for package in sorted(records):
        if not valid_packages.match(package):
            continue
        record = records[package]
        index_record = {
            k: record[k]
            for k in ("name", "metaAppId", "landscape", "icon", "hero", "sourceHints", "firstSeen", "lastSeen")
            if record.get(k) is not None
        }
        index_record.setdefault("firstSeen", record.get("lastSeen") or seen)
        index_apps[package] = index_record

        # Runtime package files intentionally omit firstSeen/lastSeen so a daily collector run does
        # not rewrite thousands of files just because the observation timestamp advanced.
        runtime_record = {
            k: index_record[k]
            for k in ("name", "metaAppId", "landscape", "icon", "hero", "sourceHints")
            if index_record.get(k) is not None
        }
        (APPS_DIR / f"{package}.json").write_text(
            json.dumps(
                {"schema": 1, "packageName": package, **runtime_record},
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            ) + "\n",
            encoding="utf-8",
        )
    INDEX_PATH.write_text(json.dumps({"schema": 1, "generatedAt": seen, "apps": index_apps}, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
    print(f"Wrote {len(index_apps)} TOM metadata records")
    return len(index_apps)


def main():
    cfg = load_json(CONFIG_PATH, {})
    if cfg.get("schema") != 1:
        raise SystemExit("metadata/resolver-config.json schema must be 1")
    prior = load_json(INDEX_PATH, {"apps": {}})
    records = {k: dict(v) for k, v in (prior.get("apps") or {}).items() if isinstance(v, dict)}
    seen = now_iso()
    for record in records.values():
        record.setdefault("firstSeen", record.get("lastSeen") or seen)

    diagnostics = {
        "schema": 1,
        "generatedAt": seen,
        "sources": {},
        "metaDiscovery": {},
    }

    # SideQuest is the preferred third-party discovery/artwork source. OculusDB remains useful for
    # historical/delisted package <-> Meta-ID gaps, but it is intentionally lower priority.
    try:
        sidequest_ids, sidequest_status = fetch_sidequest(cfg, records, seen)
        diagnostics["sources"]["sideQuest"] = sidequest_status
    except Exception as exc:
        print(f"WARN SideQuest discovery failed: {exc}", file=sys.stderr)
        sidequest_ids = set()
        diagnostics["sources"]["sideQuest"] = {"status": "failed", "error": str(exc)}

    try:
        oculusdb_count = fetch_oculusdb(cfg, records, seen)
        diagnostics["sources"]["oculusDb"] = {"status": "ok", "records": oculusdb_count}
    except Exception as exc:
        print(f"WARN OculusDB discovery failed: {exc}", file=sys.stderr)
        diagnostics["sources"]["oculusDb"] = {"status": "failed", "error": str(exc)}

    try:
        store_ids = fetch_meta_section_ids(cfg)
        diagnostics["sources"]["metaStore"] = {"status": "ok", "metaIds": len(store_ids)}
    except Exception as exc:
        print(f"WARN current Meta Store enumeration failed: {exc}", file=sys.stderr)
        store_ids = set()
        diagnostics["sources"]["metaStore"] = {"status": "failed", "error": str(exc)}
    historical_ids = {clean(v.get("metaAppId")) for v in records.values() if clean(v.get("metaAppId"))}
    candidate_ids = set(x for x in historical_ids | sidequest_ids | store_ids if x)
    diagnostics["metaDiscovery"] = {
        "sideQuestMetaIds": sorted(sidequest_ids),
        "metaStoreIds": sorted(store_ids),
        "historicalMetaIdCount": len(historical_ids),
        "candidateMetaIdCount": len(candidate_ids),
    }
    diagnostics["metaEnrichment"] = enrich_meta(cfg, records, candidate_ids, seen)
    diagnostics["outputRecords"] = write_outputs(records, seen)
    write_diagnostics(diagnostics)


if __name__ == "__main__":
    main()
