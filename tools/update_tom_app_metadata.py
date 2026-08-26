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
METAMETADATA_KNOWN_APPS_URL = "https://raw.githubusercontent.com/threethan/MetaMetadata/main/data/known_oculus_apps.json"
META_STORE_PAGE_RETRIES = 3
META_STORE_RETRY_BASE_SECONDS = 1.0
SIDEQUEST_PLACEHOLDER_PACKAGE_RE = re.compile(r"^com\.autogen\.\d+$", re.I)


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


def post_json(url: str, payload: dict, headers: dict[str, str] | None = None) -> dict:
    raw = request(
        url,
        data=json.dumps(payload, separators=(",", ":")).encode(),
        headers={"Content-Type": "application/json", **(headers or {})},
    )
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


def is_sidequest_placeholder_package(package: str | None) -> bool:
    return bool(package and SIDEQUEST_PLACEHOLDER_PACKAGE_RE.fullmatch(package))


def prune_sidequest_placeholder_records(records: dict) -> list[dict[str, str | None]]:
    removed: list[dict[str, str | None]] = []
    for package in list(records):
        if not is_sidequest_placeholder_package(package):
            continue
        record = records.pop(package)
        removed.append({
            "package": package,
            "appId": clean(record.get("metaAppId")),
        })
    return removed


def note_package_mapping(record: dict, source: str):
    hints = set(record.get("packageSourceHints") or [])
    hints.add(source)
    record["packageSourceHints"] = sorted(hints)


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


def fetch_oculusdb(cfg: dict, records: dict, seen: str) -> tuple[int, dict[str, set[str]]]:
    print("Fetching OculusDB…")
    data = get_json(cfg["oculusDbUrl"], provider="OculusDB")
    if not isinstance(data, list):
        raise RuntimeError("OculusDB allapps response was not a list")
    package_map: dict[str, set[str]] = {}
    for item in data:
        if not isinstance(item, dict):
            continue
        package = clean(item.get("packageName"))
        if not package or "rift" in package.lower():
            continue
        app_id = clean(str(item.get("id") or ""))
        rec = records.setdefault(package, {})
        merge_record(rec, {"name": item.get("appName"), "metaAppId": app_id}, "oculusdb", seen)
        if app_id:
            note_package_mapping(rec, "oculusdb")
            package_map.setdefault(app_id, set()).add(package)
    print(f"OculusDB contributed {len(data)} records")
    return len(data), package_map

def fetch_sidequest(
    cfg: dict,
    records: dict,
    seen: str,
) -> tuple[set[str], dict[str, set[str]], dict[str, set[str]], dict]:
    print("Fetching SideQuest…")
    page = 0
    meta_ids: set[str] = set()
    package_map: dict[str, set[str]] = {}
    placeholder_map: dict[str, set[str]] = {}
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

            # SideQuest uses com.autogen.<number> as a Store-listing placeholder for some
            # Meta-hosted apps. It is not an Android package name and must never become a
            # runtime apps/<package>.json key. Keep the Meta ID as discovery input so TOM can
            # resolve the real package through Meta's binary metadata instead.
            if is_sidequest_placeholder_package(package) and meta_id:
                placeholder_map.setdefault(meta_id, set()).add(package)
                total += 1
                continue

            if meta_id:
                package_map.setdefault(meta_id, set()).add(package)
            rec = records.setdefault(package, {})
            merge_record(rec, {
                "name": item.get("name"),
                "metaAppId": meta_id,
                "landscape": item.get("image_url"),
                "hero": item.get("app_banner"),
            }, "sidequest", seen)
            if meta_id:
                note_package_mapping(rec, "sidequest")
            total += 1
        page += 1
        if page > 250:
            raise RuntimeError("SideQuest pagination safety limit reached")
    if total == 0:
        raise RuntimeError("SideQuest returned zero app records")
    placeholder_count = sum(len(packages) for packages in placeholder_map.values())
    print(
        f"SideQuest contributed {total} records across {page} pages ({len(meta_ids)} Meta IDs; "
        f"{placeholder_count} com.autogen placeholders treated as Meta-ID-only discovery)"
    )
    return meta_ids, package_map, placeholder_map, {
        "status": "ok",
        "records": total,
        "pages": page,
        "metaIds": len(meta_ids),
        "placeholderPackages": placeholder_count,
        "placeholderMetaIds": len(placeholder_map),
    }

