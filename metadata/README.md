# TOM shared app metadata

This directory is the optional shared-data side of TOM's App Library & Artwork resolver. The Android
app does **not** require these files to function: it ships built-in resolver defaults and can perform
targeted provider lookups for apps the user actually browses.

`resolver-config.json` contains declarative endpoint/document-ID values that can be updated when an
undocumented Meta/Oculus interface changes. TOM validates the runtime subset before accepting it and
never downloads executable resolver code.

`tom-app-index.json` is the retained package-name index. `tools/update_tom_app_metadata.py` merges the
previous index with current Meta Store discovery, SideQuest, and lower-priority OculusDB historical
gap filling, then enriches known Meta IDs from Meta where possible. OculusDB is consumed only by this
central collector; the Android runtime never downloads its bulk all-apps feed. Historical mappings are
retained even when an app disappears from today's Store. The workflow writes compact
`apps/<android.package.name>.json` records for runtime use; observation timestamps remain only in the
aggregate index so routine daily runs do not rewrite every per-package file.

`collector-diagnostics.json` is generated alongside the index on every collector run. It records
whether SideQuest/OculusDB/Meta Store discovery succeeded, the Meta IDs discovered from SideQuest and
the configured Meta Store sections, package-name lookups that returned no result or raised an error,
and any package aliases/conflicts discovered when a third-party or historical mapping differs from
Meta's current Android binary package. This file is intended for diagnosing coverage holes such as a
current Store app that never receives an `apps/<package>.json` record; it is not consumed by the
Android app.

Current SideQuest and Meta Store IDs are validated against Meta's own Android binary package lookup.
Successful validations are retained in the aggregate index with `metaPackageVerified: true` and
`packageSourceHints`; those collector-only fields are omitted from the compact runtime package files.
If Meta reports a different current package, the official package becomes canonical while historical
or third-party package aliases are retained and receive the same official metadata/artwork. This
preserves compatibility with older installed builds without allowing a stale third-party package
mapping to block the current official package.

Meta Store enumeration is page-resilient: each failed page is retried with backoff, and a persistent
section/page failure is recorded in diagnostics without discarding IDs already discovered from other
sections/pages. A transient Meta HTTP failure therefore no longer collapses a partially successful
Store crawl to zero IDs.

The SideQuest collector request deliberately sends `Origin: https://sidequestvr.com`, matching the
browser-origin requirement of the current SideQuest search endpoint. SideQuest remains the preferred
third-party source; OculusDB is still retained only as lower-priority historical/delisted gap filling.

The included `.github/workflows/update-tom-app-metadata.yml` runs the collector daily and can also be
started manually. After this repository is published, point **Settings → App Library & Artwork →
Advanced resolver updates** at the raw metadata base path, for example:

`https://raw.githubusercontent.com/petermg/TheOcularMigraineMCP/main/metadata`

`raw.githubusercontent.com` does not provide directory listings, so opening that base path by itself
may return 404. TOM appends individual filenames such as `/resolver-config.json` and
`/apps/<android.package.name>.json` before making requests.

A project maintainer may instead bake that same base path into `BuildConfig.TOM_METADATA_BASE_URL`.
It is baked into current TOM builds as the default shared metadata source; users can override it in
Settings, and clearing an override returns to the baked default.

## SideQuest placeholder packages and focused Meta package repair

Some Meta-hosted SideQuest listings use `com.autogen.<number>` as an internal placeholder rather than
the Android package actually installed on Quest. The collector treats those values as **Meta-ID-only
discovery**: the placeholder is not emitted as an `apps/<package>.json` runtime record, historical
placeholder records from older collector runs are pruned, and their stale runtime JSON files are
removed on the next successful run.

Package repair now uses a focused queue instead of revalidating every current SideQuest/Meta Store
mapping. Official Meta package lookup is attempted for unmapped Meta IDs, SideQuest placeholder IDs,
ambiguous IDs, and source conflicts. This keeps the undocumented Meta binary endpoint out of the
thousands-of-requests failure mode while still targeting the records that can actually improve
coverage.

For package repair, the collector first extracts Android binary version codes exposed by the already
working Meta Store-details response (`lastRevision`/`firstRevision` revision binaries) and asks Meta's
binary-info endpoint for the corresponding `package_name`. The older `release_channels` app-details
path remains as a fallback. `collector-diagnostics.json` records the terminal resolution stage and
per-version binary attempts (`resolved_store_binary`, `resolved_legacy_binary`, `no_binary_version`,
`app_binary_info_empty`, `package_name_missing`, or network/error stages), so future coverage gaps show
where resolution stopped instead of appearing as an undifferentiated "no result".
