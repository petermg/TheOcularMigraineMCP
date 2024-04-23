# The Ocular Migraine: {Dev Mode} Master Control Program.
 <img alt="GitHub Downloads (specific asset, all releases)" src="https://img.shields.io/github/downloads/petermg/TheOcularMigraineMCP/version?style=social&label=visits&color=2417f1">
 
[<img alt="GitHub Downloads (all assets, all releases)" src="https://img.shields.io/github/downloads/petermg/TheOcularMigraineMCP/total?style=for-the-badge&color=b3f117">](https://github.com/petermg/TheOcularMigraineMCP/releases)

[<img alt="GitHub Downloads (specific asset, all releases)" src="https://img.shields.io/github/downloads/petermg/TheOcularMigraineMCP/TheOcularMigraine.apk?style=for-the-badge&labelColor=000000&color=00d9f2">](https://github.com/petermg/TheOcularMigraineMCP/releases/latest/download/TheOcularMigraine.apk)


### This is an applicaiton for use with the Oculus / Meta Quest mobile VR headsets, including the original Oculus Quest, Oculus / Meta Quest 2, Meta Quest Pro, Meta Quest 3.

# Table Of Contents:
(click on the arrows for each screen to open the Table Of Contents for that section)

- # [Proper Installation](#installation)

<details><summary>

# [The Main Screen](#main-screen)</summary>

  * ## [Top Section](#main-screen-top-section)
    * [Statistics Readout](#statistics)
    * [About](#about)
    * [Font Size Adjustment](#font-size-adjustment)
    * [Resolution Slider](#resolution-slider)
    * [Fixed Foveated Rendering (FFR) Level](#ffr-level)
    * [CPU Level](#cpu-level)
    * [GPU Level](#gpu-level)
  * ## [Middle Section](#main-screen-middle-section)
    * [Display Frequency](#display-frequency)
    * [Default Display Settings](#default-display-settings)
    * [Reset ALL settings to default](#reset-all-settings-to-default)
    * [Manage Game Profiles](#manage-game-profiles)
    * [Save Game Profile](#save-game-profile)
    * ### [Game Backup Menu](#game-backup)
      * Backup Options
        * [Game + Data (Full Game Backup)](#full-game-backup)
        * [Game Data Only](#game-data-backup-only)
      * Restore Options
        * [Full Game](#full-game)
        * [Game ONLY](#game-only)
        * [Game Data](#game-data)
  * ## [Bottom Section](#main-screen-bottom-section)
    * [User Defined Resolution Presets](#user-defined-resolution-presets)
    * [Disable](#disable)
</details>
<details><summary>
 
# [The Recording Screen](#recording-screen)</summary>
  * ## [Top Section](#recording-screen-top-section)
    * [Resolution Presets](#resolution-presets)
    * [Custom Resolution](#custom-resolution)
    * [Recording Bitrate](#recording-bitrate)
  * ## [Middle Section](#recording-screen-middle-section)
    * [Recording FrameRate](#recording-framerate)
    * [Recording Eye](#recording-eye)
    * [Start and Stop Recording](#start-recording-and-stop-recording)
  * ## [Bottom Section](#recording-screen-bottom-section)
    * [FOV Crop](#fov-crop)
    * [Save Recording Profile](#save-recording-profile)
    * [Load Recording Profile](#load-recording-profile)
    * [Inject 3D Metadata](#inject-3d-metadata)
    * [Process 2D Video](#process-2d-video)
    * [adaclocks](#adaclocks)
    * [Swap Interval](#swap-interval)
    * [Reset Recording to default](#reset-recording-to-default)
</details>
<details><summary>

# [The Tools Screen](#tools-screen)</summary>
  * ## [Top Section](#tools-screen-top-section)
    * [Install APK via ADB](#install-apk-via-adb)
    * [Input ADB command](#input-adb-command)
    * [ADB Shell command](#adb-shell-command)
    * [Console Output Screen](#console-output-screen)
  * ## [Middle Section](#tools-screen-middle-section)
    * [Enable OVR Metrics Tool Overlay](#enable-ovr-metrics-tool-overlay)
    * [File Manager](#file-manager)
    * [SideQuest](#sidequest)
    * [Set Kiosk Mode App](#set-kiosk-mode-app)
    * [Un-set Kiosk Mode](#un-set-kiosk-mode)
    * [Create Shortcut App](#create-shortcut-app)
    * [Create Startup App](#create-startup-app)
    * [Disable Startup App](#disable-startup-app)
  * ## [Bottom Section](#tools-screen-bottom-section)
    * [Access Lists](#access-lists)
      * [Create White List](#create-white-list)
      * [Create Black List](#create-black-list)
      * [Disable Access Lists](#disable-access-lists)
      * [Delete Access Lists](#delete-access-lists)
      * [Access List Enforcement Method](#access-list-enforcement-method)
</details>
<details><summary>

# [The Misc Screen](#misc-screen)</summary>
  * ## [Top Section](#misc-screen-top-section)
    * [Switch App Launch Detection Method](#switch-app-launch-detection-method)
    * [Disable Battery Optimization](#disable-battery-optimization)
    * [Enable All File Access](#enable-all-file-access)
    * [Disable Notifications](#disable-notifications)
    * [Android Settings](#android-settings)
  * ## [Middle Section](#misc-screen-middle-section)
    * [Web Server File Sharing and Remote Uploading](#web-server-file-sharing-and-remote-uploading)
  * ## [Bottom Section](#misc-screen-bottom-section)
    * [Restart the Home Environment](#restart-home-environment)
    * [Check Enabled Profiles](#check-enabled-profiles)
    * [Devices](#devices)
    * [Restart ADB Server](#restart-adb-server)
    * [Reboot](#reboot)
    * [Current Settings](#current-settings)
    * [Load System Defaults](#load-system-defaults)
    * [Save Settings to file](#save-settings-to-file)
    * [Load Settings from file](#load-settings-from-file)
    * [Delete BlazeRush Config](#delete-blazerush-config)
    * [Apps I Worked On](#apps-i-worked-on)
</details>


##




## Installation


1. Make sure your device is in developer mode. If it isn't, watch this 60 second video here which shows you how: https://youtu.be/jB1gwgSpU3E

2. Download the zip file ["Install.zip"](https://github.com/petermg/TheOcularMigraineMCP/releases/download/v1.0/Install.zip) and extract it to any folder on your computer.
 
 ![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/248e2c89-a0fa-4906-b4dd-612938073e33)

3. Download the latest version of The Oculus Migraine apk file from the latest releses [here.](https://github.com/petermg/TheOcularMigraineMCP/releases)

4. Take the APK you downloaded and drag and DROP it onto the bat file named "Installation.bat" from the zip file "Install.zip" that you extracted earlier and follow the onscreen prompts. DO NOT CLOSE THE BAT FILE WINDOW after the file has been installed! Press any key to continue as it then runs the command "adb tcpip 5555" which opens up the port on the Quest for this application to authenticate itself on the very first run. This is the one and **ONLY** time your PC will be required for this!

5. Put on your headset.

6. Go to UNKNOWN SOURCES.

7. Click on "The Ocular Migraine". You will see the following screen:
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/b14f0a4a-854f-4edb-8a4b-8c6a84f20fb8)



8. After it begins to load, you will be prompted a total of 3 different times with a prompt that says "Allow USB debugging?". Each time you must select the option at the bottom which says "Always allow from this computer". After you select this option the first time, the applicaiton will close. Launch it again by clicking on it from UNKNOWN SOURCES and you will be propmted 2 more times to "Allow USB debugging?" Again select "Always allow from this computer".

9. Now once the app is up and running, select "MISC" from the bottom and it will take you to the MISC page.

10. Select "Battery Optimization Settings" to open the Battery optimization settings.

11. Make sure "The Ocular Migraine" is set to "NOT OPTIMIZED". By default soon after this application is installed, the Quest will "optimize" it, which ends up KILLING the app from running in the background. This prevents the app from being able to initiate custom gaming profiles. If you do not see The Ocular Migraine listed under "NOT OPTIMIZED", click on the drop down menu showing "NOT OPTIMZED" and select "ALL APPS". Find The Ocular Migrine and click on it and select "Dopn't optimized" then click DONE. If you have already found The Ocular Migraine set as NOT OPTIMIZED without changing anything, chances are the Quest will end up "optimizing" it later. So you may want to revisit these settings later on to change it back. I have found once I change it back manually, the Quest honors the user selection.

12. Next select "Notification Settings" from the MISC page.

13. Find The Ocular Migraine, if it's not already showing, you can select ALL APPS from the dropdown menu. Click on the toggle to DISABLE notificaitons for The Ocular Migraine. This is NOT required but recommended.

### NOTE: From now on, after each reboot of your device, the **FIRST** time you launch The Ocular Migraine, it will prompt you to "Allow USB debugging?". Select "Always allow from this computer" each time. This only happens on the initial launch of the applicaiton after a reboot of your device. It will not ask this question again until the next device reboot on it's inital launch.

Each screen has 3 sub-sections, top, middle, bottom.

# Main Screen:

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/5c61be3a-959e-491c-a342-0c7b180a3c6f)



## 
## Main screen TOP section:
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/ad6842ea-2928-4fbc-b757-24f2f6a9eb5d)





## 
## Statistics
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/6440d44c-a965-471a-857c-a56d85220c8f)



From this section you will find a statistics read-out showing things like your device name, IP address, SSID name and signal strength, free space, and battery level and currently enabled display resolution. If you click on this it will update. It does not update the statistics in realtime.
## 
## About
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/d12e7d62-be91-47c3-b920-56801a2600a9)



Clicking on "About" will take you to a screen showing the current version number of the app, credits, and IF an update is avialable, an UPDATE button that will update the app (this will ONLY be shown if an update is available). NOTE: A check will be run to see if there is an available update whenever you click on ABOUT.
You will also find a link to this online help document if you click on "Help".

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/94199140-0010-49cf-8484-141de9e91589)



## 
## Font Size Adjustment
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/bf893290-3935-4216-a2a4-9d53092cb7c2)


Below "About" you will see "Font Size". If you click on this you will have the option to change the scale of the font for the application.

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/28c7cfe8-0be5-4eec-8d8d-4bace826429c)



## 
## Resolution Slider

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/21f02aee-d31d-4f88-aab5-6885019223f1)


"Resolution Slider" is a slider where you can slide the cross-hair to the left and right. Left REDUCES the resolution and right INCREASES the resolution. However you must click on "Set Resolution" to apply your resolution setting. The slider also has the options "AR 1:1.1" and "x32". The first is the aspect multiplier of the slider, for example, if the height was set to 1000, the width is set to 1100. You can change this "AR" by simply clicking on it, you will be prompted for a new multiplier factor, and it will change the mathematical product of the slider. Also there is the "x32" option. This is the factor by which the notch of the cross-hair is multiplied by. The cross-hair starts on the left at 32 and all the way on the right goes to 130. Changing the default "x32" to another number changes the multiplication factor of the notches. If you click on the resolution numbers up top (i.e. where it says 1440 x 1584 on this help page) you will be prompted to manually set your resolution width and height by direct input.
## 
## FFR Level
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/82963da4-45fb-4bd5-9ac1-551a5b0accf0)


"FFR Level" allows you to set the Fixed Foveated Rendering amount. For best performance set this to 4 and keep "dynamic" unchecked. This way FFR level 4 is forced always on. If you check "dynamic" it will only go up to 4 when required to maintain framerate.

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/98b50167-df30-4527-b652-04ec418b2875)

## 
## CPU Level

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/36d23c55-5ae6-43e8-811b-1d7b6d799750)


"CPU Level" allows you to change the CPU to a set clock level. Do this if you are confident you know what you are doing. Setting this to 5 will improve performance at the cost of battery life.

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/1dea2490-c777-49a6-a753-b0cf40ae8eb8)


## 
## GPU Level

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/bc184c15-e7ac-4ea3-b497-e43e29a1e1fe)


"GPU Level" allows you to change the GPU to a set clock level. Setting this to 5 will improve performance at the cost of battery life.

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/7448e905-2ca7-4a10-8ca0-841d980b6377)


## 
## Main screen MIDDLE section:

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/f0c3b17d-23dd-46de-afd8-cd967a35262b)


## 
 
### Display Frequency

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/9ce50bc5-2f93-475f-8fe8-3f39c231abf3)



"Display Frequency:" The options are 60hz, 72hz, 90hz, 120hz, Adaptive and Manual. Only the Quest 2 headset supports all 4 preset frequencies. The Quest 1 cannot go past 72hz. The Quest Pro cannot go past 90hz, nor can it do 60hz. The Quest 3 cannot do 60hz. Click on the frequency you want to set and it will be set if supported for your device. The Quest 3 supports adaptive refresh rates in incriments of 5hz whereas the Quest 2 does it in incriments of 1. I am not sure about the Quest Pro. You can use the OVR Metrics Tool overlay to see these changes in real time, which can be enabled from the Tools page.
##
 
### Default Display Settings
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/0b840ec1-2bb3-407e-b790-ef0c152f3ad8)


If you click on "Default Display Settings" any custom display settings you enabled will be cleared, thus setting the device back to default settings.
##
 
### Reset ALL settings to default 
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/9e8d6ca3-d1b3-4a37-9b1d-fb2cb3452d6e)


"Reset ALL settings to default" will clear any settings changes you made on the headset. (Actually this will clear ALL "oculus.debug" setprop settings). This will NOT remove any custom profiles nor will it erase any files on the device nor anything you saved to the device.
##
### Manage Game Profiles
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/af50682c-cf0c-4e40-adc6-cc2e631f03c5)


Manage Game Profiles allows you to load any saved profiles you have. Select from any of the 3 folders, **DefaultProfiles**, **RecordingProfiles**, or **GameProfiles**. It will read the selected profile and open a window showing the details of the profile. You then have the following options:
1. Delete - Deletes the saved profile.
2. Cancel - Closes this screen without doing anything else.
3. Delete Default - This will delete the default profile for the game. This option will ONLY be shown if a default profile exists for the selected game.
4. Set Default - This will set the currently shown profile as default for the selected game.
5. Run - This will run the game with the profile listed, BYPASSING any default profiles.

https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/3e8c52cf-aa3a-43dd-9769-2181ea11ec92

## 
### Save Game Profile 


![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/682bde0a-cb3a-45e7-bcfc-9c0039570116)

https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/bdc26a13-e98d-4103-b805-c9419da9661d 

"Save Game Profile" will save your custom display settings, (resolution, refresh rate, FFR amount, etc.) to a text file for whichever game you choose. You can also set these profiles to **AUTOMATICALLY** run by DEFAULT whenever you run the game you specify for it. When you click "Save Game Profile" you will be prompted to select the game you want to save the profile for. You will also then be prompted with a summary of the profile you are about to save.
In order to create a custom game profile, do the following:
1. Move the Resolution Slider to your desired game resolution and press Set Resolution.
2. If desired, set your Display Frequency, CPU Level, GPU Level and FFR Level.
3. Click on Save Game Profile.
   ![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/682bde0a-cb3a-45e7-bcfc-9c0039570116)

5. Select the game you want to save the profile for.
6. Make your selection of "Yes" (creates loadable non-default profile), "Make Kiosk App" (sets the game as the Kiosk App), "Set as Default" (saves the profile AND makes it the default profile to load when you launch the game), or "No", which cancels the action without saving the profile.

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/17908281-5af8-4ed8-af07-c266d71cc45e)

6. Run your game from the normal game selection menu and it will automatically load it's default profile if you saved one for it. Otherwise you can go to "Manage Game Profiles" on the Tools page and load different profiles you have saved for your games, you can have multiple profiles per game, and run ones from that menu without invoking the default profile being loaded. This is good for testing different profiles or just switching between different profiles for different reasons, like recording vs just gameplay.

## 

## Game Backup
"Game Backup" will open a menu to back up (or restore a backup of) the game of your choice. This will give you the option to backup the entire game, (i.e. APK, obb and data folders from /sdcard/Android/), or to just back up the data files (from /sdcard/Android/data/yourgame). This can only back up the data folders that are stored in "/sdcard/Android/" From this same menu you can RESTORE your game backups with the option to restore the ENTIRE game, (APK, OBB, Data files), or JUST the data folders. Again, this only applies to data folders in "/sdcard/Android/" All backups will be made in /sdcard/MCP/Backups/name-of-your-game. Along with the backup files there will be additional files, a Windows binary of adb and a bat file. This will allow you to restore your backups directly from a Windows PC without the need to copy the backup files back to your headset before restoring them. Just copy the backup folders to your Windows PC, then run the bat file for the game you wish to restore and select your restore options. It will restore your game directly from your PC. (**HINT**: If you use a file manager that has OTG support, such as File Manager +, you can move the backups from your headset to the OTG drive. If you want to restore them you must first copy them back onto the headset.) To get started, click on 

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/aa4f2015-dc1c-4430-ba46-61081127edae)


You will be presented with the following menu:
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/8f4372f5-1478-4f3f-bf4e-25d8f598bd42)

BACKUP OPTIONS: 

### Full Game Backup
 "Game + Data" (backs up the APK file of the game, plus any obb and data folders contained in /sdcard/Android) Please note, larger games will take longer to create backup files.
 
 https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/7ff9378e-28b5-4ad1-a2f0-d8604ed88d0a
 
 ### Game Data Backup Only
"Game Data Only" (backs up only the data folders for the game from /sdcard/Android). This will create a dummy APK file named "DATA ONLY APK" for selection during the restore option.
 
 https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/d11e2f6e-c2a0-41ef-9e7e-6ccfce484fcd
 
RESTORE OPTIONS:

 ### Full Game
Full Game (restores the game by installing the APK files and copying it's data and obb folders back to /sdcard/Android)
 
 https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/528e0edf-3bb5-4af6-9058-12851487430d
 
 ### Game ONLY
Game ONLY (Installs the APK file and copies any OBB folder back to /sdcard/Android)
 
 https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/b3f516e4-19a7-4690-b468-0714b90b5b65
 
 ### Game Data
Game Data (just copies the data folder back to /sdcard/Android). You can restore JUST the game data of any backups you have created, including from FULL backups.
 
 https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/6e0edf9a-8a69-452b-8f5f-2950f107efbd
##

## Main Screen Bottom Section

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/baa7a214-e924-441e-8b57-a6ba4f9a5fa2)

##


### User Defined Resolution Presets
Here you can create your own global resolution presets. This fisrt reads all of your device's display settings and then creates a profile with them. HOWEVER, it will NOT read the current device resolution that is set but rather it will read what the resolution SLIDER is set to and save THAT to the global preset. I might change this later on based on user feedback.
On the bottom you have three page options, [Recording,](#recording-screen), Misc, and Tools. Clicking either of those will take you to those pages.

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/d2ee82eb-faac-4761-85a1-136cde6d5b2a)




##
### Disable
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/8b5f6aad-174b-4be8-bb2f-a488bcbce0cc)


Clicking on Disable will disable The Ocular Migraine from monitoring app launches. This will prevent the gaming profiles from working. If you disable it, it will close the app. Just run The Ocular Migraine again and it will be re-enabled.
##
### Screen Navigation

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/2ab9bb2b-7ae5-44e7-8e65-b89fb7e4044f)

This is how you navigate between pages, or "Screens". Your options are "Main", "Recording", "Tools", and "Misc".
##
# Recording Screen:

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/25dc8074-ffeb-4627-a433-99fcb9af42e8)



##
### Recording Screen Top Section
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/c6f65489-134d-4086-aa92-0fd2c3fc55f0)


##
### Resolution Presets
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/1331f5de-dee2-4ce8-906d-143a8d3aabed)




On the top section of the Recording Screen you can set different recording resolutions. There are custom resolution presets and the option to set your own custom resolution. The presets are as follows:

1920x1080(16:9) - this is the Full HD resolution, pretty self explainitory.

3840x2160(16:9) - this is 4K resolution, only recommended for the Quest 3.

1280X720(16:9) - "HD" resolution.

3840X1080(32:9) - I created this preset thinking that the device would record both eyes in a 16:9 aspect ratio. However when telling the device to record both eyes, it records each eye in a 1 by 1 aspect ration. This seems not to be able to be changed. However you can still use this when recording in 3D if you want, but this does NOT set the device to record in 3D, it only sets the resolution, you will need to click on [Both(3D)] in the Middle Section under Recording Eye to record in 3D.

2560X720(32:9) - see notes from previous preset.

1080X1920(9:16) - makes a vertical recording resolution like for YouTube Shorts, tiktok, etc..

720X1280(9:16) - makes a vertical recording resolution like for YouTube Shorts, tiktok, etc..
##
### Custom Resolution
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/519c6c9c-9d87-4a5d-b29d-9e3d31cf0402)


Here you can enter in your own recording Width and Height.
##
### Recording Bitrate
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/eba6e46a-4c72-4fd5-a179-9c1af8a15b83)


Select this to set your recording bitrate.
##
### Recording Screen Middle Section
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/587c3b27-d24c-4d84-a0eb-b6301ac43549)


##
### Recording FrameRate
The following options are:
* 60fps
* 72fps
* 90fps
* 120fps
* Manual
* Hertz
  
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/e3e2d1f0-6189-4b1e-ad9f-43a70ba74973)



Please note that if you select a framerate to record that is above your display refresh rate, the display refresh rate will be raised to the framerate selected. If you select a recording framerate that is lower than your display refresh rate, the refresh rate will remain unchanged.
The Quest 1 probably cannot record any higher than 72fps.
The Quest Pro probably cannot record any higher than 90fps.
The Quest Pro and the Quest 3 even though they cannot do 60hz refresh rate are still able to record at 60fps.
The Quest 2 can record at all listed framerates.

Manual: Selecting this option will set your device to record at a custom framerate. This doesn't always work as intended so test this by making a test recording after setting it to verify.

Hertz: This sets the device to record at the framerate of the display frequency.

##
### Recording Eye
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/e292a61c-3083-441e-94c6-816e5cce0dbc)


The following options are:
* Left Eye - Records from the left eye.
* Both(3D) - Records BOTH eyes, for 3D.
* Right Eye - Records from the right eye.
##

### Start Recording and Stop Recording
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/29900e85-3bca-41dc-b948-aac9041d9051)
These options do NOT appear on the Quest 2 as currently it does NOT support this method of recording. I don't know if this works on the Quest Pro or not. Let me know!
This uses a different method of recording than the normal user activated recording method. On the Quest 3, it records in stereo. On the Quest 1 it records in mono. This uses "metacam" for recording, a built-in method that is used by the Meta Quest Developer Hub.
This method is useful if you want to record in stereo on your Quest 3 (again not sure if this works on the Quest Pro yet, waiting for user feedback). This method does record on the Quest 1 but it's not in stereo.
If you start recording using this method, you must also STOP recording using the STOP RECORDING button, otherwise the recording will continue.
##

### Recording Screen Bottom Section
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/6ea7c9ea-e674-4acf-a6a2-a135702e6b81)



##

### FOV Crop
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/4da04a65-3f07-48a1-aacf-8867beead84b)


This seems to be a little known feature that allows you to crop the rendered areas of your screen. This concentrats whatever your set resolution is into this cropped area, thus making the image much clearer. This is beneficial for gameplay recordings, it improves the visual quality of them greatly. Here are the following options:
* Up - crops the top part of the render area.
* Down - crops the bottom part of the render area.
* Outward - crops the outward edges of the render area, the edges of the screen that are away from your nose for each eye.
* Inward - crops the inward edges of the render area, the edges of the screen that are toward your nose for each eye.
* Remove Crop - removes any crop you have set.
* Optimal Crop - enables a preset crop that should correctly match up with the rendering area for recording.
##
### Save Recording Profile
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/cfc3c93c-ceb3-4641-8d0d-9bde33292028)


Saving a Recording Profile creates a recording profile that stores all of your current disiplay information, such as resolution, GPU/CPU levels, FFR level, Refresh Rate and also your recording settings such as recording bitrate, recording eye, recording resolution, screen crop and saves it to a recording profile which you can load for the game you have selected or even load it for use with any game. You can even save it as a default profile using the Manage Game Profiles option on the Main Screen. In order to create a Recording Profile, just set whatever resolution you want from the Main Screen (if you want anything other than the default device resolution), along with any FFR Level, CPU Level and GPU Level selections, set the recording resolution and framerate and bitrate and eye recording selection then click on Save Recording Profile. It will propmt you to select which game you wish to save it for, but this does NOT make it a default profile for that game. The game selected will still be run with it's default profile unless you load it's recording profile from the Load Recording Profile screen and select RUN.

https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/52f6b17d-b7ce-4039-9c19-b74b02ce06a4
##
### Load Recording Profile
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/0db28724-95c9-4238-a286-568975627c8b)


Clicking on Load Recording Profile you will be able to load any saved recording profiles. After selecting your recording profile you are presented with the following options:
* Load Only - This will load the settings in the selected Recording Profile onto the headset.
* Run - This will engage the settings from the Recording Profile and run the game it was saved for.
* Delete - This will delete the selected Recording Profile.
* Cancel - This will cancel the operation.
  
https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/34e7da94-53b9-49a1-9664-1e49b497e103

##
### Inject 3D Metadata
This is used to inject 3D metadata into the videos you've recorded after selecting "Both(3D)" for eye recording, for upload to YouTube. This will allow your video to be played back in 3D from YouTube in YouTube VR for sharing with friends.
1. Click on Inject 3D Metadata

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/a1af21af-ec10-49b0-af5c-b0c5f2aeff87)


2. You will be prompted to select your video file:

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/841fe1bc-e09f-4e07-9f92-c2bdf694276f)

3. You will be propmted to CONFIRM your video file in a different window showing the entire listing with full names: 
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/ec243a43-cfa5-4c06-a9cf-0628dd3a6078)
4. You will be prompted to set the Audio Offset. This is in case your audio is out of sync. You can play with this to try and fix that. This will shift the audio forward or backward depending on your input. Positive values makes the audio delayed by that amount and negative values plays the audio earlier by that amount.
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/37800374-0825-4ed9-81f9-fcef2a64df41)

5. You will be prompted to set the Audio Tempo. This is useful for when your audio is not just out of sync but because gradually out of sync over time. This will stretch your audio to play slower/longer or faster/shorter based on your input here. A value of 1.0 keeps the audio rate untouched. A value of 1.5 makes the audio play faster, at a rate of 1.5x. A value of 0.5 makes the audio play slower, at half speed.
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/4c1623c3-2932-40aa-8fd6-f143a66de7f9)
6. You will be prompted to set a start time. If you leave this unchanged, it will not trim the beginning of your video.
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/b6ce75a1-7be2-4413-b167-931893925e92)
7. You will then be prompted to set a Trim End Point. The default is set to 9 hours so if you don't touch this the end of your video will remain trimmed since there's not gonna be any recordings this long.
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/b928f648-31a1-412a-9171-39138c6c7116)

8. You will be prompted to accept or change the aspect ratio if needed. This should NEVER be needed unless the Quest 3 no longer records 3D in a 1:1 aspect ratio. So just click on the green arrow to accept. 
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/a95369be-cdf1-4896-9682-546fd02a8cd8)

9. You will be shown the ffmpeg command about to be run. You can modify this commend from here before pressing OK, if you know what you're doing. Otherwise don't touch this: 
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/c034fe4a-31c2-4486-9496-ac01f1fe0b7c)
10. You will then be shown a summary of the options you have selected before continuing to proceed with processing your video file.
11. Wait while your video file is being processed. This might take a bit depending on your file size and length. The audio will be recompressed, but the video is not being recompressed.
12. After it is finished it will show you the command output results: 
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/07acbad9-e925-4cc3-9d23-cf749fdfafb7)
13. Your video file is now ready to be uploaded to YouTube for 3D processing. You will find it in /Oculus/VideoShots/3D.
##
### Process 2D Video


![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/203253ef-f49e-4b98-b3a0-630ac401f993)


This option does the EXACT SAME THING as the INJECT 3D METADATA option except that it does NOT inject 3D metadata. It does all the other options however, such as set the audio offset, tempo, start and end trim points.
##
### adaclocks
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/4e30978d-b9d5-4f63-96f3-7fb87e350a89)

This option enables or disables adaclocks. This seems to have something to do with audio clocks and maybe affect recording sycn one way or another. Sometimes it seems to help, other times it seems to make no difference.
This feature seems to be the Adaptive Clocking feature, which scales the performance of the system based on need. Setting this to 0 disables this.


### Swap Interval

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/d219c57b-e7f1-4407-8b8f-2c2bdb7c0f1a)

The Swap Interval settings is a bit hard to explain. [THIS PAGE](https://github.com/MortimerGoro/ovr-mobile-sys/blob/master/VrApi/Include/VrApi.h) seems to explain it in a very technical manner, under "Frame Timing". In practice this is what it seems to do, if your refresh rate is 90hz and you have the Swap Interval set to 1, when you record the framerate will be 90fps. However if you set the Swap Interval to 2, it will halve the recorded framerate. This is automatically set to "1" in my framerate recording presets.
##
### Reset Recording to default
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/284fe4f4-3088-4233-86be-06df1b6dd945)

Resets all recording options back to system defaults.

##
# Tools Screen:

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/08f4257f-0452-4081-987c-f0e3c73799e6)

##

# Tools Screen Top Section

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/85f9db54-883b-4535-955a-d53bf5218d48)

##
### Install APK via ADB

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/c56a08e2-052e-426a-babb-1822d175657c)


Clicking on this will prompt you to select an APK to install. It will then be installed via the internal adb binary.
##
### Input ADB command

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/8946a9f7-31c8-4817-b7a9-869c6cbd2919)


For anyone who wants to play with the internal ADB binary.
##
### ADB Shell command

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/9412247f-3143-4b16-99cc-655bba6b702a)

Runs a command after "ADB shell".
##
### Console Output Screen

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/c15d207a-c788-4c4c-b67e-02b5d205fe85)

This is where you will see the output of "ADB command", "Shell command", and "ADB Shell Command" options.
##


# Tools Screen Middle Section

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/aeded760-e197-476d-aba2-4f10a1b886be)
##
### Enable OVR Metrics Tool Overlay

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/bff210dc-5ebd-4c63-9fff-e54f81ac40d2)

This will cause the OVR Metrics Tool to display an overlay consisting of statistics to monitor the performance of your game. This is useful when testing out new gaming profiles. If the OVR Metrics Tool is not installed, this will install it for you automatically.
##
### File Manager

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/99153a63-09d4-404a-be7a-212fc482c070)


This will open File Manager +. If it is not installed, it will download it and install it then open it.
##
### SideQuest

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/2f0a9484-cef3-41f4-843b-3673722d5e55)


This will open the Android version of SideQuest. If it is not installed, it will download it and install it.
##
### Set Kiosk Mode App

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/3658cd7c-e9b0-4de6-a3b0-88130f38bd5d)

This will prompt you to set up Kiosk mode.
This is how Kiosk Mode works:
1. Prompted to select your app for Kiosk Mode.
2. Prompted to create a password.
3. When you are running your Kiosk mode app, hold the volume up for a few seconds until you are prompted to enter the Kiosk Mode password.
4. Kiosk mode will be enabled if you entered the password correctly.
5. In order to get out of Kiosk Mode you must restart your headset and open The Ocular Migraine and input the correct Kiosk Mode password to disable it.
6. If you enter the wrong password at this point, the Kiosk Mode app will launch again and you will need to reboot your headset to try again to re-enter it.
7. The only time you do NOT need to reboot your headset is in cases where the application you are running has an "EXIT" button allowing you to quit the application.
8. Kiosk Mode effectively "disables" the Oculus / Meta home button on the right controller. You can still however hold it down to recenter yourself.

##
### Un-set Kiosk Mode

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/1793ee1d-1fba-4492-af3b-58ed3fcadd96)

This will prompt you for the Kiosk Mode password and then it will entirely disable Kiosk Mode. This is here so that pressing the Volume Up button for an extended amount of time no longer triggers the Kiosk Mode enable password prompt.
##

### Create Shortcut App

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/40a991d1-031b-4dbb-affa-101d8a051a88)

The Create Shortcut App feature allows you to redirect one app to another. This is useful especially for apps that are in the UNKNOWN SOURCES menu. You can substitute an offical app for one that's in your UNKNOWN SOURCES in which case you don't have to go to the UNKNOWN SOURCES menu. Official apps are able to be pinned to the bottom menu, making it even more convienent to launch an UNKNOWN SOURCES app directly from the main menu! In the video example below, I create a shortcut for the app **"File Manager +"** that's in UNKNOWN SOURCES using an official app, which allows me to launch **"File Manager +"** simply by launching the official app I set as it's shortcut. Now obviously you cannot run the app you are using as the shortcut while this is in effect. To remove this shortcut just use the Manage Saved Profile feature and find the saved profile in the Default Profiles folder, load it and select DELETE, then you will be able to run the original program again. I recommend using this with apps you have no interest in running. I personally use this to launch this exact app, The Ocular Migraine. I have set the ESPN app as the shortcut. When I click on it, it runs The Ocular Migraine instead.

https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/ef3d2702-df86-4937-af4b-5b7ed06d4f81
##
### Create Startup App

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/9cab6f4b-e83c-4a6d-95ac-e335497347c6)

This allows you to set an application to launch upon start up. Useful for an alternate launcher for example.
##

### Disable Startup App

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/c8ad61da-a7b4-490a-ac30-f7e2340e2787)

Disables the auto startup of the previously selected application.
##
# Tools Screen Bottom Section

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/fb215d8a-03f0-4874-ba46-bf9c2e2033f7)

##
## Access Lists
Here you can create access lists.
NOTE: If you enable the white list, the black list is disabled. If you enable the black list, the white list gets disabled.

### Create White List

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/33c945cf-b8d1-4fa4-82b5-5e7b1b5fb2a1)

This will prompt you to select applications to be white-listed. After which if you try to launch any other application other than those on the white list, they will be immediately shut down.

### Create Black List

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/bef1cd10-e871-42ef-b9cc-43f1b683f491)

This will prompt you to select applications to be black-listed. If you try to run any application on the black list it will be immediately shut down. You can alternatively use the built in "lock" function for applications that Meta has now enabled in the menu for each app.
##

### Disable Access Lists

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/2eba98f5-37da-4473-8d05-9d5bf00e61f4)

This disables the access lists without deleting them. The purpose of this is so that when you create the list again, it will reload your previously created list with your previously select applications to which you can add or remove applications from that list. It's useful if you just want to add or remove another application or two and not have to create your list all over from scratch.
##
### Delete Access Lists

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/80eb2131-1eb4-43cc-b709-75646baa627a)

This will actually DELETE the access lists files, both white list and black list. This is useful if you want to create another list from scratch without having anything from before selected.

##
### Access List Enforcement Method

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/24940b54-4302-4068-b67f-1b83a586d60e)

Switches between two different modes of enforcing the access lists. Depending on what Meta will do with it's firmware in the future, certain features might break so I tried a couple of different methods. If you find one doesn't work, try switching to the other.

##



# Misc Screen:

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/59514696-a46c-4cb6-844d-7f8e9f8e33c4)


