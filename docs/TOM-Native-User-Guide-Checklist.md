# Native TOM User Guide — Screen, Screenshot & Documentation Checklist

**Baseline audited:** `TheOcularMigraineNative-v0.1.0-alpha13.5.138-RC.zip` (`versionName 0.1.0-alpha.13.5.138`, `versionCode 2000`, package `openpc.ocular.migraine`). **Guide being replaced:** original Tasker TOM's `petermg/TheOcularMigraineMCP/README.md`. This is a documentation checklist, **not** the native project's README or a claim of completed headset testing.

## How to use this document

- Keep the evolving manual in `docs/USER_GUIDE.md`. Do **not** overwrite Native TOM's development-oriented `README.md`. Once reviewed, publish the replacement to the intended location in the public guide repository as a separate, final step.
- Work **one feature/workspace at a time**. Each documentation patch should edit only `docs/USER_GUIDE.md` and, as needed, this checklist. No Android source changes should be required for guide-only passes.
- In each completed manual section include: **purpose; prerequisites/permissions; navigation; all fields, buttons and options; recommended/default settings; exact how-to procedures; expected results/output paths; warnings and limitations; troubleshooting; related sections; screenshots**. Explain what **System Default**, **Apply**, **Save**, **Reset**, **Read Back**, **Arm**, and **Finalize** do in their respective screens.
- While drafting, use a visible placeholder rather than a broken image: `> **SCREENSHOT NEEDED — S-XXX:** [description] (planned file: images/user-guide/S-XXX-description.png)`. After the user supplies an image, replace with `![Description](images/user-guide/S-XXX-description.png)`.
- In the tables, `[ ]` means **screenshot and corresponding instructions still to be completed**. Check items off only when the appropriate image is received and the manual section accurately describes the tested build. The IDs are stable even if screenshots are later retaken.
- For long, scrollable activities, take **top and bottom** shots as indicated. Prefer the app's own **Settings → Documentation screenshots → Enable screenshot controls**, then **Capture PNG**. The tool hides its button, writes PNG to `/sdcard/TOM/Screenshots/`, and captures the app window (not every Quest system dialog or external app).
- Before uploading public screenshots, obscure headset IDs, network names/addresses, pairing codes, PINs, personal apps, paths revealing identity, and private recordings. Screenshots must come from the Quest build; these are **not** generated mockups.
- Maintain a small test project/file set so the instructions can show *successful outputs*, not just empty defaults. Do not demonstrate destructive restores/patches against valued apps or enable Kiosk without confirming the escape route.

## Screenshot manifest — required shots and state variants

### 01 — Installation, first run, pairing, and recovery

- [ ] **S-001** — Setup & Recovery, top: Developer Mode versus Android developer options.
- [ ] **S-002** — Setup & Recovery, Wireless Debugging instructions and Android Settings launch.
- [ ] **S-003** — Setup & Recovery, pairing-code and pairing-port inputs, Discover, Pair & Connect (**no real code exposed**).
- [ ] **S-004** — Setup & Recovery, successful ADB connection and automatic permission grants.
- [ ] **S-005** — Setup & Recovery, reconnect / repair missing permissions state.
- [ ] **S-006** — Permission Health screen: status/requirements, Recheck All, Reconnect ADB.
- [ ] **S-007** — Native TOM updating the original TOM in place / installation result (**external Android install UI; capture separately if available**).

**Document:** prerequisites, headset-specific Developer Mode navigation, first installation, upgrade/signing compatibility, pairing versus connecting, required/optional permissions, automatic recovery, failure scenarios, privacy/security boundaries. Do not imply an arbitrary user can reproduce the special same-signature migration without the matching signed APK.

### 02 — Dashboard, navigation and shared UI

