# SPOTIFY-LISTEN-TIME
 View your spotify listening stats with this simple application

**FEATURES (V2.0)**
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



Add a file to the program (You can run the "SpoTimer.py" in VSCode instead of installing the .exe if you want):
 1. Download your spotify listening data from the email you received and extract the file to your preferred directory.
 2. Download this project as a ZIP file, once installed extract the project then extract the "SpoTimerExecutable.zip" file to the directory you want to store the application at.
 3. Launch the application.

![image](https://github.com/AdamC192/Spotify-Listen-Time/assets/112624338/bbad339e-d1c1-4085-8ed3-d3d52c092ebe)


 3. Once the applicaton has opened, click the "ADD FILE" button, in file explorer find the "StreamingHistory" files and select file,

![image](https://github.com/AdamC192/Spotify-Listen-Time/assets/112624338/8af65e75-e2d8-4f6e-bbff-3f7cc201467a)


 4. Add as much files as you want, and once finished press the "CALCULATE TOTAL" button, your total listen hours should show (values in the terminal behind the application are the individual hours for each file provided),

![image](https://github.com/AdamC192/Spotify-Listen-Time/assets/112624338/080d12b0-7ce6-431f-b8e7-1a1c6b6c246c)


 5. From this point you can add more files using the "ADD FILE" button, recalculate the total, or press "RESET" to reset the program.

All code involved in the application is contained in the "SpoTimer.py", feel free to take what you want.