##

### Misc Screen Top Section
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/841646db-849e-4c89-a797-ea16ee9fb781)


##
### Switch App Launch Detection Method

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/5bbf70e3-0331-4912-8d48-eb6d3c7bf360)

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/f09ec6c9-e591-4603-8cda-5f281c256aa3)




Clicking on this will toggle between two different app launch detection methods. The default WAS Logcat. Currently the default is set to App Usage.
App Usage is pretty fool proof overall but is slightly slower than the Logcat method. The Logcat method is very fast but doesn't detect already running apps being brought to the foreground as clicking on them, whereas App Usage does detect this. However this issue only applies to 2D apps, not VR 3D applications.
##
### Disable Battery Optimization

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/d6302893-2400-4faa-ae3f-454c0bf2e0b7)

This is required to prevent the Quest from killing The Ocular Migraine when running in the background which is required for it to detect when apps are launched so that it can enable the resolution presets for that app. Also for the Kiosk mode and access lists to work.

https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/ae12b7ab-07ae-4a4a-9a7c-4ef3bfac6f79
##

### Enable All File Access

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/d4037ac8-7a53-4863-b4f6-06dc54debbdd)

The purpose of granting this special permission to The Ocular Migraine is so that it can access OTG storage for the purpose of restoring any backups you might have copied to a thumb drive. Yes, you can connect a thumb drive to your Quest via an OTG cable and copy game backups onto it using a file manager that supports OTG storage, such as "File Manager +" which you can install using the menu on The Ocular Migraine. To enable this option, click on "Android Settings", then "Apps", then "Special app access", then "All files access", then scroll to find The Ocular Migraine from the list of apps. Click on it to select it, then click on the toggle "Allow access to manage all files".