- [ ] **S-010** — Dashboard top: battery/storage, ADB state, Settings, About TOM.
- [ ] **S-011** — Dashboard first workspace rows: Game Profiles, Global / Test, Backup & Restore, App Compatibility.
- [ ] **S-012** — Dashboard remaining rows: Recording, Media Tools, File Host, Kiosk, Apps & Installation, ADB / Tools.
- [ ] **S-013** — Workspaces chooser from an interior screen.
- [ ] **S-014** — Dashboard permission-attention banner / disconnected ADB state (if reproducible safely).
- [ ] **S-015** — TOM app chooser: search, Quest/TOM picking, list mode.
- [ ] **S-016** — TOM app chooser: gallery mode, artwork change/reset, Use This App.

**Document:** screen map, navigation, what the status indicators mean, system Quest picker versus TOM picker, gallery/list, selecting packages, where global versus per-app settings live.

### 03 — Game Profiles, automatic switching, benchmark

- [ ] **S-020** — Game Profiles: app selection, Quest/TOM picker, app library.
- [ ] **S-021** — Game Profiles: profile engine toggles, detection status, saved Default behavior.
- [ ] **S-022** — App list/gallery, search and app artwork actions.
- [ ] **S-023** — Saved profiles: select, Load, Activate, Import Old TOM, Load Default.
- [ ] **S-024** — Profile Editor: active application, profile slot and automatic slot toggle.
- [ ] **S-025** — Profile Editor: resolution enable/slider, refresh, FFR, Dynamic FFR.
- [ ] **S-026** — Profile Editor: CPU/GPU, AppSW, compositor sharpening.
- [ ] **S-027** — Profile Editor: advanced exact resolution/aspect, frame pacing/performance values.
- [ ] **S-028** — Profile Editor: Save Slot, Apply Now, Apply + Launch, Launch App, other bottom actions.
- [ ] **S-029** — New Benchmark: baseline configuration and test controls.
- [ ] **S-030** — Automated benchmark running: current status and cancel/restore option.
- [ ] **S-031** — Benchmark results: ground-truth/resolution validation and telemetry explanation.
- [ ] **S-032** — Benchmark results/history or results picker (if exposed by the current build).
- [ ] **S-033** — Profile engine applying a saved profile (status feedback; safely reproducible).

**Document:** profile slots/defaults, automatic foreground detector, Usage Stats/accessibility fallback, saving versus activating, all exact properties/limits, performance/battery/thermal considerations, test methodology, adaptive benchmark stages, verifying *actual rendered pixels* rather than trusting requested resolution, telemetry confidence and restoration after cancel/exit. Explain the different meanings of a profile and a one-time global override.

### 04 — Global / Test

- [ ] **S-040** — Global / Test top: pause automatic profile writes, render resolution slider.
- [ ] **S-041** — Global / Test quick controls: refresh, FFR, dynamic FFR, CPU/GPU.
- [ ] **S-042** — Global / Test compositor options: AppSW and sharpening.
- [ ] **S-043** — Global / Test advanced controls: exact dimensions, custom refresh and swap interval.
- [ ] **S-044** — Global / Test Apply, Read Properties, Reset Applied Settings, Resume Automatic Profiles, result.

**Document:** temporary versus persisted effects, global/profile precedence, System Default semantics, reset versus resume, safe test sequence, unsupported headset/game overrides.

### 05 — Recording: saved profiles, settings and capture

