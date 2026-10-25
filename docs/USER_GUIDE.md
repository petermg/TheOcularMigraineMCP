# Native TOM User Guide

[← README](../README.md) · [Developer Guide](DEVELOPMENT_GUIDE.md) · [Release information](NATIVE_UPDATE_RELEASES.md)

> **Comprehensive guide in progress.** Follow the [screen-by-screen screenshot and documentation checklist](USER_GUIDE_SCREENSHOT_CHECKLIST.md). Sections here are currently an overview; do not treat them as a finished reference manual.

This guide describes the **current development build** of The Ocular Migraine Native (TOM), a Meta Quest Android utility. Features may depend on headset firmware, permissions, installed recording components and a functioning local Wireless ADB connection. Menu names describe the current application source; some options appear only when their parent mode is selected.

## Contents

1. [First-run setup and permissions](#first-run-setup-and-permissions)
2. [Finding your way around](#finding-your-way-around)
3. [Game Profiles and benchmarking](#game-profiles-and-benchmarking)
4. [Global / Test](#global--test)
5. [Recording and microphones](#recording-and-microphones)
6. [Media Tools and Audio Mixing Lab](#media-tools-and-audio-mixing-lab)
7. [Backup and Restore](#backup-and-restore)
8. [Apps & Installation and App Compatibility](#apps--installation-and-app-compatibility)
9. [File Host](#file-host)
10. [Kiosk mode](#kiosk-mode)
11. [ADB / Tools](#adb--tools)
12. [Appearance, sounds, and screenshots](#appearance-sounds-and-screenshots)
13. [Daily Broadcast and updates](#daily-broadcast-and-updates)
14. [Files and troubleshooting](#files-and-troubleshooting)

## First-run setup and permissions

1. Install a build intended for your headset. Normal development distribution uses a signed, sideloaded APK; the app package is `openpc.ocular.migraine`.
2. Launch TOM. If required grants are missing, **Setup** displays a checklist. An already verified install should proceed to Home instead of showing the setup page every time.
3. Enable Quest **Wireless Debugging** in the headset's developer settings. When pairing is needed, select **Pair device with pairing code** in Android's Wireless Debugging interface.
4. Enter the **six-digit pairing code** and pairing port in TOM. TOM can attempt to discover the pairing port; if it cannot, enter the port displayed by Android. Pairing and establishing a usable ADB shell are separate steps, and TOM checks both.
5. After connection, TOM attempts to grant and verify missing required privileges. Follow any Quest system prompts. Use **Reconnect / Retry Automatic Setup**, **Repair Missing Permissions**, **Setup / Repair**, and **Permission Health** if required access remains blocked.
6. Notifications help background operations show progress. They are recommended, but declining the notification permission does not by itself block the Dashboard.

**Why these permissions?** TOM uses app usage information for automatic profiles, secure settings for authorized device changes, file-management permission for supported backups/exports, microphone permission for recording, and app-install privileges for the installer. These are powerful permissions; grant them only on a headset you control.

**If pairing fails:** Check that Wireless Debugging is still enabled, the pairing-code screen is open, the code and port are current, and TOM is connecting to the same headset. Use **Reconnect** after the first successful pairing. A completed pairing does not guarantee the subsequent ADB shell is connected.

## Finding your way around

Home contains the primary workspaces: **Game Profiles**, **Global / Test**, **Backup & Restore**, **App Compatibility**, **Recording**, **Media Tools**, **File Host**, **Kiosk**, **Apps & Installation**, and **ADB / Tools**. **Settings** and **About TOM** are accessible from the top of Home; other pages provide Home / Workspaces navigation.

The ADB status indicator on Home shows whether the app has a usable connection. You can inspect its health through **ADB / Tools**, and use **Setup / Repair** if required privileges are missing. You do not need to connect a PC each time merely to use TOM's in-process Wireless ADB when it is already paired and connected.

## Game Profiles and benchmarking

**Purpose:** Associate a Quest application with performance and rendering settings and apply them when the app is detected in the foreground.

A cautious workflow:

1. Open **Game Profiles** and choose the installed game.
2. Review available profile modes and saved slots (including Performance, Balanced, Quality and Custom where applicable).
3. Start with conservative settings. Save the profile, run the game and check that it launches, renders correctly and maintains acceptable responsiveness.
4. Use TOM's benchmark and ground-truth telemetry tools to evaluate the actual game rather than assuming requested settings always equal rendered resolution or sustained performance.
5. Adjust and retest. Keep a known-good profile before pushing CPU, GPU, refresh-rate or resolution values higher.

Automatic profile switching depends on permissions, foreground detection and the headset runtime. Benchmark readings also depend on what telemetry a particular game and OS build expose. Do not treat a profile value as proof that the game rendered at that exact resolution without verification.

## Global / Test

Use **Global / Test** for temporary, headset-wide experiments such as resolution, refresh rate, CPU/GPU level and foveated-rendering controls. These are different from app-specific saved profiles.

- Prefer changing one variable at a time so you know which change produced a result.
- Record the previous settings if you are investigating a performance regression.
- Use **System Default** / clearing controls where present to relinquish a TOM override.
- If the interface, game or refresh behavior becomes unstable, restore known-good settings before continuing.

The supported range of an override does not guarantee that every headset firmware and game accepts it.

## Recording and microphones

**Recording** contains recording-profile controls and capture controls. Two capture paths are available where their prerequisites are present:

| Capture path | Intended use | Important detail |
| --- | --- | --- |
| **Magic Island** | TOM-controlled capture, framing and supported 3D workflows | Relies on the corresponding Quest recording service and its compatibility with your firmware. |
| **MetaCam / Native Video** | Quest native recording and detection workflows | TOM can arm recording detection and optionally capture a companion microphone sidecar. |

### Record a short test

1. Open **Recording** and select the desired recorder.
2. Choose the recording resolution/frame rate/FOV options supported by that mode. Keep first tests short.
3. If you want TOM microphone audio, enable the applicable **TOM mic sidecar** option and choose **Processed Mic** or **RAW Stereo**, as offered for the capture mode. External USB devices, if supported in that workflow, must actually be connected and selected.
4. For the Native Mic Companion path, select the mic source **before arming**. The native mic-type selector is intentionally disabled while arming, armed, recording or finalizing; **Disarm** to switch it.
5. Start/trigger a recording as appropriate for the selected capture pipeline, stop it, and allow finalization/muxing to complete.
6. Open the resulting file and listen to both game and microphone audio; check sync, channels and whether both eyes / expected crop are present when recording in 3D.

**Mic choice:** Processed Mic is suitable for ordinary spoken commentary. RAW Stereo uses the Quest raw audio path in supported modes. It is not automatically interchangeable with a USB mic or with Meta's own microphone capture. Recordings with simultaneous app microphone usage can depend on Android and Meta service behavior.

### Sync and processing

TOM writes recording synchronization data to `/sdcard/TOM/Projects/Sync/`. Related workflows, including **Auto Edit**, read from the same location. Finished video and microphone sidecars are organized under `/sdcard/TOM/Recordings/` and `/sdcard/TOM/Audio/Recordings/`.

An original MetaCam/Magic Island source recording may still be in a Meta-owned folder outside `/sdcard/TOM/`; TOM does **not** relocate the system recorder's files. Its own generated outputs follow the TOM folder layout.

For a complete test: **record video + TOM mic → stop and finalize → confirm sync JSON → run Auto Edit / mix → play completed output**.

### FOV, both-eyes and 3D

The capture page has advanced FOV/crop settings and calculator workflows. True stereoscopic output requires compatible source capture geometry; a 2D file renamed as 3D does not become stereoscopic. Verify output in a compatible player, including eye arrangement and aspect ratio. Some formats store non-square/anamorphic pixels or require correct 3D metadata to display properly.

## Media Tools and Audio Mixing Lab

**Media Tools** supports several modes: preparing side-by-side content for YouTube 3D, converting a both-eyes side-by-side video to one-eye 2D, and processing an ordinary 2D video. Choose the correct source mode before exporting.

- **3D to 2D:** choose left or right eye. TOM crops to that eye and produces a 2D file without adding 3D metadata; it needs re-encoding.
- **2D processing:** normal video adjustments, without adding 3D metadata.
- **Trimming:** the visual trim editor provides **Keyframe / Lossless** (default), **Exact / Smart**, and **Exact / Full Hardware** modes. Keyframe-aligned stream copy avoids a full quality-changing re-encode but may not cut at an arbitrary frame. Exact modes have different performance/encoding tradeoffs.
- **FFmpeg preview:** advanced users can review/edit the generated FFmpeg command before processing. An invalid command can fail; do not assume edited commands are safe or supported.
- **Auto Edit:** processes appropriate media and can use the corresponding TOM microphone synchronization sidecar where present.
- **Audio Mixing Lab:** create mixes and save projects for reopening. Audio output and project files are not the same thing; verify both if you need an editable project.

Expected files include `TOM/Media/2D/`, `TOM/Media/3D/`, `TOM/Media/AutoEdit/`, `TOM/Audio/Mixes/`, and `TOM/Projects/AudioMixingLab/`.

**Playback checks:** inspect the rendered frame size, aspect ratio, left/right eye ordering, audio sync and player metadata. Video file creation alone is not enough to prove a successful 3D export.

## Backup and Restore

**Backup & Restore** supports the fullest portable game backup available through its normal non-root device workflow. This may include the base APK, split APKs, external Data and OBB, depending on what the Quest exposes and what the user selects.

**It does not capture private internal app data** such as `/data/user/0/<package>` without special access. A game that stores progress only in its private sandbox may not have its save restored even if the backup operation reports that its portable components succeeded.

Recommended procedure:

1. Choose a small, noncritical game and create a backup.
2. Inspect the backup contents and `manifest.json` under `/sdcard/TOM/Backups/`.
3. Confirm the manifest's **actually included** components, not only the components requested.
4. Test restoring to a disposable or safely recoverable installation. Verify its installed APK, Data/OBB behavior and application launch.
5. Retain the original data until the restore is proven satisfactory.

Restore normally installs the APK components first and merges readable external Data/OBB. Destination files absent from a backup are not inherently removed. Android can reject outdated target SDK packages, unavailable files and inaccessible directories. Some operations run as detached on-device jobs and may continue beyond a single UI interaction.

The backup format is documented in [Alpha.9 backup format](ALPHA_9_BACKUP_FORMAT.md).

## Apps & Installation and App Compatibility

- **Apps & Installation:** Install a single APK, supported split APK sets and supported package-plus-data bundles. Verify source and signatures; do not install untrusted packages simply because TOM can install them.
- **App Compatibility:** Inspect documented per-game recipes/requirements. Some changes are specific to an app version or Quest runtime. Keep a fallback and follow any on-screen warnings; not every historical game has a validated fix.
- **Universal Patcher:** Where used, preserve its baseline inputs and verify output on a test app before applying it to a valued installation. The central staging/baseline directories are under `TOM/InstallStaging/` and `TOM/UniversalPatcherBaselines/`.

## File Host

File Host provides file browsing and transfers over the local network. Treat an active server as a service accessible to devices on the relevant network. Use a trusted network, check the host's displayed address/session information, and stop sharing when finished. Do not expose a file server to the public internet merely to make a transfer convenient.

## Kiosk mode

Kiosk mode can lock the normal experience to a selected application for a single-purpose installation. **Before enabling it**, choose and verify the configured enable/disable shortcuts (including the volume-button press counts), any administrator PIN and the escape process on your actual Quest. An example or prior alpha's escape count is not a substitute for checking the **current Kiosk settings**. Test that you can exit and administer the headset before leaving it unattended.

## ADB / Tools

This workspace includes Wireless ADB status/reconnect and diagnostic tools, shell/CLI access where supported, permission health, recovery and other device utilities. Commands can alter or erase system/user data; avoid executing unfamiliar commands. The CLI is intended for people who understand Android shell behavior. TOM itself uses its paired local ADB backend for many operations.

## Appearance, sounds, and screenshots

Under **Settings → Customize appearance**, configure themes, accent colors, density, original TOM background images or imported custom artwork, and optional TTF/OTF typefaces. Typeface scope can be headings only, headings + descriptive text, or **all TOM text except RESET FONTS**. Font scale is adjustable from **85% to 200%**. Both **RESET FONTS** controls always use fixed readable system typography and reset the font to system/100%.

Heritage artwork is optional and off by default; opacity/intensity can be set between 5% and 65%. Large typefaces or scales can make some text wrap, and you may need to scroll more often. Toast notifications are kept at system-sized text.

**Settings → Customize sounds** controls optional event audio. Master/event switches are off by default. A configured startup cue is tied to Quest boot completion, not simply opening the app; a TOM-initiated reboot/poweroff cue does not necessarily play for actions invoked through the Quest system menu.

**Settings → Documentation screenshots** exposes the temporary **Capture PNG** button inside TOM when enabled. Exports go to `/sdcard/TOM/Screenshots/`.

## Daily Broadcast and updates

- Native TOM reads `https://raw.githubusercontent.com/petermg/TheOcularMigraineMCP/main/etc/nativenews`; **the original TOM uses a different file** (`etc/news`).
- The response is hidden if blank, whitespace only, `0` or unavailable. There is no fallthrough to the original TOM announcement source.
- A successful automatic announcement appears **at most once per local calendar day** by default.
- **About TOM → Daily Broadcast** fetches the current broadcast any time. There is **no snooze button**.
- **Settings → Daily Broadcast → Show Daily Broadcast every launch** is an **OFF-by-default testing toggle**. Enable it temporarily when previewing HTML messages; disable it again for normal once-per-day behavior.
- Broadcasts support plain text or scrollable HTML with formatting, images and external HTTPS links. The embedded HTML viewer has JavaScript, DOM storage and file/content access disabled.
- Software updates are separate from announcements. Release discovery follows the full Native release rules; automatic installation is not performed. See [Native update/release rules](NATIVE_UPDATE_RELEASES.md).

## Files and troubleshooting

All **new TOM-owned user-facing outputs** are under `/sdcard/TOM/`. The authoritative folder map is in the [main README](../README.md#current-storage-layout) and in `TomStoragePaths.kt`. There is **no automatic migration** of files created by older development versions. Android-private caches/preferences remain private and original Meta recordings remain where the recording service stores them.

| Symptom | First checks |
| --- | --- |
| Setup repeatedly reports missing access | Confirm ADB connection, open Permission Health, retry Setup / Repair; look for a grant the Quest rejected. |
| Recorder does not detect recording or mic | Verify chosen recorder, required service, permission, arming state and mic source selected **before** arming. |
| Output video is missing | Check `TOM/Recordings/` and `TOM/Media/`; verify that recording/export actually finalized. Check system-owned source folders separately. |
| Auto Edit cannot match audio | Verify a new corresponding sync JSON under `TOM/Projects/Sync/` and that media files are still accessible. |
| Exported video is distorted or incorrectly 3D | Inspect actual dimensions, pixel aspect, metadata and left/right eye layout in a capable player. |
| Backup lacks save progress | Consult `manifest.json`; private internal saves cannot be assumed captured. |
| Font or UI is too large | Use **RESET FONTS** in Settings/Appearance to return to system/100%. |
| Daily Broadcast is absent | Confirm the file is nonblank/not `0`, the headset is online, and it was not already shown today; use About TOM to request it manually. |
| Files have unexpected paths | Check you are using **new outputs** from the centralized-storage build; no legacy path probing is installed. |

If reporting an issue, include the exact screen/operation, TOM version, expected vs. observed behavior, Quest model/OS if known, and diagnostics from `TOM/Logs/` when helpful. Check exported logs before sharing them for identifiers or private information.
