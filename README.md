# The Ocular Migraine: {Dev Mode} Master Control Program.

### This is an applicaiton for use with the Oculus / Meta Quest mobile VR headsets, including the original Oculus Quest, Oculus / Meta Quest 2, Meta Quest Pro, Meta Quest 3.

## Table Of Contents:

- [Installation](#installation)


* [The Main Screen](#main-screen)
  * [Top Section](#main-screen-top-section)
    * [Statistics Readout](#statistics)
    * [Font Size Adjustment](#font-size-adjustment)
    * [About](#about)
    * [Resolution Slider](#resolution-slider)
    * [Fixed Foveated Rendering (FFR)](#ffr-level)
    * [CPU Level](#cpu-level)
    * [GPU Level](#gpu-level)
    * [All Levels](#all-levels)
  * [Middle Section](#main-screen-middle-section)
    * [Display Frequency](#display-frequency)
    * [Default Display Settings](#default-display-settings)
    * [Reset These Settings To Default](#reset-these-settings-to-default)
    * [Reset ALL settings to default](#reset-all-settings-to-default)
    * [Delete BlazeRush config](#delete-blazerush-config)
    * [Save Game Profile](#save-game-profile)
    * [Load Game Profile](#load-game-profile)
    * [Run Game](#run-game)
    * [Game Backup Menu](#game-backup)
      * Backup Options
        * [Game + Data (Full Game Backup)](#full-game-backup)
        * [Game Data Only](#game-data-backup-only)
      * Restore Options
        * [Full Game](#full-game)
        * [Game ONLY](#game-only)
        * [Game Data](#game-data)
* [The Recording Screen](#recording-screen)
  * [Top Section](#recording-screen-top-section)
    * [Resolution Presets](#resolution-presets)
    * [Custom Resolution](#custom-resolution)
  * [Middle Section](#recording-screen-middle-section)
    * [Recording FrameRate](#recording-framerate)
    * [Recording Eye](#recording-eye)
  * [Bottom Section](#recording-screen-bottom-section)
    * [Recording Bitrate](#recording-bitrate)
    * [FOV Crop](#fov-crop)
    * [Save Recording Profile](#save-recording-profile)
    * [Load Recording Profile](#load-recording-profile)
    * 
* [The Tools Screen](#tools-screen)
* [The Misc Screen](#misc-screen)
* 
[The Main Screen (About)](#about)




## Installation.


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

## Main Screen:

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/2ac5e1ad-c750-4818-a935-afeebd6621bc)
## 
## Main screen TOP section:
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/4434c847-89c4-490c-a82b-c298bb66871d)

## 
## Statistics
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/079550a3-e1c0-426e-950b-18017fb9806a)

From this section you will find a statistics read-out showing things like your device name, IP address, SSID name and signal strength, free space, and battery level and currently enabled display resolution. If you click on this it will update.
## 
## About
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/1ed8def8-24d1-4df5-ac2c-0e79355048fe)

Clicking on "About" will take you to a screen showing the current version number of the app, credits, and an UPDATE button that will update the app. Currently it does not have version checking enabled so it just downloads the latest apk and installs it, regardless of if it's newer or not. Version checking implimentation is on the TO-DO list.

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/c5e796eb-4e79-4ac3-8d94-d4541d1be168)
## 
## Font Size Adjustment
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/b571075c-0803-4023-bcdd-aa9688c1ab20)

Below the "About" button you will see the name of your device, for exmaple on the Quest 3 it will say "eureka", Quest 2 will say "hollywood". If you click on this you will have the option to change the scale of the font for the application.

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/93a0fce5-0be6-4d1c-ac46-295604aa8141)

## 
## Resolution Slider

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/f87abc03-1854-4d92-9d3e-a7f0b926089c)

"Resolution Slider" is a slider where you can slide the cross-hair to the left and right. Left REDUCES the resolution and right INCREASES the resolution. However you must click on "Set Resolution" to apply your resolution setting. The slider also has the options "AR 1:1.1" and "x32". The first is the aspect multiplier of the slider, for example, if the height was set to 1000, the width is set to 1100. You can change this "AR" by simply clicking on it and it will change the mathematical function of the slider. Also there is the "x32" option. This is the number by which the notch of the cross-hair is multiplied by. The cross-hair starts on the left at 32 and all the way on the right goes to 130. Changing the default "x32" to another number changes what each notch on the slider is multiplied by.
## 
## FFR Level
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/68cc9cc8-43b1-402c-851a-5c442235693f)

"FFR Level" allows you to set the Fixed Foveated Rendering amount. For best performance set this to 4 and keep "dynamic" enabled.
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/0f6e74c3-29b9-4819-bb38-30c9d19829a6)
## 
## CPU Level
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/ad320f08-0169-4993-acaf-317d65e2f8f0)

"CPU Level" allows you to change the CPU to a set clock level. This is NOT recommended however as the device is set to dynamically do this. Setting this will result in more battery useage and more heat. This will NOT "unlock" any performance as the headset is DESIGNED to automatically scale the CPU up when needed to it's maximum clock rate.
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/f1202bb1-88a5-462a-b811-2872c00c29f5)
## 
## GPU Level
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/6a7d2360-94e7-4c46-b766-a03eb1e51cb9)

"GPU Level" allows you to change the GPU to a set clock level. This is NOT recommended however as the device is set to dynamically do this. Setting this will result in more battery useage and more heat. This will NOT "unlock" any performance as the headset is DESIGNED to automatically scale the GPU up when needed to it's maximum clock rate.
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/2ae5cda2-e7c3-4d98-892f-47ede3b798f9)
## 
## All Levels
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/f4114b93-7097-4956-aee1-2117d15854f5)

"All Levels" simply has the 3 former options on their own menu screen (FFR Level/CPU Level/GPU Level). So this is redundant and later will be depricated itself or the other options will be, I've not decided yet.

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/a264a9ea-8516-42f8-9041-0cc421251519)
## 
## Main screen MIDDLE section:

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/dde5dcc0-2b85-4375-babc-c60d21c24c72)
## 
 
### Display Frequency
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/54142827-008d-4840-b034-a35b1ca1bec0)

"Display Frequency:" The options are 60hz, 72hz, 90hz, 120hz. Only the Quest 2 headset supports all 4 frequencies. The Quest 1 cannot go past 72hz. The Quest Pro cannot go past 90hz, nor can it do 60hz. The Quest 3 cannot do 60hz. Click on the frequency you want to set and it will be set if supported for your device.
##
 
### Default Display Settings
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/42eb76b2-af6f-472a-8545-97bce3e4a286)

If you click on "Default Display Settings" any custom display settings you enabled will be cleared, thus setting the device back to default settings.
##
### Reset These Settings To Default
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/d7b58b55-329d-4690-a929-b6d12a4dc19c)

"Reset These Settings To Default" will reset the display settings to defaul - redundant and will probably be removed in an update.
##
 
### Reset ALL settings to default 
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/d8cdd52b-7ad1-42fe-8895-1e0f5cd791d1)

"Reset ALL settings to default" will clear any settings changes you made on the headset. This will NOT remove any custom profiles nor will it erase any files on the device nor anything you saved to the device. It only clears any "setprop" commands that were sent to the headset, thus restoring the default settings.
##
### Delete BlazeRush config
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/001623b3-84a9-4b5c-8cfe-e3f362e2ae6f)

"Delete BlazeRush config" will delete the config settings file for the game "BlazeRush". This is required if you want to run that game at a different resolution. This is because upon first run BlazeRush will get the device resolution and create a config file telling the game to run at that resolution. Once this config file is created, it will no longer look to see if the device has a different display resolution than what is stored in the config file. Therefore, if you want to run BlazeRush at a different resolution you MUST first delete the config file so that it will create a new config file based on the resolution you have set the device to.


## 
### Save Game Profile 

https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/3c85d9f7-503c-44a0-b0c2-ac10f90198a5

"Save Game Profile" will save your custom display settings, (resolution, refresh rate, FFR amount, etc.) to a text file for whichever game you choose. You can also set these profiles to **AUTOMATICALLY** run by DEFAULT whenever you run the game you specify for it. When you click "Save Game Profile" you will be prompted to select the game you want to save the profile for. You will also then be prompted with a summary of the profile you are about to save.
In order to create a custom game profile, do the following:
1. Move the Resolution Slider to your desired game resolution.
2. Press Set Resolution.
3. Click on Save Game Profile.
   ![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/78d89a82-adf7-4c68-a474-fc6165f062f3)
5. Select the game you want to save the profile for.
6. Make your selection of "Yes" (creates loadable non-default profile), "Make Kiosk App" (sets the game as the Kiosk App), "Set as Default" (saves the profile AND makes it the default profile to load when you launch the game), or "No", which cancels the action without saving the profile.

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/17908281-5af8-4ed8-af07-c266d71cc45e)


6. Run your game from the normal game selection menu and it will automatically load it's default profile if you saved one for it. Otherwise you can go to "Manage Game Profiles" on the Tools page and load different profiles you have saved for your games, you can have multiple profiles per game, and run ones from that menu without invoking the default profile being loaded. This is good for testing different profiles or just switching between different profiles for different reasons, like recording vs just gameplay.

## 
### Load Game Profile



https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/89bacee2-60b9-4615-bf78-c1a77d8af6b8

"Load Game Profile" is an option that will allow you to load the settings of a saved game profile that you saved earlier. You can then test it with other game profiles and possibly save those settings to another profile for other games as well, with the option to also save it as default for another game, for example if you find that multiple games work well with the same profile.
1. Select "Load Game Profile" ![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/5ca62129-1ec1-4b87-ba49-d07dd30c825c)
2. Select the folder of your game.

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/c9749f23-8b37-48ae-a0ac-9222013fc45c)

3. Select the profile you wish to load.

4. The following screen will show you the details of the game profile you just selected and present the following options to you:

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/fa53932e-5486-42b5-b607-a6154fcf9dfe)


"Delete" (this deletes the profile).

"Cancel", (this cancels the operation and takes you back to the Main page).

"Delete Default", (this deletes any default profile for the game).

"Set Default", (this makes the currently loaded profile the default profile for the selected game).

"Run", (this will run the game with the selected profile BYPASSING any default profile saved for the game, which is useful for testing alternate profiles for things like gameplay or recording or just testing different settings).
##

### Run Game
"Run Game" is for running a game while BYPASSING it's DEFAULT GAMING PROFILE that you saved for it. This is useful for testing other settings on a game when it ALREADY has a default gaming profile. This way you can launch the game with the current device settings that you set WITHOUT the app loading the custom default gaming profile settings, so you can test other settings to create other profiles without having to first DELETE the default gaming profile for that game.
1. Click on "Run Game". ![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/2ee96f56-8dce-4d57-9549-c3649a69fead)
2. Select the game you wish to run.
3. The game will now launch without loading it's default profile, thus enabling you to test different settings on the game without it changing them by loading the default profile if it has one. If a game does NOT have a default profile, you can just launch it normally from the games menu.

## 
## Game Backup
"Game Backup" will open a menu to back up (or restore a backup of) the game of your choice. This will give you the option to backup the entire game, (i.e. APK, obb and data folders from /sdcard/Android/), or to just back up the data files (from /sdcard/Android/data/yourgame). This can only back up the data folders that are stored in "/sdcard/Android/" From this same menu you can RESTORE your game backups with the option to restore the ENTIRE game, (APK, OBB, Data files), or JUST the data folders. Again, this only applies to data folders in "/sdcard/Android/" You can also select to restore backups from OTG media! This means if you copy your game backups onto a thumbdrive via an OTG cable, you can browse to it to select them. HOWEVER you must FIRST allow all files access to The Ocular Migraine and MOUNT an OTG device via a third party app, which The Ocular Migraine can download and install for you, "File Manager +". All backups will be made in /sdcard/MCP/Backups/name-of-your-game. Along with the backup files there will be additional files, a Windows binary of adb and a bat file. This will allow you to restore your backups directly from a Windows PC without the need to copy the backup files back to your headset before restoring them. Just copy the backup folders to your Windows PC, then run the bat file for the game you wish to restore and select your restore options. It will restore your game directly from your PC. To get started, click on 

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/38f73240-5ba1-4878-9099-da8e951c54b6)

You will be presented with the following menu:
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/02199091-4404-4ab5-924c-d2c0ef002899)
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


## Recording Screen:

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/64fda31e-d15d-4427-b69e-e6e5e57f1413)
##
### Recording Screen Top Section
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/d22322b4-3b9e-47f5-b3b9-bd924e79d7d6)
##
### Resolution Presets
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/fd68f709-b140-4a84-af74-41b10de389e6)


On the top section of the Recording Screen you can set different recording resolutions. There are custom resolution presets and the option to set your own custom resolution. The presets are as follows:

1920x1080(16:9) - this is the Full HD resolution, pretty self explainitory.

3840x2160(16:9) - this is 4K resolution, only recommended for the Quest 3.

1280X720(16:9) - "HD" resolution.

3840X1080(3D) - I created this preset thinking that the device would record both eyes in a 16:9 aspect ratio. However when telling the device to record both eyes, it records each eye in a 1 by 1 aspect ration. This seems not to be able to be changed. However you can still use this when recording in 3D if you want, but this does NOT set the device to record in 3D, it only sets the resolution, you will need to click on [Both(3D)] in the Middle Section under Recording Eye to record in 3D.

2560X720(3D) - see notes from previous preset.

1080X1920(9:16) - makes a vertical recording like for YouTube Shorts, tiktok, etc..

720X1280(9:16) - makes a vertical recording like for YouTube Shorts, tiktok, etc..
##
### Custom Resolution
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/dbc3d68f-ac10-4f5c-a3b6-62925cf2da90)

Here you can enter in your own recording Width and Height.
##
### Recording Screen Middle Section
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/caecbe54-75c5-40c6-9cdf-3d0b0e1c4978)
##
### Recording FrameRate
The following options are:
* 60hz/fps
* 60fps@120hz
* 72hz/fps
* 90hz/fps
* 120hz/fps

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/afc32c5a-d0cb-489e-94ba-8d21c48647fc)

Please note, the Quest 1 cannot go above 72hz, the Quest Pro can only do 72hz and 90hz, and the Quest 3 can not do 60hz. Only the Quest 2 can do all 4 options. Also the 60fps@120hz option is NOT recommended as it makes your experience jerky, even though the recording may look fine. This was more of an exeprimental feature to get the Quest Pro and Quest 3 to record at 60fps.
##
### Recording Eye
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/29463ba8-a5f0-4fca-9a4a-29cc2a03b189)

The following options are:
* Left Eye - Records from the left eye.
* Both(3D) - Records BOTH eyes, for 3D.
* Right Eye - Records from the right eye.
##
### Recording Screen Bottom Section
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/376beecf-a1fb-4c7e-b697-a5a93b4ca268)
##
### Recording Bitrate
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/94bc0e28-8220-46ed-aee1-3f701be1190a)

Select this to set your recording bitrate. I have made the default selection 45Mbps.
##
### FOV Crop
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/039a40de-debf-4738-bc81-30b5fee89229)

This seems to be a little known feature that allows you to crop the rendered areas of your screen. This concentrats whatever your set resolution is into this cropped area, thus making the image much clearer. This is beneficial for gameplay recordings, it improves the visual quality of them greatly. Here are the following options:
* Up - crops the top part of the render area.
* Down - crops the bottom part of the render area.
* Outward - crops the outward edges of the render area, the edges of the screen that are away from your nose for each eye.
* Inward - crops the inward edges of the render area, the edges of the screen that are toward your nose for each eye.
* Remove Crop - removes any crop you have set.
* Optimal Crop - enables a preset crop that should correctly match up with the rendering area for recording.
##
### Save Recording Profile
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/6c1611cd-8329-4e0f-ba3f-908aededc8ff)

Saving a Recording Profile creates a recording profile that stores all of your current disiplay information, such as resolution, GPU/CPU levels, FFR level, Refresh Rate and also your recording settings such as recording bitrate, recording eye, recording resolution, screen crop and saves it to a recording profile which you can load for the game you have selected or even load it for use with any game. You can even save it as a default profile using the Manage Default Profiles option on the Tools Screen. In order to create a Recording Profile, just set whatever resolution you want from the Main Screen, set the recording resolution and framerate and bitrate and eye recording selection then click on Save Recording Profile. It will propmt you to select which game you wish to save it for, but this does NOT make it a default profile for that game. The game selected will still be run with it's default profile unless you load it's recording profile from the Load Recording Profile screen and select RUN.

https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/52f6b17d-b7ce-4039-9c19-b74b02ce06a4
##
### Load Recording Profile
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/8ecf5c16-4bf7-462a-bf0d-f0f15ef96f8d)

Clicking on Load Recording Profile you will be able to load any saved recording profiles. After selecting your recording profile you are presented with the following options:
* Load Only - This will load the settings in the selected Recording Profile onto the headset.
* Run - This will engage the settings from the Recording Profile and run the game it was saved for.
* Delete - This will delete the selected Recording Profile.
* Cancel - This will cancel the operation.
  
https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/34e7da94-53b9-49a1-9664-1e49b497e103

##
## Inject 3D Metadata
This is used to inject 3D metadata into the videos you've recorded after selecting "Both(3D)" for eye recording, for upload to YouTube. This will allow your video to be played back in 3D from YouTube in YouTube VR for sharing with friends.
1. Click on Inject 3D Metadata

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/30f98d44-638b-4dab-b0ee-81ffba91a847)

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








## Tools Screen:

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/4c62b54b-b81e-44f0-bdde-4927649f68fd)

## Misc Screen:

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/267ac2dd-a3e3-49ba-b6cb-df8bc2cb3d86)