- [ ] **S-050** — Recording landing: Saved Profiles and Capture Settings navigation.
- [ ] **S-051** — Saved recording profiles: New, Load, Save, Delete, Import Old TOM.
- [ ] **S-052** — Capture Settings: Magic Island versus MetaCam selector and help.
- [ ] **S-053** — Shared Capture: recording eye and common settings.
- [ ] **S-054** — Magic Island capture: formats, Standard/Cinematic/Custom views, size cap.
- [ ] **S-055** — Magic Island 3D Widescreen, Both Eyes and expected dimensions/status.
- [ ] **S-056** — Magic Island exact Custom view width/height and Casting FOV.
- [ ] **S-057** — Magic Island FPS, bitrate, rolling seconds and quality choices.
- [ ] **S-058** — Magic Island tripod/unattended and sleep/stop options.
- [ ] **S-059** — Magic Island microphone sidecar: Processed Mic versus RAW Stereo, refresh devices, sync offset.
- [ ] **S-060** — Magic Island Start Recording / Stop & Finalize and a valid status/result.
- [ ] **S-061** — MetaCam: native capture resolution, FPS, bitrate, full-rate capture.
- [ ] **S-062** — Capture FOV Method(s): method chooser, recommended and advanced combinations.
- [ ] **S-063** — System Capture FOV in degrees, automatic eye crop, exact IN/OUT/UP/DOWN.
- [ ] **S-064** — Advanced mirrored Magic Island view → System crop helper.
- [ ] **S-065** — Magic Island OpenXR FOV auto-match and manual eye bounds.
- [ ] **S-066** — MetaCam + TOM Mic Companion: source, Arm, Disarm, status.
- [ ] **S-067** — Audio Processing / Game Mix: presets, gain, ducking, timing, limiter.
- [ ] **S-068** — Finalization: defer mux, Audio Mixing Lab launch, pending recordings.
- [ ] **S-069** — Apply/Read Back/Reset recording settings and status feedback.
- [ ] **S-070** — A real finalized 2D capture example (player/file info; external view if needed).
- [ ] **S-071** — A real Both Eyes / stereoscopic widescreen capture example (dimensions/eye geometry).
- [ ] **S-072** — Recorder-specific help or compatibility/limits, if a dedicated TOM dialog is used.

**Document:** every recorder/mode and field, system versus OpenXR FOV methods, per-eye aspect ratios and anamorphic output, raw versus processed mic, USB/headset mic restrictions, capture/recording permission behavior, Audio Mixing Lab versus immediate mux, where output goes, exact start/stop procedures, error recovery. Do not present all formats and captures as working on every Horizon OS or headset.

### 06 — Media Tools, trim, Auto Editor

- [ ] **S-080** — Media Tools: choose source video and three processing modes.
- [ ] **S-081** — Prepare YouTube 3D: SBS/FFmpeg mode, aspect/output settings.
- [ ] **S-082** — Prepare VR180 / Spatial Media V2 mode and aspect options.
- [ ] **S-083** — Convert Both Eyes 3D → 2D; left/right eye selection.
- [ ] **S-084** — Process ordinary 2D video, with no 3D metadata.
- [ ] **S-085** — Media trim/audio offset/tempo fields and Review & Create action.
- [ ] **S-086** — Visual Trim Editor timeline, play, Set Start/End, keyframe navigation.
- [ ] **S-087** — Trim Editor: Keyframe/Lossless (default), Exact/Smart, Exact/Full Hardware.
- [ ] **S-088** — Generated FFmpeg command preview/edit dialog (if supplied by this build).
- [ ] **S-089** — Export/progress/completed output, including file location.
- [ ] **S-090** — Auto Editor source, detector/audio/motion options and saved profile.
- [ ] **S-091** — Auto Editor Analyze & Build Edit Plan with KEEP/CUT timeline.
- [ ] **S-092** — Auto Editor Apply / Export JSON result and optional Help.

**Document:** modes and metadata differences, when re-encoding is mandatory, frame-accurate vs stream-copy trims, Smart GOP handling and full hardware encode fallback, audio timing, FFmpeg command review, output verification, Auto Editor matching mic sidecars and analysis/profile settings.

### 07 — Audio Mixing Lab

- [ ] **S-095** — Audio Mixing Lab initial projects/source picker, remix/open/relink.
- [ ] **S-096** — Mic Leveling modes and gentle dynaudnorm custom controls.
- [ ] **S-097** — Loudnorm dynamic/preserve alternatives and advanced targets.
- [ ] **S-098** — Custom Game Mix gain, ducking/sidechain, limiter.
- [ ] **S-099** — Render full audio mix progress/finished master.
- [ ] **S-100** — Audio master playback, scrub, Mux Now.
- [ ] **S-101** — Reopened editable mix project and rendered output locations.