https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/e84dc6d6-f2e3-413b-92a1-91ef5048ba88
##
### Disable Notifications

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/0a18f7ff-a6ff-443a-bf00-e7c91e678733)

This is NOT a requirement but a recommendation. If you want to do it, this is how:

https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/ad4c4d3f-7f98-416a-8ea7-db4c07d522cc
##
### Android Settings
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/ac8cce95-ead9-4edd-9e42-622d46910019)

This opens the general Android Settings of your Quest. Be careful with this. I put this in here just for fun for those who want to poke around, but again, be careful with this. Not all settings are documented or necessarily work as expected here.
##

### User Defined ADB Commands
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/2601116f-ec85-4aa8-9dee-db75efd8a83c)

Long press to ender an adb shell command you wish to save. This will create a script text file that will be run each time you click on it. The script is stored in /sdcard/MCP/Scripts/. You can manually modify each script if you would like it to run multiple commands, just put a semicolon between the commands, for example "echo this is a test;echo test completed". Those are two commands on a single line. If you put multiple lines in the script, it probably will not run correctly. 

##


### Misc Screen Middle Section
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/ac2e70fa-7274-41e2-9568-2ebef079ed00)

##

### Web Server File Sharing and Remote Uploading

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/2389b27d-af04-4b1d-8d08-5bb1deee13ee)


