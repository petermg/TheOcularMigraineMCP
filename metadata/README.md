# TOM shared app metadata

This directory is the optional shared-data side of TOM's App Library & Artwork resolver. The Android
app does **not** require these files to function: it ships built-in resolver defaults and can perform
targeted provider lookups for apps the user actually browses.

`resolver-config.json` contains declarative endpoint/document-ID values that can be updated when an
undocumented Meta/Oculus interface changes. TOM validates the runtime subset before accepting it and
never downloads executable resolver code.

`tom-app-index.json` is the retained package-name index. `tools/update_tom_app_metadata.py` merges the
previous index with current Meta Store discovery, OculusDB, and SideQuest, then enriches known Meta IDs
from Meta where possible. Historical mappings are retained even when an app disappears from today's
Store. The workflow writes compact `apps/<android.package.name>.json` records for runtime use; observation timestamps remain only in the aggregate index so routine daily runs do not rewrite every per-package file.

The included `.github/workflows/update-tom-app-metadata.yml` runs the collector daily and can also be
started manually. After this repository is published, point **Settings → App Library & Artwork →
Advanced resolver updates** at the raw metadata directory, for example:

`https://raw.githubusercontent.com/petermg/TheOcularMigraineMCP/main/metadata`

A project maintainer may instead bake that same URL into `BuildConfig.TOM_METADATA_BASE_URL`. It is
baked into current TOM builds as the default shared metadata source; users can still override or clear it in Settings.