**Document:** sidecar master versus final game/mic mix, non-destructive processing, modes/field units, relinking, project JSON, mix preview, final mux, loudness clipping, synchronization and troubleshooting.

### 08 — Backup & Restore, including TOM configuration

- [ ] **S-110** — Backup & Restore landing: Create Backup / Restore / Manage / TOM Configuration modes.
- [ ] **S-111** — Create: Quest/TOM app picker, list/gallery, search.
- [ ] **S-112** — Create: APKs/Data/OBB checkboxes and Full/Data Only presets.
- [ ] **S-113** — Create: preflight storage and successful backup result.
- [ ] **S-114** — Restore: Internal TOM backups, USB/removable chooser, search and gallery.
- [ ] **S-115** — Restore: selected backup details/manifest and component availability.
- [ ] **S-116** — Restore: APK/Data/OBB checkboxes, optional runtime grants and low-target override.
- [ ] **S-117** — Restore: Clear Installed App Data, Restore Selected, Delete Backup and safety dialog.
- [ ] **S-118** — Restore: progress and component-by-component success/failure report.
- [ ] **S-119** — TOM Configuration: Export JSON and Restore JSON.
- [ ] **S-120** — Backup folder/manifest example in a file viewer (external, if necessary).

**Document:** exact portable scope, manifest and component verification, split APK installs, merge/non-delete semantics, private `/data/user/0` **not backed up**, guide to what is/isn't recoverable, removable backups, detached job lifecycle, failure cases, configuration backup independent from app data, destructive-operation warnings.

### 09 — Apps & Installation, compatibility & patching

- [ ] **S-125** — Apps & Installation: Choose APK, installer choice and permissions option.
- [ ] **S-126** — Apps & Installation: Choose APK Set / split APK flow.
- [ ] **S-127** — Apps & Installation: Choose Bundle Folder (APK + external Data/OBB).
- [ ] **S-128** — Installer success/failure/status with signature or SDK compatibility explanation.
- [ ] **S-130** — App Compatibility: recipe selector, hardware status and analysis.
- [ ] **S-131** — App Compatibility: runtime recipe and launch/reset actions.
- [ ] **S-132** — App Compatibility: backup/patch/install, clean initialization, DATA finish, rollback actions.
- [ ] **S-133** — Universal Patcher: Installed App versus APK File and loaded baseline.
- [ ] **S-134** — Universal Patcher: Auto Dynamic Resolution analysis, install/update/remove.
- [ ] **S-135** — Universal Patcher: manual ELF library/function search, force-false/true queue.
- [ ] **S-136** — Universal Patcher: patch queue, recipe state, rebuild/restore controls.
- [ ] **S-137** — Universal Patcher: import/export recipe and advanced safeguards.

**Document:** inputs, source trust, signature updates, split APK constraints, exact compatibility recipe version/validation, publisher-signature loss, baseline lifecycle, safety backups, patcher limits, external DATA initialization, rollback. Separate documented validated recipes from experimental utilities.

### 10 — File Host

- [ ] **S-140** — File Host: access permissions, start/stop, port, keep-alive mode.
- [ ] **S-141** — File Host running: local address, transfer URL, status.
- [ ] **S-142** — File Host desktop/mobile browser: folder navigation, download, upload (external screenshot).
- [ ] **S-143** — File Host: storage-permission error or missing access recovery.

**Document:** local-network security (no authentication), storage scope, port, media/downloads, file overwrite and upload behavior, sleep keeping alive, error codes, stop the service afterward.

### 11 — Kiosk