def fetch_metametadata_package_map() -> tuple[dict[str, set[str]], dict]:
    """Fetch MetaMetadata's generated Meta-ID -> Android-package map as a fallback only.

    TOM does not copy or execute MetaMetadata/Lightning Launcher code here. This consumes the
    project's public generated known-app list, just as TOM already consumes its public per-package
    metadata in the separate MetaMetadata provider. Package provenance remains collector-only.
    """
    print("Fetching MetaMetadata known package map…")
    data = get_json(METAMETADATA_KNOWN_APPS_URL, provider="MetaMetadata known app map")
    if not isinstance(data, list):
        raise RuntimeError("MetaMetadata known app map was not a list")

    valid_package = re.compile(r"^[A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)+$")
    package_map: dict[str, set[str]] = {}
    invalid = 0
    placeholder = 0
    for item in data:
        if not isinstance(item, dict):
            invalid += 1
            continue
        app_id = clean(str(item.get("id") or ""))
        package = clean(item.get("packageName"))
        if not app_id or not package or not valid_package.fullmatch(package):
            invalid += 1
            continue
        if is_sidequest_placeholder_package(package):
            placeholder += 1
            continue
        package_map.setdefault(app_id, set()).add(package)

    package_count = sum(len(packages) for packages in package_map.values())
    print(
        f"MetaMetadata package map contributed {package_count} package mappings across "
        f"{len(package_map)} Meta IDs"
    )
    return package_map, {
        "status": "ok",
        "records": len(data),
        "metaIds": len(package_map),
        "packageMappings": package_count,
        "invalidRecords": invalid,
        "placeholderPackagesSkipped": placeholder,
        "url": METAMETADATA_KNOWN_APPS_URL,
    }


def fetch_meta_section_ids(cfg: dict) -> tuple[set[str], dict]:
    print("Fetching current Meta Store sections…")
    found: set[str] = set()
    endpoint = cfg["metaGraphqlEndpoint"]
    doc_id = cfg["metaStoreSectionDocId"]
    lsd = cfg["metaStoreLsd"]
    sections = list(cfg.get("metaStoreSectionIds", []))
    failures: list[dict[str, object]] = []
    completed_sections = 0

    for section in sections:
        cursor = "0"
        page_index = 0
        section_complete = False
        while True:
            variables = {
                "ageRatingFilter": [], "controllerFilter": [], "cursor": cursor, "first": 100,
                "interactionModeFilter": [], "languageFilter": [], "playerModeFilter": [],
                "priceRangeFilter": [], "ratingAboveFilter": 0, "saleTypeFilter": [],
                "sortOrder": "release_date", "topicIdFilter": [], "id": section,
                "__relay_internal__pv__MDCAppStoreShowRatingCountrelayprovider": False,
            }
            root = None
            last_error = None
            for attempt in range(1, META_STORE_PAGE_RETRIES + 1):
                try:
                    root = post_form_json(
                        endpoint,
                        {"lsd": lsd, "variables": variables, "doc_id": doc_id},
                        {"X-FB-LSD": lsd},
                    )
                    break
                except Exception as exc:
                    last_error = str(exc)
                    if attempt < META_STORE_PAGE_RETRIES:
                        delay = META_STORE_RETRY_BASE_SECONDS * (2 ** (attempt - 1))
                        print(
                            f"WARN Meta Store section={section} page={page_index} attempt={attempt} failed: {exc}; "
                            f"retrying in {delay:.1f}s",
                            file=sys.stderr,
                        )
                        time.sleep(delay)
            if root is None:
                failure = {
                    "sectionId": str(section),
                    "page": page_index,
                    "cursor": cursor,
                    "attempts": META_STORE_PAGE_RETRIES,
                    "error": last_error or "unknown Meta Store page failure",
                }
                failures.append(failure)
                print(
                    f"WARN Meta Store section={section} page={page_index} abandoned after "
                    f"{META_STORE_PAGE_RETRIES} attempts; preserving {len(found)} IDs already discovered",
                    file=sys.stderr,
                )
                break

            all_items = (((root.get("data") or {}).get("node") or {}).get("all_items") or {})
            edges = all_items.get("edges") or []
            for edge in edges:
                app_id = clean(((edge or {}).get("node") or {}).get("id"))
                if app_id:
                    found.add(app_id)
            page_info = all_items.get("page_info") or {}
            if not page_info.get("has_next_page"):
                section_complete = True
                break
            next_cursor = str(page_info.get("end_cursor") or "")
            page_index += 1
            if not next_cursor or page_index > 20:
                failures.append({
                    "sectionId": str(section),
                    "page": page_index,
                    "cursor": next_cursor,
                    "attempts": 0,
                    "error": "invalid cursor or pagination safety limit reached",
                })
                break
            cursor = next_cursor

        if section_complete:
            completed_sections += 1

    if failures:
        status = "partial" if found else "failed"
    else:
        status = "ok"
    summary = {
        "status": status,
        "metaIds": len(found),
        "sectionsConfigured": len(sections),
        "sectionsCompleted": completed_sections,
        "pageFailures": failures,
    }
    print(
        f"Meta Store sections exposed {len(found)} unique IDs "
        f"({completed_sections}/{len(sections)} sections complete, {len(failures)} page failures)"
    )
    return found, summary

