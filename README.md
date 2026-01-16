# Shut Up System Windows

This program automatically mutes the Windows System Sounds every minute. It uses the [pycaw](https://github.com/AndreMiras/pycaw) library to control audio sessions and sets the System Sounds volume to zero if it is not already muted.

## Features
- Mutes Windows System Sounds automatically every minute
- Runs silently in the background

## Installation

1. **Clone or Download the Repository**
   ```
   git clone https://github.com/CheapPizza/sus-windows
   cd sus-windows
   ```

2. **Create a Python Virtual Environment**
   ```
   python -m venv .venv
   ```

3. **Activate the Virtual Environment**
   - On Windows Command Prompt:
     ```
     .venv\Scripts\activate
     ```
   - On PowerShell:
     ```
     .venv\Scripts\Activate.ps1
     ```

4. **Install Requirements**
   ```
   pip install -r requirements.txt
   ```

5. **Edit the Batch File**
   Open `shutup.bat` and make sure the paths point to your repository and virtual environment location:
   ```bat
   cd /d "C:\Users\YourUsername\Documents\sus-windows"
   call .venv\Scripts\activate.bat
   pythonw shut-up-system-windows.py
   ```

## Running Automatically with Task Scheduler

To run the script automatically on startup:

1. Open Task Scheduler
2. Action => Create Basic Task...
3. Give it a name and desciprtion
4. On the Trigger page select "When I log on"
5. On the Action page select "Start a program"
6. Select shutup.bat using the file browser
7. Just click Finish and you are done  
(Optional)  
8. Go to the Task Scheduler Library tab and refresh to check that the new task is running
9. Log in and out and check system volume. It should be 0
10. Increase the volume and verify that it goes back to 0 (this may take up to a minute)

## Troubleshooting
- Ensure your virtual environment is activated and dependencies are installed.
- If the script does not mute system sounds, check that `pycaw` is installed and working.
- Make sure the batch file paths are correct for your system.