- [ ] **S-150** — Kiosk: Configuration / Status & Safety tabs.
- [ ] **S-151** — Kiosk: app picker, current selection and admin PIN controls (**PIN obscured**).
- [ ] **S-152** — Kiosk: Volume Up/Down counts and Save Configuration (Keep Off).
- [ ] **S-153** — Kiosk: Status & Safety preflight/check results.
- [ ] **S-154** — Kiosk: Enable, Resume, Disable, Clear Configuration and current state.
- [ ] **S-155** — Kiosk PIN / volume recovery flow (safe test with known recovery).

**Document:** exact setup, 3–50 count range, initial 25 default where used, enable/disable with PIN, preflight, suspension, fail-open reboot, emergency escape and differences from Startup App/legacy child lists. Include a prominent *verify escape BEFORE use* warning.

### 12 — ADB / Tools, redirects, Startup App and diagnostics

- [ ] **S-160** — ADB / Tools: Usage Stats primary and Accessibility fallback.
- [ ] **S-161** — ADB / Tools: Wireless ADB automatic recovery, Developer settings and privileged enable.
- [ ] **S-162** — ADB / Tools: pairing code/port, Discover, Pair, Auto Connect, Restart/Disconnect.
- [ ] **S-163** — ADB / Tools: boot recovery toggles and last recovery result.
- [ ] **S-164** — ADB / Tools: Device Power actions (reboot, power off, restart Home).
- [ ] **S-165** — ADB / Tools: Startup App Quest/TOM picker, set/clear, Launch Now and boot toggle.
- [ ] **S-166** — ADB / Tools: App Redirects source/destination rules, enable and saved list.
- [ ] **S-167** — ADB / Tools: OVR Metrics status, overlay, app/store controls.
- [ ] **S-168** — ADB / Tools: diagnostic log Capture Now / Export / Clear.
- [ ] **S-169** — ADB / Tools: profile engine event log and status readouts.
- [ ] **S-170** — ADB / Tools: advanced privileges/properties/core reset/Storage Lab.
- [ ] **S-171** — ADB / Tools: quick shell command and console output.
- [ ] **S-172** — Live ADB Shell Console: command, streaming output, Auto-scroll, Stop, Copy, Clear.
- [ ] **S-173** — Live ADB Shell Console: keyboard/history usage or example command (non-destructive).
- [ ] **S-174** — Storage Lab experimental diagnostics (explicitly label test-only).

**Document:** what ADB is, self-pairing versus PC ADB, permissions, experimental classic TCP :5555, choosing detection method, boot recovery, Startup App and redirects, OVR Metrics, exact utility actions, shell safety, diagnostics privacy/locations, connectivity troubleshooting.

### 13 — Settings: appearance, sounds, metadata and documentation

- [ ] **S-180** — Settings top: Appearance, RESET FONTS, sounds, Daily Broadcast.
- [ ] **S-181** — Settings: Documentation Screenshots enabled/disabled; Capture PNG demonstration.
- [ ] **S-182** — Settings: metadata resolver, preload, artwork/cache refresh and advanced source URL.
- [ ] **S-183** — Customize Appearance: theme and accent choices.
- [ ] **S-184** — Customize Appearance: density, font scaling and font selection/import/scope.
- [ ] **S-185** — Customize Appearance: heritage background asset/custom import/opacity.
- [ ] **S-186** — Customize Appearance: live preview, Apply, Reset preview, RESET FONTS.
- [ ] **S-187** — TOM Sounds: master switch, three event switches, built-in cues.
- [ ] **S-188** — TOM Sounds: import, preview, restore built-in and stop.

**Document:** availability/defaults, state persistence, safe font fallback, original font licensing/optional assets where relevant, effects of opacity/scale, exact startup/shutdown/first ADB sound triggers, supported audio formats and limits, artwork network/privacy behavior, screenshot capture mechanics and paths.

### 14 — About, Daily Broadcast, updates and help

- [ ] **S-190** — About TOM: version, code, author, links.
- [ ] **S-191** — About TOM: Daily Broadcast and manual fetch example.
- [ ] **S-192** — About TOM: update checks, availability/status, GitHub Releases, verified APK download.
- [ ] **S-193** — Update/install confirmation or no-update state (avoid invented available releases).
- [ ] **S-194** — Example error/recovery screen with its original result text, if illustrative.