def _normalize_version_code(value) -> int | str | None:
    """Preserve Meta binary version codes as JSON numbers whenever they are numeric."""
    if value is None or isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, float) and value.is_integer():
        return int(value)
    text = clean(str(value))
    if not text:
        return None
    if re.fullmatch(r"-?\d+", text):
        try:
            return int(text)
        except ValueError:
            pass
    return text


def _store_binary_version_codes(node: dict) -> list[int | str]:
    values: list[int | str] = []

    def add(value):
        normalized = _normalize_version_code(value)
        if normalized is not None and normalized not in values:
            values.append(normalized)

    # Current Store-details responses expose revision binaries even when the older
    # release_channels query no longer yields a usable latest_supported_binary.
    for revision_key in ("lastRevision", "firstRevision"):
        for revision in ((node.get(revision_key) or {}).get("nodes") or []):
            application = revision.get("application") or {}
            for channel in ((application.get("liveChannel") or {}).get("nodes") or []):
                add((channel.get("latest_supported_binary") or {}).get("version_code"))
            add((revision.get("live_binary") or {}).get("version_code"))
            add((revision.get("binary") or {}).get("version_code"))
    return values


def _legacy_binary_version_codes(cfg: dict, app_id: str) -> list[int | str]:
    details = post_form_json(cfg["oculusGraphqlEndpoint"], {
        "doc_id": cfg["appDetailsDocId"],
        "access_token": cfg["appDetailsAccessToken"],
        "variables": {"applicationID": app_id},
    })
    node = (details.get("data") or {}).get("node") or {}
    values: list[int | str] = []
    for channel in ((node.get("release_channels") or {}).get("nodes") or []):
        value = _normalize_version_code((channel.get("latest_supported_binary") or {}).get("version_code"))
        if value is not None and value not in values:
            values.append(value)
    return values


def _compact_graphql_errors(errors) -> list[dict[str, object]]:
    compact: list[dict[str, object]] = []
    for raw in (errors or [])[:5]:
        if isinstance(raw, dict):
            item: dict[str, object] = {}
            message = clean(raw.get("message"))
            if message:
                item["message"] = message[:500]
            path = raw.get("path")
            if isinstance(path, list):
                item["path"] = path[:16]
            extensions = raw.get("extensions") or {}
            if isinstance(extensions, dict):
                code = extensions.get("code")
                if code is not None:
                    item["code"] = str(code)[:120]
            compact.append(item or {"message": str(raw)[:500]})
        else:
            compact.append({"message": str(raw)[:500]})
    return compact


