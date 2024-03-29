# The Ocular Migraine: {Dev Mode} Master Control Program.

### This is an applicaiton for use with the Oculus / Meta Quest mobile VR headsets, including the original Oculus Quest, Oculus / Meta Quest 2, Meta Quest Pro, Meta Quest 3.

# Table Of Contents:

- ## [Installing](#installation)


* # [The Main Screen](#main-screen)
  * ## [Top Section](#main-screen-top-section)
    * [Statistics Readout](#statistics)
    * [Font Size Adjustment](#font-size-adjustment)
    * [About](#about)
    * [Resolution Slider](#resolution-slider)
    * [Fixed Foveated Rendering (FFR)](#ffr-level)
    * [CPU Level](#cpu-level)
    * [GPU Level](#gpu-level)
    * [All Levels](#all-levels)
  * ## [Middle Section](#main-screen-middle-section)
    * [Display Frequency](#display-frequency)
    * [Default Display Settings](#default-display-settings)
    * [Reset These Settings To Default](#reset-these-settings-to-default)
    * [Reset ALL settings to default](#reset-all-settings-to-default)
    * [Delete BlazeRush config](#delete-blazerush-config)
    * [Save Game Profile](#save-game-profile)
    * [Run Game](#run-game)
    * [Manage Game Profiles](#manage-game-profiles)
    * [Create Shortcut App](#create-shortcut-app)
    * ### [Game Backup Menu](#game-backup)
      * Backup Options
        * [Game + Data (Full Game Backup)](#full-game-backup)
        * [Game Data Only](#game-data-backup-only)
      * Restore Options
        * [Full Game](#full-game)
        * [Game ONLY](#game-only)
        * [Game Data](#game-data)
  * ## [Bottom Section](#main-screen-bottom-section)
* # [The Recording Screen](#recording-screen)
  * ## [Top Section](#recording-screen-top-section)
    * [Resolution Presets](#resolution-presets)
    * [Custom Resolution](#custom-resolution)
  * ## [Middle Section](#recording-screen-middle-section)
    * [Recording FrameRate](#recording-framerate)
    * [Recording Eye](#recording-eye)
  * ## [Bottom Section](#recording-screen-bottom-section)
    * [Recording Bitrate](#recording-bitrate)
    * [FOV Crop](#fov-crop)
    * [Save Recording Profile](#save-recording-profile)
    * [Load Recording Profile](#load-recording-profile)
    * [Inject 3D Metadata](#inject-3d-metadata)
    * [Swap Interval](#swap-interval)
* # [The Tools Screen](#tools-screen)
* # [The Misc Screen](#misc-screen)
  * ## [Top Section](#misc-screen-top-section)
    * [Switch App Launch Detection Method](#switch-app-launch-detection-method)
    * [Disable Battery Optimization](#disable-battery-optimization)
    * [Enable All File Access](#enable-all-file-access)
    * [Disable Notifications](#disable-notifications)
  * ## [Bottom Section](#misc-screen-bottom-section)
    * [Restart the Home Environment](#restart-home-environment)
    * [Check Enabled Profiles](#check-enabled-profiles)
    * [Devices](#devices)
    * [Restart ADB Server](#restart-adb-server)
    * [Reboot](#reboot)
    * [Dynamic Clock](#dynamic-clock)



##
[Dynamic Clock](#dynamic-clock)
[The Main Screen (About)](#about)
[The Main Screen (About)](#about)
[The Main Screen (About)](#about)





## Installation


1. Make sure your device is in developer mode. If it isn't, watch this 60 second video here which shows you how: https://youtu.be/jB1gwgSpU3E

2. Download the zip file ["Install.zip"](https://github.com/petermg/TheOcularMigraineMCP/releases/download/v1.0/Install.zip) and extract it to any folder on your computer.
 
 ![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/248e2c89-a0fa-4906-b4dd-612938073e33)

3. Download the latest version of The Oculus Migraine apk file from the latest releses [here.](https://github.com/petermg/TheOcularMigraineMCP/releases)

4. Take the APK you downloaded and drag and DROP it onto the bat file named "Installation.bat" from the zip file "Install.zip" that you extracted earlier and follow the onscreen prompts. DO NOT CLOSE THE BAT FILE WINDOW after the file has been installed! Press any key to continue as it then runs the command "adb tcpip 5555" which opens up the port on the Quest for this application to authenticate itself on the very first run. This is the one and **ONLY** time your PC will be required for this!

5. Put on your headset.

6. Go to UNKNOWN SOURCES.

7. Click on "The Ocular Migraine".

8. After it begins to load, you will be prompted a total of 3 different times with a prompt that says "Allow USB debugging?". Each time you must select the option at the bottom which says "Always allow from this computer". After you select this option the first time, the applicaiton will close. Launch it again by clicking on it from UNKNOWN SOURCES and you will be propmted 2 more times to "Allow USB debugging?" Again select "Always allow from this computer".

9. Now once the app is up and running, select "MISC" from the bottom and it will take you to the MISC page.

10. Select "Battery Optimization Settings" to open the Battery optimization settings.

11. Make sure "The Ocular Migraine" is set to "NOT OPTIMIZED". By default soon after this application is installed, the Quest will "optimize" it, which ends up KILLING the app from running in the background. This prevents the app from being able to initiate custom gaming profiles. If you do not see The Ocular Migraine listed under "NOT OPTIMIZED", click on the drop down menu showing "NOT OPTIMZED" and select "ALL APPS". Find The Ocular Migrine and click on it and select "Dopn't optimized" then click DONE. If you have already found The Ocular Migraine set as NOT OPTIMIZED without changing anything, chances are the Quest will end up "optimizing" it later. So you may want to revisit these settings later on to change it back. I have found once I change it back manually, the Quest honors the user selection.

12. Next select "Notification Settings" from the MISC page.

13. Find The Ocular Migraine, if it's not already showing, you can select ALL APPS from the dropdown menu. Click on the toggle to DISABLE notificaitons for The Ocular Migraine. This is NOT required but recommended.

### NOTE: From now on, after each reboot of your device, the **FIRST** time you launch The Ocular Migraine, it will prompt you to "Allow USB debugging?". Select "Always allow from this computer" each time. This only happens on the initial launch of the applicaiton after a reboot of your device. It will not ask this question again until the next device reboot on it's inital launch.

Each screen has 3 sub-sections, top, middle, bottom.

# Main Screen:

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/50953447-0d97-4da5-80ae-1534ed3ee19e)


## 
## Main screen TOP section:
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/b4078f82-86f8-4325-93cd-4217b2d3323e)




## 
## Statistics
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/6440d44c-a965-471a-857c-a56d85220c8f)



From this section you will find a statistics read-out showing things like your device name, IP address, SSID name and signal strength, free space, and battery level and currently enabled display resolution. If you click on this it will update.
## 
## About
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/d12e7d62-be91-47c3-b920-56801a2600a9)



Clicking on "About" will take you to a screen showing the current version number of the app, credits, and an UPDATE button that will update the app. Currently it does not have version checking enabled so it just downloads the latest apk and installs it, regardless of if it's newer or not. Version checking implimentation is on the TO-DO list. You will also find a link to this online help document if you click on "Help! How do I use this thing?!".

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/4c22f64c-4d92-416a-86b2-9cfd2a3669f5)


## 
## Font Size Adjustment
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/bf893290-3935-4216-a2a4-9d53092cb7c2)


Below "About" you will see "Font Size". If you click on this you will have the option to change the scale of the font for the application.

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/d05daafa-0d83-4cf5-bb09-6f3ec71ff7d2)


## 
## Resolution Slider

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/21f02aee-d31d-4f88-aab5-6885019223f1)


"Resolution Slider" is a slider where you can slide the cross-hair to the left and right. Left REDUCES the resolution and right INCREASES the resolution. However you must click on "Set Resolution" to apply your resolution setting. The slider also has the options "AR 1:1.1" and "x32". The first is the aspect multiplier of the slider, for example, if the height was set to 1000, the width is set to 1100. You can change this "AR" by simply clicking on it and it will change the mathematical function of the slider. Also there is the "x32" option. This is the number by which the notch of the cross-hair is multiplied by. The cross-hair starts on the left at 32 and all the way on the right goes to 130. Changing the default "x32" to another number changes what each notch on the slider is multiplied by.
## 
## FFR Level
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/82963da4-45fb-4bd5-9ac1-551a5b0accf0)


"FFR Level" allows you to set the Fixed Foveated Rendering amount. For best performance set this to 4 and keep "dynamic" enabled.

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/98b50167-df30-4527-b652-04ec418b2875)

## 
## CPU Level

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/36d23c55-5ae6-43e8-811b-1d7b6d799750)


"CPU Level" allows you to change the CPU to a set clock level. This is NOT recommended however as the device is set to dynamically do this. Setting this will result in more battery useage and more heat. This will NOT "unlock" any performance as the headset is DESIGNED to automatically scale the CPU up when needed to it's maximum clock rate.

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/db2d14e3-0fe8-4958-b537-38b442c435c9)

## 
## GPU Level

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/bc184c15-e7ac-4ea3-b497-e43e29a1e1fe)


"GPU Level" allows you to change the GPU to a set clock level. This is NOT recommended however as the device is set to dynamically do this. Setting this will result in more battery useage and more heat. This will NOT "unlock" any performance as the headset is DESIGNED to automatically scale the GPU up when needed to it's maximum clock rate.

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/6cbab271-627e-4efc-bccb-328ab83fb20f)

## 
## Main screen MIDDLE section:

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/48a74bea-f620-4d90-90f4-4eaae07806b1)

## 
 
### Display Frequency

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/db2f6214-b298-4e8b-9e51-45ff436df0c6)


"Display Frequency:" The options are 60hz, 72hz, 90hz, 120hz. Only the Quest 2 headset supports all 4 frequencies. The Quest 1 cannot go past 72hz. The Quest Pro cannot go past 90hz, nor can it do 60hz. The Quest 3 cannot do 60hz. Click on the frequency you want to set and it will be set if supported for your device.
##
 
### Default Display Settings
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/0b840ec1-2bb3-407e-b790-ef0c152f3ad8)


If you click on "Default Display Settings" any custom display settings you enabled will be cleared, thus setting the device back to default settings.
##
 
### Reset ALL settings to default 
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/9e8d6ca3-d1b3-4a37-9b1d-fb2cb3452d6e)


"Reset ALL settings to default" will clear any settings changes you made on the headset. This will NOT remove any custom profiles nor will it erase any files on the device nor anything you saved to the device. It only clears any "setprop" commands that were sent to the headset, thus restoring the default settings.
##
### Manage Game Profiles
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/af50682c-cf0c-4e40-adc6-cc2e631f03c5)


Manage Game Profiles allows you to load any saved profiles you have. Select from any of the 3 folders, **DefaultProfiles**, **RecordingProfiles**, or **GameProfiles**. It will read the selected profile and open a window showing the details of the profile. You then have the following options:
1. Delete - Deletes the saved profile.
2. Cancel - Closes this screen without doing anything else.
3. Delete Default - This will delete the default profile for the game.
4. Set Default - This will set the currently shown profile as default for the selected game.
5. Run - This will run the game with the profile listed, BYPASSING any default profiles.

https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/40e12818-ce48-4621-afd6-12e6479f64d0

## 
### Save Game Profile 

https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/3c85d9f7-503c-44a0-b0c2-ac10f90198a5

"Save Game Profile" will save your custom display settings, (resolution, refresh rate, FFR amount, etc.) to a text file for whichever game you choose. You can also set these profiles to **AUTOMATICALLY** run by DEFAULT whenever you run the game you specify for it. When you click "Save Game Profile" you will be prompted to select the game you want to save the profile for. You will also then be prompted with a summary of the profile you are about to save.
In order to create a custom game profile, do the following:
1. Move the Resolution Slider to your desired game resolution.
2. Press Set Resolution.
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
 "Game + Data" (backs up the APK file of the game, plus any obb and data folders contained in /sdcard/Android)
 
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
Currently some of what's on this section is up in the air right now. I originally had this as multiple global resolution presets you could set. This was a feature from very early development and I may get rid of it and just clean up this page a bit with the added space. Not sure yet. What do you think? On the bottom you have three page options, [Recording,](#recording-screen), Misc, and Tools. Clicking either of those will take you to those pages.
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/03f1f3ff-d546-4d08-99a5-480f3af4bb23)



##
### Disable
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/8b5f6aad-174b-4be8-bb2f-a488bcbce0cc)


Clicking on Disable will disable The Ocular Migraine from monitoring app launches. This will prevent the gaming profiles from working. If you disable it, it will close the app. Just run The Ocular Migraine again and it will be re-enabled.
##


# Recording Screen:

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/2a2c53a6-ac1c-41be-8cf5-4deca609c35f)


##
### Recording Screen Top Section
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/6e43d036-14f3-4f5b-af92-4285e624c863)

##
### Resolution Presets
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/6f5722eb-c637-4541-aa49-a26a3e4bcf55)



On the top section of the Recording Screen you can set different recording resolutions. There are custom resolution presets and the option to set your own custom resolution. The presets are as follows:

1920x1080(16:9) - this is the Full HD resolution, pretty self explainitory.

3840x2160(16:9) - this is 4K resolution, only recommended for the Quest 3.

1280X720(16:9) - "HD" resolution.

3840X1080(32:9) - I created this preset thinking that the device would record both eyes in a 16:9 aspect ratio. However when telling the device to record both eyes, it records each eye in a 1 by 1 aspect ration. This seems not to be able to be changed. However you can still use this when recording in 3D if you want, but this does NOT set the device to record in 3D, it only sets the resolution, you will need to click on [Both(3D)] in the Middle Section under Recording Eye to record in 3D.

2560X720(32:9) - see notes from previous preset.

1080X1920(9:16) - makes a vertical recording like for YouTube Shorts, tiktok, etc..

720X1280(9:16) - makes a vertical recording like for YouTube Shorts, tiktok, etc..
##
### Custom Resolution
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/519c6c9c-9d87-4a5d-b29d-9e3d31cf0402)


Here you can enter in your own recording Width and Height.
##
### Recording Screen Middle Section
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/e12df625-316a-4c10-9f8b-e9d751ec653c)

##
### Recording FrameRate
The following options are:
* 60hz/fps
* 60fps@120hz
* 72hz/fps
* 90hz/fps
* 120hz/fps

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/a01fe4ac-ccd4-4580-b24a-4ec61e3dde95)


Please note, the Quest 1 cannot go above 72hz, the Quest Pro can only do 72hz and 90hz, and the Quest 3 can not do 60hz. Only the Quest 2 can do all 4 options. Also the 60fps@120hz option is NOT recommended as it makes your experience jerky, even though the recording may look fine. This was more of an exeprimental feature to get the Quest Pro and Quest 3 to record at 60fps.
##
### Recording Eye
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/e292a61c-3083-441e-94c6-816e5cce0dbc)


The following options are:
* Left Eye - Records from the left eye.
* Both(3D) - Records BOTH eyes, for 3D.
* Right Eye - Records from the right eye.
##
### Recording Screen Bottom Section
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/8038ccbf-3504-49e4-bcde-dc330ba510ed)


##
### Recording Bitrate
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/eba6e46a-4c72-4fd5-a179-9c1af8a15b83)


Select this to set your recording bitrate. I have made the default selection 45Mbps.
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


Saving a Recording Profile creates a recording profile that stores all of your current disiplay information, such as resolution, GPU/CPU levels, FFR level, Refresh Rate and also your recording settings such as recording bitrate, recording eye, recording resolution, screen crop and saves it to a recording profile which you can load for the game you have selected or even load it for use with any game. You can even save it as a default profile using the Manage Default Profiles option on the Tools Screen. In order to create a Recording Profile, just set whatever resolution you want from the Main Screen, set the recording resolution and framerate and bitrate and eye recording selection then click on Save Recording Profile. It will propmt you to select which game you wish to save it for, but this does NOT make it a default profile for that game. The game selected will still be run with it's default profile unless you load it's recording profile from the Load Recording Profile screen and select RUN.

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
4. You will be prompted to accept or change the aspect ratio if needed. This should NEVER be needed unless the Quest 3 no longer records 3D in a 1:1 aspect ratio. So just click on the green arrow to accept. 
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/556c58d6-a643-4ccc-971c-c08583ee8b6a)
5. You will be shown the ffmpeg command about to be run. You can modify this commend from here before pressing OK, if you know what you're doing. Otherwise don't touch this: 
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/c034fe4a-31c2-4486-9496-ac01f1fe0b7c)
6. After it is finished it will show you the command output results: 
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/07acbad9-e925-4cc3-9d23-cf749fdfafb7)
7. Your video file is now ready to be uploaded to YouTube for 3D processing. You will find it in the same directory from the video you selected with the end of the file name saying "3D_AR_1x1" before the file extension.

**NOTICE**: For some reason things seem to have changed somewhat with how YouTube processes these 3D files. While this currently still works for the YouTube app on mobile devices like Android/iOS, and the Quest via YouTubeVR, on the desktop browser it no longer appears in anaglyph 3D but just as side-by-side video.

**NOTICE #2**: For some reason there is an issue with the Quest recording for long recordings, the audio goes out of sync and trails BEHIND the video. I have confirmed this is an issue with the audio only and NOT the video length. As of now I have not come up with a solution for correcting this in processing. If anyone has any ideas, please let me know. I've tried a lot to figure this out and so far no answer.
##
### Swap Interval

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/d219c57b-e7f1-4407-8b8f-2c2bdb7c0f1a)


The Swap Interval settings is a bit hard to explain. [THIS PAGE](https://github.com/MortimerGoro/ovr-mobile-sys/blob/master/VrApi/Include/VrApi.h) seems to explain it in a very technical manner, under "Frame Timing". In practice this is what it seems to do, if your refresh rate is 90hz and you have the Swap Interval set to 1, when you record the framerate will be 90fps. However if you set the Swap Interval to 2, it will halve the recorded framerate. This is automatically applied in my framerate recording presets, specifically the 60fps/120hz setting. That one sets the display frequency to 120hz and the swap interval to 2, thus making the recording be 60fps. However the gameplay will have juttering, although this will not appear in the recorded video. There is another setting that is built into those recording framerate presets, namely debug.oculus.fullRateCapture, which gets set to 1, as by default it's set to 0. This seems to possibly toggle between variable framerate capture and full, else it is full and half respectively. Nevertheless to have this as an independent option isn't really useful by itself and I already have it in preset where it would be required so I may end up just removing this option all together.

# Tools Screen:

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/0f37d68c-1a09-4ea4-bd18-0548333a5361)
##

# Tools Screen Top Section

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/2fea58d2-a040-48e0-adcb-772a85d28974)
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
# Tools Screen Middle Section

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/5dd1e2c4-62a1-4ce1-aff3-2073fb323605)
##
### Enable OVR Metrics Tool Overlay

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/bff210dc-5ebd-4c63-9fff-e54f81ac40d2)

This will cause the OVR Metrics Tool to display an overlay consisting of statistics to monitor the performance of your game. This is useful when testing out new gaming profiles.
##
### Open File Manager

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/5a0e702d-80ab-4317-b414-90d220035786)

This will open File Manager +. If it is not installed, it will download it and install it then open it.
##
### Open QAVS

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/8af1e8c8-de12-4146-982a-3e487c7e5e6d)

This will open [Quest App Version Switcher](https://sidequestvr.com/app/5333/questappversionswitcher-qavs). If it is not installed, it will download it and install it, then open it.
##
### Open SideQuest

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/28bcc7e0-1dd8-484f-97b8-dd575c212fba)

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
6. If you enter the wrong password at this point, the Kiosk Mode app will launch again and you will need to reboot your headset to try again to reset it.
7. The only time you do NOT need to reboot your headset is in cases where the application you are running has an "EXIT" button allowing you to quit the application.
8. Kiosk Mode effectively "disables" the Oculus / Meta home button on the right controller. You can still however hold it down to recenter yourself.

##
### Un-set Kiosk Mode

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/1793ee1d-1fba-4492-af3b-58ed3fcadd96)

This will propmt you for the Kiosk Mode password and then it will entirely disable Kiosk Mode. This is here so that pressing the Volume Up button for an extended amount of time no longer triggers the Kiosk Mode enable password prompt.
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

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/fb99e977-2aa5-4272-b885-53a9d94e5bf0)
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

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/8c36cae0-fd69-4790-880d-36066dbcf0d7)



##

### Misc Screen Top Section
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/27176fde-7fd2-4f36-8a1c-02d74dd17890)

##
### Switch App Launch Detection Method

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/5bbf70e3-0331-4912-8d48-eb6d3c7bf360)


Clicking on this will toggle between two different app launch detection methods. The default is Logcat. The other is App Usage.
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
### Misc Screen Middle Section
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/19501e1a-1690-4694-a17f-42b69942f1b9)

##
Right now the only thing in this section are three customizable buttons. If you LONG PRESS on one, it will prompt you to enter an adb shell command. When you press OK, it will save that command as a preset for that button. So now in order to run that command just do a short single click on the button and it will then run the command and show a pop up of the output after the command is finished running. I don't know how useful this is, I may make more of these buttons, or remove them all together.
##

### Misc Screen Bottom Section
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/41556a10-6f79-44a3-bc36-f7feddde7ffa)


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
This will INSTANTLY reboot the headset. Sometimes however the ADB server seems to go stale. So if pressing this once doesn't immediately reboot your headset, pressing it again will.

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/c5e7b5f2-e4c4-47d7-b344-23bd82bcdbda)

##
### Dynamic Clock
There used to be a dynamic clock property that could be set via ADB on the Oculus / Meta headsets. This command doesn't seem to do anything anymore so I put it here and will probably remove it.

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/05de5cd7-ac90-401b-93ac-df2ec82ce8da)

##
### Delete BlazeRush Config

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/a66c146b-9503-4d8a-a337-510b4e8230b6)

"Delete BlazeRush config" will delete the config settings file for the game "BlazeRush". This is required if you want to run that game at a different resolution. This is because upon first run BlazeRush will get the device resolution and create a config file telling the game to run at that resolution. Once this config file is created, it will no longer look to see if the device has a different display resolution than what is stored in the config file. Therefore, if you want to run BlazeRush at a different resolution you MUST first delete the config file so that it will create a new config file based on the resolution you have set the device to.
##

### Apps I Worked On

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/20fda1a4-6d29-49e4-8486-b6913bfe1aa9)

This opens a page with links to other applications I've worked on.
##





