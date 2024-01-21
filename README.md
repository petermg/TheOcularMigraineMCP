# The Ocular Migraine {Dev Mode} Master Control Program.

### This is an applicaiton for use with the Oculus / Meta Quest mobile VR headsets, including the original Oculus Quest, Oculus / Meta Quest 2, Meta Quest Pro, Meta Quest 3.
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

## Main screen TOP section:
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/4434c847-89c4-490c-a82b-c298bb66871d)


![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/079550a3-e1c0-426e-950b-18017fb9806a)

## Statistics

From this section you will find a statistics read-out showing things like your device name, IP address, SSID name and signal strength, free space, and battery level and currently enabled display resolution. If you click on this it will update.

## About
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/1ed8def8-24d1-4df5-ac2c-0e79355048fe)

Clicking on "About" will take you to a screen showing the current version number of the app, credits, and an UPDATE button that will update the app. Currently it does not have version checking enabled so it just downloads the latest apk and installs it, regardless of if it's newer or not. Version checking implimentation is on the TO-DO list.

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/c5e796eb-4e79-4ac3-8d94-d4541d1be168)

## Font Size Adjustment
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/b571075c-0803-4023-bcdd-aa9688c1ab20)

Below the "About" button you will see the name of your device, for exmaple on the Quest 3 it will say "eureka", Quest 2 will say "hollywood". If you click on this you will have the option to change the scale of the font for the application.

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/93a0fce5-0be6-4d1c-ac46-295604aa8141)


## Resolution Slider

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/f87abc03-1854-4d92-9d3e-a7f0b926089c)

"Resolution Slider" is a slider where you can slide the cross-hair to the left and right. Left REDUCES the resolution and right INCREASES the resolution. However you must click on "Set Resolution" to apply your resolution setting. The slider also has the options "AR 1:1.1" and "x32". The first is the aspect multiplier of the slider, for example, if the height was set to 1000, the width is set to 1100. You can change this "AR" by simply clicking on it and it will change the mathematical function of the slider. Also there is the "x32" option. This is the number by which the notch of the cross-hair is multiplied by. The cross-hair starts on the left at 32 and all the way on the right goes to 130. Changing the default "x32" to another number changes what each notch on the slider is multiplied by.
## FFR Level
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/68cc9cc8-43b1-402c-851a-5c442235693f)

"FFR Level" allows you to set the Fixed Foveated Rendering amount. For best performance set this to 4 and keep "dynamic" enabled.
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/0f6e74c3-29b9-4819-bb38-30c9d19829a6)

## CPU Level
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/ad320f08-0169-4993-acaf-317d65e2f8f0)

"CPU Level" allows you to change the CPU to a set clock level. This is NOT recommended however as the device is set to dynamically do this. Setting this will result in more battery useage and more heat. This will NOT "unlock" any performance as the headset is DESIGNED to automatically scale the CPU up when needed to it's maximum clock rate.
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/f1202bb1-88a5-462a-b811-2872c00c29f5)

## GPU Level
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/6a7d2360-94e7-4c46-b766-a03eb1e51cb9)

"GPU Level" allows you to change the GPU to a set clock level. This is NOT recommended however as the device is set to dynamically do this. Setting this will result in more battery useage and more heat. This will NOT "unlock" any performance as the headset is DESIGNED to automatically scale the GPU up when needed to it's maximum clock rate.
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/2ae5cda2-e7c3-4d98-892f-47ede3b798f9)

## All Levels
![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/f4114b93-7097-4956-aee1-2117d15854f5)

"All Levels" simply has the 3 former options on their own menu screen (FFR Level/CPU Level/GPU Level). So this is redundant and later will be depricated itself or the other options will be, I've not decided yet.

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/a264a9ea-8516-42f8-9041-0cc421251519)

## Main screen MIDDLE section:

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/dde5dcc0-2b85-4375-babc-c60d21c24c72)

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/54142827-008d-4840-b034-a35b1ca1bec0)