Here you can configure the web server of your Quest. The top option allows you to turn web server file sharing on and off using "Toggle Server". 
"Set Server Directory" allows you to specify which directory you would like to share.
Once the web server is enabled you will see the web server URL in green along with the shared folder in green. So in the screen shot above on my phone or computer I would go to http://192.168.1.248:1987 which would then show me all my files in the shared directory which in this example is /storage/emulated/0, which is the root of the sdcard partition. You will then be able to access the files and subfolders here.

"Toggle Remote Uploading" is useful to allow you to upload files to your Quest from your phone or computer. When enabled it will show you the web address to go to for uploading. In the example above the address I could go to on my phone or computer would be http://192.168.1.248:1987/upload. This will bring me to a webpage that will allow me to select a file from my device and upload it to the Quest. It will ALSO allow me to specify a directory to upload it to. If the directory does not exist, it will be created. If a directory is not specified, it will be uploaded to "/sdcard/Uploaded" by default.

Currently this seems to work well on the Quest 2, but on the Quest 3 it seems that when it goes to sleep, the web server becomes unresponsive. Sometimes when it's plugged into USB-C it stays responsive to YMMV on the Quest 3. HOWEVER, when downloading a very large video file on the Qeust 3 it will finish the download, it will not cut it off.

##

### Misc Screen Bottom Section
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/56cfca18-9356-4e44-bcac-58aeaf3351c6)

