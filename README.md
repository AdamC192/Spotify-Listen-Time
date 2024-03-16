# SPOTIFY-LISTEN-TIME
 View your spotify listening stats with this simple program

**FEATURES (V1.0)**
- View total listening hours based on provided .JSON data files.
- Sum the total listening hours from multiple .JSON data files. 

**INSTRUCTIONS & USE CASES**

Requesting streaming history from spotify:
 1. Follow this link: https://www.spotify.com/uk/account/privacy/
 2. Scroll down to find the 'Download Your Data' section.
 3. Select the checkbox saying 'Select Extended streaming history'
 4. To continue press the 'Request Data' button.
 5. You should receive an email mentioning that you need to 'Confirm your data request' make sure to press confirm,

![image](https://github.com/AdamC192/Spotify-Listen-Time/assets/112624338/4a8ebefe-dac4-4287-9b25-9834d9939e49)

   
 6. Await an email that looks like the following (this email should take no longer than 30 days to come through),

![image](https://github.com/AdamC192/Spotify-Listen-Time/assets/112624338/74c4dcf6-8e77-4ffc-8520-60f95b214399)


Add a file to the program:
 1. Once the file has downloaded, extract the .ZIP folder in an accessible location (such as the desktop or documents folders).
 2. Open the folder and locate a folder named 'StreamingHistory_music_[NUMBER].json' (there may be multiple files)

![image](https://github.com/AdamC192/Spotify-Listen-Time/assets/112624338/fd3a9621-e4c1-4664-814d-1037ea1f37ce)

 3. Copy the directory of on of the files and open the python script 'main.py'.
 4. Enter the directory of the file into the termial of the running python script (make sure to double slash any backslashes and that there are no quotation marks included in the directory),

![image](https://github.com/AdamC192/Spotify-Listen-Time/assets/112624338/50c62666-6e66-491d-966b-2a75c33e75b4)

 5. Press enter to add the file the program, once complete it should show your total listening time,

![image](https://github.com/AdamC192/Spotify-Listen-Time/assets/112624338/75803cc2-7260-4eee-a32c-f8a7292c8f23)

 6. From this point you can type 'RESET' in the terminal to reset the program and the current total listen time, or you can type in the directory of another file to add to your total listen time.