"Display Frequency:" The options are 60hz, 72hz, 90hz, 120hz. Only the Quest 2 headset supports all 4 frequencies. The Quest 1 cannot go past 72hz. The Quest Pro cannot go past 90hz, nor can it do 60hz. The Quest 3 cannot do 60hz. Click on the frequency you want to set and it will be set if supported for your device.

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/42eb76b2-af6f-472a-8545-97bce3e4a286)

If you click on "Default Display Settings" any custom display settings you enabled will be cleared, thus setting the device back to default settings.

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/d7b58b55-329d-4690-a929-b6d12a4dc19c)

"Reset These Settings To Default" will reset the display settings to defaul - redundant and will probably be removed in an update.

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/d8cdd52b-7ad1-42fe-8895-1e0f5cd791d1)

"Reset ALL settings to default" will clear any settings changes you made on the headset. This will NOT remove any custom profiles nor will it erase any files on the device nor anything you saved to the device. It only clears any "setprop" commands that were sent to the headset, thus restoring the default settings.

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/001623b3-84a9-4b5c-8cfe-e3f362e2ae6f)

"Delete BlazeRush config" will delete the config settings file for the game "BlazeRush". This is required if you want to run that game at a different resolution. This is because upon first run BlazeRush will get the device resolution and create a config file telling the game to run at that resolution. Once this config file is created, it will no longer look to see if the device has a different display resolution than what is stored in the config file. Therefore, if you want to run BlazeRush at a different resolution you MUST first delete the config file so that it will create a new config file based on the resolution you have set the device to.

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/78d89a82-adf7-4c68-a474-fc6165f062f3)

"Save Game Profile" will save your custom display settings, (resolution, refresh rate, FFR amount, etc.) to a text file for whichever game you choose. You can also set these profiles to **AUTOMATICALLY** run by DEFAULT whenever you run the game you specify for it. When you click "Save Game Profile" you will be prompted to select the game you want to save the profile for. You will also then be prompted with a summary of the profile you are about to save.

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/5ca62129-1ec1-4b87-ba49-d07dd30c825c)

"Load Game Profile" is an option that will allow you to load the settings of a saved game profile that you saved earlier. You can then test it with other games and possibly save those settings to another profile for other games as well, with the option to also save it as default for another game.

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/2ee96f56-8dce-4d57-9549-c3649a69fead)

"Run Game" is for running a game while BYPASSING it's DEFAULT GAMING PROFILE that you saved for it. This is useful for testing other settings on a game when it ALREADY has a default gaming profile. This way you can launch the game with the current device settings that you set WITHOUT the app loading the custom default gaming profile settings, so you can test other settings to create other profiles without having to first DELETE the default gaming profile for that game.

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/38f73240-5ba1-4878-9099-da8e951c54b6)

"Game Backup" will open a menu to back up the game of your choice. This will give you the option to backup the entire game, (i.e. APK, obb and data folders from /sdcard/Android/), or to just back up the data files (from /sdcard/Android/data/yourgame). This can only back up the data folders that are stored in "/sdcard/Android/" This will ALSO present you a menu from which you can RESTORE your game backups with the option to restore the ENTIRE game, (APK, OBB, Data files), or JUST the data folders. Again, this only applies to data folders in "/sdcard/Android/" You can also select to restore backups from OTG media! This means if you copy your game backups onto a thumbdrive via an OTG cable, you can browse to it to select them. HOWEVER you must FIRST allow all files access to The Ocular Migraine and MOUNT an OTG device via a third party app, which The Ocular Migraine can download and install for you, "File Manager +".

## Recording Screen:

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/64fda31e-d15d-4427-b69e-e6e5e57f1413)

## Tools Screen:

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/4c62b54b-b81e-44f0-bdde-4927649f68fd)

## Misc Screen:

![image](https://github.com/petermg/TheOcularMigraineMCP/assets/20764493/267ac2dd-a3e3-49ba-b6cb-df8bc2cb3d86)