def _package_from_binary_version(
    cfg: dict,
    app_id: str,
    version_code: int | str,
) -> tuple[str | None, str, list[dict[str, object]]]:
    # Keep the AppBinaryInfo selection shape compatible with the currently working public
    # MetaMetadata collector. This undocumented endpoint has returned server-side execution
    # exceptions for smaller selection sets even though ordinary GraphQL semantics would allow
    # them. TOM independently issues the request; no MetaMetadata/Lightning Launcher code runs.
    query = """
query ($params: AppBinaryInfoArgs!) {
  app_binary_info(args: $params) {
    info {
      binary {
        ... on AndroidBinary {
          id
          package_name
          version_code
          asset_files {
            edges {
              node {
                ... on AssetFile {
                  file_name
                  uri
                  size
                }
              }
            }
          }
        }
      }
    }
  }
}
"""
    payload = {
        "doc": query,
        # Keep numeric version codes numeric. Meta's AppBinaryInfoArgs accepts the native
        # version-code scalar; converting it to a JSON string can produce an HTTP-200 GraphQL
        # error/empty-data response that previously looked like an ordinary coverage miss.
        "variables": json.dumps({"params": {"app_params": [{"app_id": app_id, "version_code": version_code}]}}),
        "access_token": cfg["appBinaryAccessToken"],
    }
    result = post_json(cfg["oculusGraphqlEndpoint"], payload, headers={"Accept": "*/*"})
    info = (((result.get("data") or {}).get("app_binary_info") or {}).get("info") or [])
    saw_binary = False
    for item in info:
        binary = (item or {}).get("binary") or {}
        if binary:
            saw_binary = True
        package = clean(binary.get("package_name"))
        if package:
            return package, "resolved", []

    graphql_errors = _compact_graphql_errors(result.get("errors"))
    if graphql_errors:
        return None, "app_binary_info_graphql_error", graphql_errors
    if not info:
        return None, "app_binary_info_empty", []
    return None, "package_name_missing" if saw_binary else "app_binary_info_empty", []


def resolve_package_from_meta_id(cfg: dict, app_id: str) -> dict[str, object]:
    result: dict[str, object] = {
        "package": None,
        "stage": None,
        "storeVersionCodes": [],
        "legacyVersionCodes": [],
        "binaryAttempts": [],
    }
    tried: set[int | str] = set()
    store_node = {}
    store_error = None

    try:
        store_root = post_form_json(cfg["oculusGraphqlEndpoint"], {
            "doc_id": cfg["storeDetailsDocId"],
            "access_token": cfg["storeAccessToken"],
            "variables": {"applicationID": app_id},
        })
        store_node = (store_root.get("data") or {}).get("node") or {}
    except Exception as exc:
        store_error = str(exc)
        result["storeDetailsError"] = store_error

    store_versions = _store_binary_version_codes(store_node) if store_node else []
    result["storeVersionCodes"] = store_versions

    def try_versions(version_codes: list[int | str], source: str) -> str | None:
        for version_code in version_codes:
            if version_code in tried:
                continue
            tried.add(version_code)
            try:
                package, stage, graphql_errors = _package_from_binary_version(cfg, app_id, version_code)
                attempt = {
                    "source": source,
                    "versionCode": version_code,
                    "stage": stage,
                }
                if graphql_errors:
                    attempt["graphqlErrors"] = graphql_errors
                result["binaryAttempts"].append(attempt)
                if package:
                    return package
            except Exception as exc:
                result["binaryAttempts"].append({
                    "source": source,
                    "versionCode": version_code,
                    "stage": "binary_lookup_error",
                    "error": str(exc),
                })
        return None

    package = try_versions(store_versions, "store-details")
    if package:
        result["package"] = package
        result["stage"] = "resolved_store_binary"
        return result

    legacy_error = None
    legacy_versions: list[int | str] = []
    try:
        legacy_versions = _legacy_binary_version_codes(cfg, app_id)
    except Exception as exc:
        legacy_error = str(exc)
        result["legacyDetailsError"] = legacy_error
    result["legacyVersionCodes"] = legacy_versions

    package = try_versions(legacy_versions, "legacy-release-channel")
    if package:
        result["package"] = package
        result["stage"] = "resolved_legacy_binary"
        return result

    attempts = result["binaryAttempts"]
    attempt_stages = [x.get("stage") for x in attempts if isinstance(x, dict)]
    if not store_node and not legacy_versions:
        result["stage"] = "no_store_node_and_no_binary_version" if not store_error else "store_details_error_no_legacy_binary"
    elif not store_versions and not legacy_versions:
        result["stage"] = "no_binary_version"
    elif "app_binary_info_graphql_error" in attempt_stages:
        result["stage"] = "app_binary_info_graphql_error"
    elif "package_name_missing" in attempt_stages:
        result["stage"] = "package_name_missing"
    elif attempts and all(stage == "binary_lookup_error" for stage in attempt_stages):
        result["stage"] = "binary_lookup_error"
    else:
        result["stage"] = "app_binary_info_empty"
    return result


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