##
### Restart Home Environment

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/2c931077-c858-4346-b7cc-d68e62ea7dc2)


Clicking this will restart your home environment. This is for the purpose of applying resolution changes to it. If you want to change the resolution in your home environment, you must select this option after making the settings changes on the Main Screen.
##
### Check Enabled Profiles

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/72a082f3-1b8c-43fe-a30d-7300926719c8)

This is mainly for troubleshooting. I will probably remove this button or make it able to be toggled on by a "debug" option.
##
### Devices
This is also good for troubleshooting. It runs the "adb devices" command and then shows the output. I also may only make this show up in a debug mode.

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/ac2dae1c-fbf2-4212-ac3b-c68886af0fde)

##
### Restart ADB Server
Restarts the ADB server on the device, for troubleshooting.

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/1cc55ea1-ac5a-43ae-b81f-3e38af5f4fc0)

##
### Reboot
This will INSTANTLY reboot the headset. Instantly.

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/c5e7b5f2-e4c4-47d7-b344-23bd82bcdbda)

##
### Current Settings
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/0688834b-3424-44a7-9053-404c321a2f27)

This will query the headset for all it's "oculus.debug" set flags and display them.
##
### Load System Defaults
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/bad8b228-873c-45b6-8fcd-8631354d3774)

This will clear ALL "oculus.debug" flags. Usually this sets the headset back to "default" however some firmwares have some of these flags already set to certain specific settings for some reason. This will clear all of that. Just reboot your headset to get it back.
##
### Save Settings to file
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/b5b3342b-1e3d-4e53-a922-9ab1c5e12ef8)