**Document:** `etc/nativenews` versus original TOM's `etc/news`, once-per-day policy and test override, safe HTML behavior, compatible full releases versus experimental builds, no automatic installation, verifying signing/update identity, support channels, where to report issues and collect non-sensitive logs.

## Old guide migration cross-check

The old public Tasker TOM guide groups controls under **Main**, **Recording**, **Tools**, and **Misc**, and contains legacy installation flows and screenshots. Native TOM reorganizes them into the workspaces above. Cross-reference, but **do not copy old instructions as if current**.

| Legacy guide topic | Native destination / action |
|---|---|
| Original Main: resolution, CPU/GPU, FFR, refresh | Global / Test; Game Profiles |
| Original Main: saved game profiles and defaults | Game Profiles / Profile Editor |
| Original Main: game backups | Backup & Restore (separate Create/Restore/Config) |
| Original Recording | Recording + Media Tools + Audio Mixing Lab |
| Original Tools: ADB, OVR Metrics, Startup App, shortcuts | ADB / Tools, App Redirects, Startup App, Live ADB Shell |
| Original Tools: kiosk | Kiosk (dedicated safety-aware workspace) |
| Original Misc: Web server | File Host |
| Original Misc: preferences, utilities | Settings, ADB / Tools, About TOM |
| Original Misc/Tools: blacklist/whitelist/child account | **Legacy-only / not identified in this audited Native UI**; verify before documenting or claiming parity |
| Original one-time installation / reboots | Replace with current Native Setup & Recovery + migration guidance |
| Original video 3D injection / processing | Media Tools (SBS/VR180, 3D→2D, normal 2D, Trim, Auto Editor) |

## Workflow for each future documentation patch

1. **Source-check** target activity, XML, conditional visibility and relevant controller/service behavior. Record the authoritative source baseline. Do not guess behavior from labels alone.
2. **Write** the complete corresponding section in `docs/USER_GUIDE.md`, with all options, examples, failures, and screenshot placeholders using the IDs above.
3. **Deliver** a pure Git patch relative to the **Native TOM project root**; run `git apply --check` against the matching ZIP/source before delivery. Never put `/mnt/data/...` paths in patch headers.
4. **User captures** images on the Quest and identifies the matching `S-XXX` IDs. Images live in `docs/images/user-guide/` in the documentation checkout; original app screenshots remain in `/sdcard/TOM/Screenshots/` until copied.
5. **Verify** the screenshot matches current UI and procedure. Mark checklist complete and revise the manual only if testing contradicts the source or reveals a firmware-dependent behavior.
6. **Publish** only once guide content/images are complete; avoid altering the original public `README.md` or Native project's own README prematurely.

## Coverage audit notes

- Source contains **25 registered Android activities**, including internal pickers/editors and dynamically generated About/Compatibility/Universal Patcher/Storage Lab pages. Manifest registration is not a guarantee every page is independently navigable.
- Most pages use XML layouts; **About**, **App Compatibility**, **Universal Patcher**, **Storage Lab**, and several states use programmatically constructed UI, so an XML-only inventory would miss controls.
- New documentation screenshot feature is implemented in `TomDocumentationCapture.kt` and `TomThemedActivity.kt`; it uses `PixelCopy` where possible, falls back to drawing Android views, and saves through `MediaStore`. This cannot prove capture of external Quest settings, Android install prompts, or separately composited imagery.
- Current `docs/USER_GUIDE.md` is a short starting overview, not yet exhaustive. Current `docs/TOM_UI_WORKSPACE_INVENTORY_13_5_25.md` is a historical inventory and **not** an authoritative list for Alpha 13.5.138.
- A checklist item covering dynamic/result states may require multiple screenshots when a single image cannot show all controls. Capture additional pictures with suffixes `-a`, `-b` as needed; preserve the parent ID.