def _id_to_packages(records: dict) -> dict[str, set[str]]:
    result: dict[str, set[str]] = {}
    for package, record in records.items():
        app_id = clean(record.get("metaAppId"))
        if app_id:
            result.setdefault(app_id, set()).add(package)
    return result


def _verified_packages(records: dict) -> dict[str, set[str]]:
    result: dict[str, set[str]] = {}
    for package, record in records.items():
        app_id = clean(record.get("metaAppId"))
        if app_id and record.get("metaPackageVerified") is True:
            result.setdefault(app_id, set()).add(package)
    return result


def enrich_meta(
    cfg: dict,
    records: dict,
    meta_ids: set[str],
    seen: str,
    *,
    placeholder_ids: set[str],
    sidequest_packages: dict[str, set[str]],
    oculusdb_packages: dict[str, set[str]],
    metametadata_packages: dict[str, set[str]],
) -> dict:
    id_to_packages = _id_to_packages(records)
    known_before = len(id_to_packages)
    verified_before = _verified_packages(records)

    # MetaMetadata already maintains a public generated Meta-ID -> Android-package list and
    # updates it daily. Use that data as a package-mapping fallback for the exact cases that
    # would otherwise require reverse-engineering Meta's undocumented app_binary_info resolver:
    # currently unmapped IDs and SideQuest com.autogen placeholders. Artwork/name enrichment
    # still comes from TOM's own Meta fetch below, and this mapping is never marked Meta-verified.
    mapping_seed_ids = (set(meta_ids) - set(id_to_packages)) | set(placeholder_ids)
    metametadata_applied: list[dict[str, object]] = []
    metametadata_ambiguous: list[dict[str, object]] = []
    for app_id in sorted(mapping_seed_ids):
        packages = sorted(metametadata_packages.get(app_id, set()))
        if not packages:
            continue
        if len(packages) > 1:
            metametadata_ambiguous.append({"appId": app_id, "packages": packages})
        added: list[str] = []
        for package in packages:
            rec = records.setdefault(package, {})
            existing_id = clean(rec.get("metaAppId"))
            if existing_id and existing_id != app_id:
                continue
            if not existing_id:
                rec["metaAppId"] = app_id
            rec["lastSeen"] = seen
            rec.setdefault("firstSeen", seen)
            note_package_mapping(rec, "metametadata-map")
            if package not in id_to_packages.setdefault(app_id, set()):
                id_to_packages[app_id].add(package)
                added.append(package)
        if added:
            metametadata_applied.append({"appId": app_id, "packages": added})

    unmapped_ids = set(meta_ids) - set(id_to_packages)
    placeholder_ids_needing_lookup = set(placeholder_ids) - set(id_to_packages)

    ambiguous_ids = {app_id for app_id, packages in id_to_packages.items() if len(packages) > 1}
    source_conflict_ids = {
        app_id for app_id in meta_ids
        if sidequest_packages.get(app_id)
        and oculusdb_packages.get(app_id)
        and set(sidequest_packages[app_id]) != set(oculusdb_packages[app_id])
    }
    multiply_verified_ids = {app_id for app_id, packages in verified_before.items() if len(packages) > 1}

    # Do not blindly validate every current third-party mapping. The Meta binary endpoint is
    # expensive and can rate/network-fail under thousands of requests. Concentrate official
    # package lookup on IDs that actually need repair or disambiguation.
    lookup_ids = sorted(
        unmapped_ids
        | placeholder_ids_needing_lookup
        | ambiguous_ids
        | source_conflict_ids
        | multiply_verified_ids
    )
    print(
        f"Resolving {len(lookup_ids)} focused Meta package mappings "
        f"({len(unmapped_ids)} unmapped, {len(placeholder_ids_needing_lookup)} placeholder IDs still unresolved, "
        f"{len(ambiguous_ids)} ambiguous, {len(source_conflict_ids)} source conflicts)…"
    )

    no_package_ids: list[dict[str, object]] = []
    mapping_errors: list[dict[str, object]] = []
    mapping_conflicts: list[dict[str, object]] = []
    official_packages_added = 0
    official_packages_verified = 0
    resolution_stage_counts: dict[str, int] = {}

    def map_one(app_id):
        try:
            return app_id, resolve_package_from_meta_id(cfg, app_id), None
        except Exception as exc:
            return app_id, None, str(exc)

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        for app_id, resolution, error in pool.map(map_one, lookup_ids):
            known_packages = set(id_to_packages.get(app_id, set()))
            sidequest_known = set(sidequest_packages.get(app_id, set()))
            oculusdb_known = set(oculusdb_packages.get(app_id, set()))
            package = clean((resolution or {}).get("package")) if isinstance(resolution, dict) else None
            stage = clean((resolution or {}).get("stage")) if isinstance(resolution, dict) else None
            if stage:
                resolution_stage_counts[stage] = resolution_stage_counts.get(stage, 0) + 1

            if package:
                if package not in known_packages:
                    official_packages_added += 1
                rec = records.setdefault(package, {})
                merge_record(rec, {"metaAppId": app_id}, "meta", seen)
                note_package_mapping(rec, "meta")
                id_to_packages.setdefault(app_id, set()).add(package)

                # Meta's current Android binary package is canonical. Preserve legitimate
                # historical/third-party aliases, but com.autogen placeholders are discarded
                # before this stage and never become runtime package keys.
                for candidate in id_to_packages[app_id]:
                    candidate_record = records.setdefault(candidate, {})
                    candidate_record["metaPackageVerified"] = candidate == package
                official_packages_verified += 1

                conflicting_packages = sorted((known_packages | sidequest_known | oculusdb_known) - {package})
                if conflicting_packages:
                    mapping_conflicts.append({
                        "appId": app_id,
                        "officialPackage": package,
                        "otherPackages": conflicting_packages,
                        "sideQuestPackages": sorted(sidequest_known),
                        "oculusDbPackages": sorted(oculusdb_known),
                        "knownPackagesBeforeValidation": sorted(known_packages),
                        "resolutionStage": stage,
                    })
            elif error:
                print(f"WARN package mapping failed for {app_id}: {error}", file=sys.stderr)
                mapping_errors.append({
                    "appId": app_id,
                    "knownPackages": sorted(known_packages),
                    "error": error,
                })
            else:
                entry = {
                    "appId": app_id,
                    "knownPackages": sorted(known_packages),
                    "stage": stage or "unknown",
                }
                if isinstance(resolution, dict):
                    for key in (
                        "storeVersionCodes", "legacyVersionCodes", "binaryAttempts",
                        "storeDetailsError", "legacyDetailsError",
                    ):
                        if resolution.get(key):
                            entry[key] = resolution[key]
                no_package_ids.append(entry)

    if no_package_ids:
        print(
            f"WARN Meta package mapping returned no package for {len(no_package_ids)} focused IDs; "
            f"see metadata/{DIAGNOSTICS_PATH.name}",
            file=sys.stderr,
        )
    if mapping_errors:
        print(
            f"WARN Meta package mapping raised errors for {len(mapping_errors)} focused IDs; "
            f"see metadata/{DIAGNOSTICS_PATH.name}",
            file=sys.stderr,
        )
    if mapping_conflicts:
        print(
            f"INFO Meta package validation found {len(mapping_conflicts)} package aliases/conflicts; "
            f"official packages were made canonical and aliases retained",
        )

    targets = [(app_id, sorted(packages)) for app_id, packages in id_to_packages.items() if packages]
    print(f"Fetching official Meta details for {len(targets)} mapped app IDs…")

    def details_one(pair):
        app_id, packages = pair
        try:
            return app_id, packages, fetch_meta_details(cfg, app_id), "meta"
        except Exception:
            try:
                return app_id, packages, fetch_public_experience(cfg, app_id), "meta-public"
            except Exception as exc:
                print(f"WARN Meta details failed for {app_id}: {exc}", file=sys.stderr)
                return app_id, packages, {}, "meta"

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        for app_id, packages, details, source in pool.map(details_one, targets):
            if details:
                for package in packages:
                    merge_record(records.setdefault(package, {}), details, source, seen)

    verified_after = _verified_packages(records)
    return {
        "candidateMetaIds": len(meta_ids),
        "knownPackageMappingsBeforeRun": known_before,
        "verifiedMetaIdsBeforeRun": len(verified_before),
        "packageMappingAttempts": len(lookup_ids),
        "unmappedMetaIdsBeforeLookup": len(unmapped_ids),
        "placeholderMetaIdsBeforeLookup": len(placeholder_ids_needing_lookup),
        "metaMetadataPackageMappingsApplied": len(metametadata_applied),
        "metaMetadataPackageMappingDetails": metametadata_applied,
        "metaMetadataPackageMappingAmbiguities": metametadata_ambiguous,
        "ambiguousMetaIdsBeforeLookup": len(ambiguous_ids),
        "sourceConflictMetaIdsBeforeLookup": len(source_conflict_ids),
        "packageMappingResolutionStages": resolution_stage_counts,
        "packageMappingNoResults": no_package_ids,
        "packageMappingErrors": mapping_errors,
        "packageMappingConflicts": mapping_conflicts,
        "officialPackagesAdded": official_packages_added,
        "officialPackagesVerifiedThisRun": official_packages_verified,
        "verifiedMetaIdsAfterRun": len(verified_after),
        "mappedMetaIdsEnriched": len(targets),
        "mappedPackageAliasesEnriched": sum(len(packages) for _, packages in targets),
    }