This is a VERY cool feature. This reads all of the "oculus.debug" flags that are currently set and saves them to a text file which you are prompted to name. This is to be used with the next option...
##
### Load Settings from file
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/eed9a7ce-1040-4fbb-9a20-d9df2e702662)

You can use this feature to load settings onto the headset that you saved from the last option. This is useful to test a different array of settings. This is kind of like saving a profile but these are not able to be automatically loaded. You have to load these manually. This is gererally for testing or if you have some things on your headset working exactly as you like but aren't sure which settings you changed to get there, the Save Settings to file and Load Settings from file is a great way to save the overall settings.
##


### Delete BlazeRush Config

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/a66c146b-9503-4d8a-a337-510b4e8230b6)

"Delete BlazeRush config" will delete the config settings file for the game "BlazeRush". This is required if you want to run that game at a different resolution. This is because upon first run BlazeRush will get the device resolution and create a config file telling the game to run at that resolution. Once this config file is created, it will no longer look to see if the device has a different display resolution than what is stored in the config file. Therefore, if you want to run BlazeRush at a different resolution you MUST first delete the config file so that it will create a new config file based on the resolution you have set the device to.
##

### Apps I Worked On

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/20fda1a4-6d29-49e4-8486-b6913bfe1aa9)

This opens a page with links to other applications I've worked on.
##





