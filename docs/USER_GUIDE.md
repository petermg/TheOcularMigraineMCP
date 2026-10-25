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

This chapter is for someone installing **The Ocular Migraine Native (TOM)** on a Meta Quest for the first time, replacing the original Tasker-based TOM, or fixing missing access after an update. TOM's startup page is titled **The Ocular Migraine — Setup & Recovery**. Completing it prepares the local ADB connection and verifies the access needed by the Native app. It does **not** require the old Tasker application or a permanently connected PC.

> **Version and verification:** The controls described here were checked against Native TOM **0.1.0-alpha.13.5.138** (`versionCode 2000`). Exact Quest system menus, grant behavior and install prompts can vary by Horizon OS version. Descriptions of what *should* happen are based on source code; final screenshots and behavior still need confirmation on a headset. This is the **user guide**, not a guide to compiling TOM or publishing GitHub releases.

### 1. What to prepare before installation

- **A supported Meta Quest** in which you can install a compatible, signed Native TOM APK. A new user must first get TOM onto the headset through an authorized sideload/installation method; TOM cannot install itself before it is installed.
- **Meta Developer Mode enabled.** This is configured through the Meta Horizon mobile app for the headset linked to your eligible Meta developer account. It is **not** the same switch as Android's **Developer options** inside the headset. See [Meta's current device setup instructions](https://developers.meta.com/vr/documentation/android-apps/enable-developer-mode/) if the mobile app's wording has changed.
- **Wireless debugging access** to the headset's Android settings. TOM will help open Android Settings, but the initial consent and the pairing code come from the headset's own settings UI.
- **The current TOM APK from a source you trust.** For an upgrade, use the APK with the intended package name, valid signing certificate and appropriate Android versionCode. Do not uninstall an existing TOM simply to try an update.
- **A few minutes without interruptions.** The pairing code is temporary. Keep the Android pairing-code dialog accessible until TOM has attempted to pair; do not share the code publicly.

**Safety:** TOM can manage applications, files, runtime settings, recordings and kiosk behavior. Only authorize it on a Quest you own or administer. If you already have legacy profiles or backups, copy important files from `/sdcard/MCP/` before attempting a legacy-to-Native migration. Do not clear the original app's data as a preparatory step.

### 2. Install TOM or update an existing installation

**New installation:** Obtain a signed Native TOM APK and install it using your preferred trusted Quest sideloading method. One example for users who already have Android Platform Tools and a working USB debugging connection from a PC is:

```text
adb install -r TheOcularMigraine.apk
```

The command is **an optional PC-based installation example**, not something to enter into the TOM pairing-code fields. APK filenames and download locations may differ; use the real downloaded filename. If installation succeeds, open **The Ocular Migraine** on the Quest and continue to step 3.

**Updating Native TOM over Native TOM:** An ordinary in-place Android update should preserve the app's private data when the package name and signing certificate match and the new versionCode is acceptable. On the next launch TOM rechecks required grants. Do not confuse retaining Android app data with guaranteeing that every old setting is compatible with a newer file format.

**Replacing the original Tasker-based TOM:** The migration build deliberately keeps the original Android application ID, `openpc.ocular.migraine`. The audited candidate is `versionCode 2000`, higher than the previously inspected legacy build (`1385`). Android will only update in place when the **actual APK signature is compatible** as well as the package/version requirements; merely having the same name is insufficient. The project's migration instructions require checking the *final signed APKs*, not assuming a local debug build has the correct certificate.

If the signed upgrade is accepted, you should have one installed TOM package rather than two competing applications. Native TOM can then show its new **Setup & Recovery** page and request/grant missing native permissions. **Preserved Tasker app data is not automatically proof that its historical profiles were imported into Native TOM.** Keep an independent copy and verify imported material in the relevant workspace before deleting anything.

If Android reports a signature mismatch or downgrade, **stop**. Do not fix this by uninstalling the existing application: uninstalling can discard private data, saved pairing identity and locally stored app settings. Obtain the correctly signed, appropriately versioned APK instead. The maintainers' migration procedure is in [`LEGACY_TASKER_TO_NATIVE_MIGRATION.md`](LEGACY_TASKER_TO_NATIVE_MIGRATION.md).

> **SCREENSHOT NEEDED — S-007:** Android/Quest installation result for a successful *authorized* original-TOM-to-Native-TOM in-place update, ideally alongside the installed Native version. **External Android installation screen:** TOM's own screenshot button is not expected to capture it. Hide package-specific personal details. (Planned file: `images/user-guide/S-007-in-place-native-update.png`)

### 3. Recognize the Setup & Recovery page

When launched, TOM checks previously verified setup state and the currently available permissions. On the **first** run, missing required items direct you to **The Ocular Migraine — Setup & Recovery**. The top of that page includes a progress/summary area and explanations of outstanding **CORE** or **FEATURE** requirements.

The page is organized into three numbered steps:

1. **Developer Mode & Wireless Debugging**, with **Open Android Settings (then tap OPEN)**.
2. **Connect or pair local ADB**, with **Reconnect / Retry Automatic Setup**, a **6-digit code** field, an optional **Pairing port**, **Find Pairing Port**, and **Pair & Connect**.
3. **Automatic permission setup**, which reports verification status and, when applicable, shows **Enable Notifications** / **Open Notification Settings** and **Repair Missing Permissions**.

The **Repair Missing Permissions** button is intentionally conditional: it appears when an attempted automatic grant did not resolve required access. Do not be concerned if it is absent on a successful setup. Successful first-run setup displays confirmation and then opens the **Dashboard automatically**; there is no separate final Grant button to press.

> **SCREENSHOT NEEDED — S-001:** Setup & Recovery, top instructions, status and distinction between Meta Developer Mode and Android Developer options; capture the top of the scrollable page. (Planned file: `images/user-guide/S-001-setup-overview.png`)

### 4. Enable Meta Developer Mode and open Android's Wireless debugging settings

**Part A — Meta Developer Mode (phone):**

1. In the **Meta Horizon** mobile app, select the paired headset, then **Headset Settings → Developer Mode**.
2. Enable **Developer Mode**, following Meta's account verification or pairing instructions if presented. This authorizes development/sideloading features on the headset.
3. Return to the headset. Meta's developer switch alone is **not** the same as turning on Android Wireless debugging.

**Part B — Android Developer options (headset):**

1. On TOM's Setup & Recovery page, press **Open Android Settings (then tap OPEN)**. On the audited Quest path, TOM opens the **Android Settings App info** screen. **Tap OPEN on that screen** to reach Android Settings itself. If you stop on App info, you have not opened the Android Settings menu yet.
2. If **Developer options** is visible, open **System → Developer options → Wireless debugging**.
3. If **Developer options** is missing, open **About headset**, tap **Build number seven times**, then return to **System → Developer options → Wireless debugging**. Quest firmware may rearrange these menu labels.
4. Turn **Wireless debugging** **ON**. If Android asks whether to allow debugging on the current network, choose the appropriate allow option. If available and this is a trusted network, **Always allow on this network** can prevent repeated prompts. Approve additional debugging authorization prompts that belong to your own headset.
5. Choose **Pair device with pairing code**. Keep its six-digit code and the **pairing port** available for step 5 below. The pairing-code screen must still be active when pairing is attempted.

**If the button opens only App info:** That is the intended route on the audited Horizon version, not an error. If Android Settings cannot be opened on your firmware, use the Quest's available authorized Settings route instead; the app cannot guarantee access to firmware-restricted activities.

> **SCREENSHOT NEEDED — S-002:** Lower portion of Setup & Recovery's developer-options instructions and **Open Android Settings (then tap OPEN)**. If adding an image of Android Settings, capture it separately and redact identifiers; do not use it as evidence that TOM can screenshot external system pages. (Planned file: `images/user-guide/S-002-wireless-debugging-instructions.png`)

### 5. Pair TOM with the headset's local ADB service

Native TOM uses an **in-process, headset-local ADB client**. Initial pairing proves that this TOM installation is authorized to talk to the headset's debugging service; after pairing, TOM still needs to establish a working **ADB shell connection**. These are distinct stages.

1. Return to the **Connect or pair local ADB** section in TOM while Android's **Pair device with pairing code** screen is still active.
2. Enter the temporary **six-digit numeric code** in **6-digit code**. TOM rejects non-numeric or non-six-digit input.
3. Press **Find Pairing Port** if you want TOM to discover the active pairing service. A successful discovery displays a port number. If discovery fails, read the **pairing port** from Android's pairing-code popup and type it into **Pairing port (optional)**. A manually entered port must be from **1 to 65535**.
4. Press **Pair & Connect**. TOM chooses the entered port first, otherwise its discovered port, otherwise it tries discovery again. It attempts pairing and then a separate ADB connection.
5. Read the result. **Paired and connected** means TOM can proceed to checking permissions. **Pairing succeeded, but the ADB shell did not connect** means the pairing stage worked but the usable connection still needs attention; use **Reconnect / Retry Automatic Setup**. **Pairing failed** calls for a new/current code and correct port.

**Already paired?** Press **Reconnect / Retry Automatic Setup** first. TOM checks its saved pairing and attempts a connection; a new pairing code is not necessarily required. The button also allows a fresh automatic permission-grant attempt after a problem is repaired.

**Keep the values straight:** The pairing port shown beside the one-time code is **not necessarily the same** as the port for the ADB connection itself. Use the pairing port from the Android popup in the pairing field. Do not enter an IP address, the Quest's device serial, or your Wi-Fi password in that field.

> **SCREENSHOT NEEDED — S-003:** Pairing section showing **6-digit code**, **Pairing port (optional)**, **Find Pairing Port** and **Pair & Connect**, with a **dummy/redacted code**. A real pairing code must never appear in the published guide. (Planned file: `images/user-guide/S-003-pair-and-connect.png`)

### 6. Automatic permission setup and completion

After obtaining a usable ADB shell, TOM examines which permissions and app-ops are missing, requests **only those missing**, and reads the actual permission status back. This is not a blind success message based on whether a shell command exited. A permission denied by Horizon OS can remain unresolved and require manual repair.

On the audited version TOM attempts the relevant automatic grants for **WRITE_SECURE_SETTINGS**, **Usage Stats**, **All files access**, **Display over other apps**, **Microphone**, **Install unknown apps**, and **Notifications** (Android 13+ where applicable). **Accessibility** is *not* silently enabled through ADB; if you select Accessibility-only detection, its service must be enabled manually in Android Settings.

A fully verified initial setup produces a message such as **Required permissions granted and verified. Opening Dashboard…** and opens the Dashboard after a brief confirmation. If access remains missing, the page lists the remaining required items and presents **Repair Missing Permissions** after the automatic attempt. It does **not** keep silently retrying forever.

**Notifications:** TOM may ask once for Android notification permission if an ADB grant did not succeed. You can decline; notifications are **optional for onboarding** and declining them by itself does not block the Dashboard. They help you see background-profile, recording, file-hosting and processing status. If you decline and later change your mind, use **Open Notification Settings** where offered.

> **SCREENSHOT NEEDED — S-004:** Successful setup status *after* ADB connection and verified required access, before the Dashboard opens. This state may be brief; use a controlled test and redact device/network details. (Planned file: `images/user-guide/S-004-setup-success.png`)

> **SCREENSHOT NEEDED — S-005:** Example of Setup & Recovery showing a **missing required permission** and the **Repair Missing Permissions** button; create on a safe test installation rather than revoking permissions on a production headset. (Planned file: `images/user-guide/S-005-manual-setup-repair.png`)

### 7. Understanding Permission Health

From the Dashboard, open **ADB / Tools → Permission Health / Repair** to see the detailed health screen. On Setup & Recovery, **Repair Missing Permissions** can also open it after a failed automatic grant. Permission Health displays counts for **Core missing**, **Feature access missing**, and **Optional not granted**. Every entry shows a ✓ or !, explains the requirement and, if access is missing, offers a repair action.

| Permission Health entry | What TOM uses it for | Classification in normal automatic-detection mode | What to do if missing |
| --- | --- | --- | --- |
| **Local ADB connection** | Quest overrides and ADB-based tools | **Core** | **Reconnect**. Being disconnected does *not* prove Wireless debugging is switched off. |
| **Usage Stats access** | Primary foreground-app detection for automatic Game Profiles | **Core** | **Open Settings** to enable Usage Access, or retry setup's authorized grant. |
| **WRITE_SECURE_SETTINGS** | TOM's Wireless debugging toggle/recovery controls | **Core** | **Grant via ADB** with confirmation; a working ADB connection is required. |
| **All files access** | File Host and direct file operations; shell backup access is separate | **Feature required** | **Open Settings**, allow file-management access for TOM, and recheck. |
| **Install unknown apps** | The standard Android APK installer route; *not* required by TOM's local-ADB installer path | **Feature required** | **Open Settings**, enable installation from TOM if you intend to use this route, then recheck. |
| **Microphone** | Processed or raw microphone capture by TOM | **Feature required** | **Open Settings** / respond to Android's microphone permission prompt. Video-only capture and profiles do not themselves need the mic. |
| **Notifications** | Visibility of foreground/background-operation notifications | **Optional** | **Open Settings** or accept the Android prompt. A denial alone does not block setup. |
| **Display over other apps** | Kiosk preflight and Startup App recovery | **Feature required** | **Open Settings** and authorize overlay access for TOM. |
| **Accessibility service** | Optional foreground-detection fallback and kiosk key-event integration | **Optional** by default; **Core** when Accessibility-only detection is selected | **Open Settings**, enable TOM's Accessibility service only if that mode or feature needs it. |

**Important distinction:** Although several permissions are described as *Feature required*, the current **first-run gate requires both Core and Feature-required permissions to be verified** before it automatically opens the Dashboard. This is stricter than saying an unrelated feature could function without a particular grant. By contrast, optional grants do **not** block entry. The Usage Stats/Accessibility classification changes if you explicitly change TOM's foreground-detection mode.

**Controls on Permission Health:**

- **Recheck All** refreshes the read-only status and counts. It does not authorize grants or turn on debugging.
- **Reconnect ADB** requests a new connection. The message tells you to recheck when connection has settled; it is not instant proof of success.
- **Grant via ADB** appears for missing **WRITE_SECURE_SETTINGS**, asks for confirmation, runs a one-time grant through the existing local ADB session, then verifies the real result.
- **Open Settings** appears for the appropriate Android access page (Usage, Files, Overlay, Installer, Accessibility). For a missing microphone or notification grant, TOM can instead raise Android's permission dialog. Firmware restrictions may sometimes prevent a requested Settings page from opening.
- **Home** returns through TOM's normal navigation gate. If required grants remain missing, navigation can direct you back to Setup & Recovery instead of bypassing setup.

The scan is deliberately **passive**: viewing Permission Health does not execute ADB shell commands or grant anything.

> **SCREENSHOT NEEDED — S-006:** **TOM — Permission Health** showing the summary, representative ✓/! rows, **Recheck All**, **Reconnect ADB**, and at least one relevant repair action. For a long list, capture a second scrolled image using the same ID plus a suffix. (Planned file: `images/user-guide/S-006-permission-health.png`)

### 8. What happens on later launches and after updates

Once setup has been **successfully verified**, TOM stores that completion state. A temporarily disconnected local ADB connection then **does not, by itself, reopen the first-run wizard** when you launch TOM. TOM can instead open the Dashboard and attempt reconnection. The Dashboard's ADB indicator or **ADB disconnected · Reconnect / Repair** action lets you inspect the problem.

If a **different required permission or app-op is later revoked**, the startup gate can send you to Setup & Recovery even if TOM was configured previously. The repair process is intentional: it prevents the app from pretending that privileged features remain available. A previously verified user should not need to re-enter a pairing code just because the connection is momentarily idle.

Android or Horizon updates, changed Wi-Fi network authorization, expired pairing state, or a new app install can affect what needs repair. Check connection state first; then retry automatic setup or use an individual Permission Health action. TOM does not assume every disconnected transport means Wireless debugging is off and will not silently enable it before user-authorized pairing.

### 9. Troubleshooting: choose the symptom you actually see

| Symptom | First check | Correct next action |
| --- | --- | --- |
| **I cannot find Developer Mode on the headset.** | Meta Developer Mode is a **mobile-app** headset setting, not the Android Developer options menu. | Enable it in the Meta Horizon app; then follow TOM's Android Settings instructions. |
| **Open Android Settings only shows App info.** | On the audited Quest firmware, this is expected. | Tap **OPEN** on the Android Settings App info screen. |
| **Developer options is missing.** | Look under **About headset** for **Build number**. | Tap the build number **seven times**, then open **System → Developer options**. |
| **Find Pairing Port found nothing.** | Is **Pair device with pairing code** still open? | Reopen that popup; enter its pairing port manually if discovery remains unavailable. |
| **Pair & Connect says invalid code/port.** | Code must be exactly six digits; manual port must be 1–65535. | Copy the current code and *pairing* port from Android's dialog. |
| **Pairing worked but TOM says ADB disconnected.** | Pairing and shell connection are separate. | Select **Reconnect / Retry Automatic Setup**, and accept legitimate debugging/network authorization prompts. |
| **I keep seeing missing required access.** | Read the **CORE** or **FEATURE** items listed on Setup. | Use **Repair Missing Permissions** after an automatic attempt, authorize the specific Android setting, then **Recheck All**. |
| **Notifications are disabled.** | They are optional for Dashboard entry. | Choose **Enable Notifications** or **Open Notification Settings** when desired. |
| **TOM worked yesterday; today the setup page returned.** | A grant may have been revoked; an ADB disconnection alone normally will not cause this *after completed setup*. | Check individual permission status. Do not uninstall TOM or erase its data as a first troubleshooting step. |
| **Android refuses the in-place APK update.** | The package name, signer or versionCode may not match. | Use a properly signed/higher-version APK; **do not uninstall** the existing app just to make it install. |
| **An old Tasker profile did not appear after migration.** | Android retaining application data does not automatically convert legacy formats. | Preserve `/sdcard/MCP/` and use the relevant Native import workflow where supported; verify before removing backups. |

### 10. Capturing this chapter's documentation screenshots

Native TOM includes a documentation capture control under **Settings → Documentation screenshots**. Once the app is set up, enable the screenshot controls there. The floating **Capture PNG** control hides itself during capture and saves to **`/sdcard/TOM/Screenshots/`**. Copy approved files into `docs/images/user-guide/` using the filenames shown in the placeholders.

For onboarding screens that no longer appear automatically after success, **Setup / Repair** is shown on the Dashboard when there is missing required access or disconnected ADB; it is not a permanently displayed button when everything is healthy. For controlled documentation work, an advanced user with an authorized ADB shell can open the exported setup activity explicitly without revoking permissions:

```text
adb shell am start -n openpc.ocular.migraine/openpc.ocular.migraine.nativeapp.StartupSetupActivity --ez openpc.ocular.migraine.extra.OPEN_SETUP_REPAIR true
```

The command invokes the source-defined **open for repair** flag; it should display the setup instructions even after completed onboarding, but still needs confirmation on the headset. It is **not** a command to pair, grant permissions or change debugging settings. Do **not** deliberately break your working headset's permissions merely to stage a failure screenshot. Success and permission-failure states (**S-004**, **S-005**) may require a dedicated test setup. TOM's own in-app capture does **not** guarantee capture of separately opened Android Settings or installer prompts (**S-007**); use a legitimate external screenshot workflow for those screens if needed. Always hide a real six-digit pairing code, personal headset identifiers, Wi-Fi details and private app information before publishing.

**Next:** [Finding your way around](#finding-your-way-around) explains the Dashboard, workspace navigation and status indicators. [ADB / Tools](#adb--tools) later covers diagnostics and the live shell beyond the initial pairing procedure.

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