def write_diagnostics(diagnostics: dict):
    DIAGNOSTICS_PATH.write_text(
        json.dumps(diagnostics, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote collector diagnostics to metadata/{DIAGNOSTICS_PATH.name}")


def write_outputs(records: dict, seen: str, *, removed_placeholder_packages: set[str]) -> int:
    APPS_DIR.mkdir(parents=True, exist_ok=True)
    index_apps = {}
    valid_packages = re.compile(r"^[A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)+$")
    for package in sorted(records):
        if not valid_packages.match(package):
            continue
        record = records[package]
        index_record = {
            k: record[k]
            for k in (
                "name", "metaAppId", "landscape", "icon", "hero", "sourceHints",
                "packageSourceHints", "metaPackageVerified", "firstSeen", "lastSeen",
            )
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

    # Remove stale runtime files emitted by older collector versions that treated SideQuest
    # com.autogen placeholders as real Android packages.
    removed_files = 0
    for package in sorted(removed_placeholder_packages):
        if not is_sidequest_placeholder_package(package):
            continue
        path = APPS_DIR / f"{package}.json"
        if path.exists():
            path.unlink()
            removed_files += 1
    if removed_files:
        print(f"Removed {removed_files} stale SideQuest com.autogen runtime package files")

    print(f"Wrote {len(index_apps)} TOM metadata records")
    return len(index_apps)


def main():
    cfg = load_json(CONFIG_PATH, {})
    if cfg.get("schema") != 1:
        raise SystemExit("metadata/resolver-config.json schema must be 1")
    prior = load_json(INDEX_PATH, {"apps": {}})
    records = {k: dict(v) for k, v in (prior.get("apps") or {}).items() if isinstance(v, dict)}
    pruned_placeholders = prune_sidequest_placeholder_records(records)
    removed_placeholder_packages = {entry["package"] for entry in pruned_placeholders if entry.get("package")}
    historical_placeholder_ids = {entry["appId"] for entry in pruned_placeholders if entry.get("appId")}
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
        sidequest_ids, sidequest_packages, sidequest_placeholders, sidequest_status = fetch_sidequest(cfg, records, seen)
        diagnostics["sources"]["sideQuest"] = sidequest_status
    except Exception as exc:
        print(f"WARN SideQuest discovery failed: {exc}", file=sys.stderr)
        sidequest_ids = set()
        sidequest_packages = {}
        sidequest_placeholders = {}
        diagnostics["sources"]["sideQuest"] = {"status": "failed", "error": str(exc)}

    try:
        metametadata_packages, metametadata_status = fetch_metametadata_package_map()
        diagnostics["sources"]["metaMetadataPackageMap"] = metametadata_status
    except Exception as exc:
        print(f"WARN MetaMetadata package-map discovery failed: {exc}", file=sys.stderr)
        metametadata_packages = {}
        diagnostics["sources"]["metaMetadataPackageMap"] = {"status": "failed", "error": str(exc)}

    try:
        oculusdb_count, oculusdb_packages = fetch_oculusdb(cfg, records, seen)
        diagnostics["sources"]["oculusDb"] = {"status": "ok", "records": oculusdb_count}
    except Exception as exc:
        print(f"WARN OculusDB discovery failed: {exc}", file=sys.stderr)
        oculusdb_packages = {}
        diagnostics["sources"]["oculusDb"] = {"status": "failed", "error": str(exc)}

    try:
        store_ids, meta_store_status = fetch_meta_section_ids(cfg)
        diagnostics["sources"]["metaStore"] = meta_store_status
    except Exception as exc:
        print(f"WARN current Meta Store enumeration failed: {exc}", file=sys.stderr)
        store_ids = set()
        diagnostics["sources"]["metaStore"] = {"status": "failed", "error": str(exc)}
    historical_ids = {clean(v.get("metaAppId")) for v in records.values() if clean(v.get("metaAppId"))}
    candidate_ids = set(x for x in historical_ids | sidequest_ids | store_ids if x)
    current_placeholder_ids = set(sidequest_placeholders)
    placeholder_ids = historical_placeholder_ids | current_placeholder_ids
    diagnostics["metaDiscovery"] = {
        "sideQuestMetaIds": sorted(sidequest_ids),
        "metaStoreIds": sorted(store_ids),
        "historicalMetaIdCount": len(historical_ids),
        "candidateMetaIdCount": len(candidate_ids),
        "prunedHistoricalPlaceholderPackages": pruned_placeholders,
        "sideQuestPlaceholderMappings": {
            app_id: sorted(packages) for app_id, packages in sorted(sidequest_placeholders.items())
        },
    }
    diagnostics["metaEnrichment"] = enrich_meta(
        cfg,
        records,
        candidate_ids,
        seen,
        placeholder_ids=placeholder_ids,
        sidequest_packages=sidequest_packages,
        oculusdb_packages=oculusdb_packages,
        metametadata_packages=metametadata_packages,
    )
    diagnostics["outputRecords"] = write_outputs(
        records,
        seen,
        removed_placeholder_packages=removed_placeholder_packages,
    )
    write_diagnostics(diagnostics)


if __name__ == "__main__":
    main()
