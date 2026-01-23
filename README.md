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

## Running Automatically with Task Scheduler

To run the script automatically on startup **without a visible window**:

1. Open Task Scheduler
2. Action => Create Basic Task...
3. Give it a name and description
4. On the Trigger page select "When I log on"
5. On the Action page select "Start a program"
6. For **Program/script**, browse to and select your `pythonw.exe` inside the virtual environment, for example:
   ```
   C:\Users\YourUsername\Documents\sus-windows\.venv\Scripts\pythonw.exe
   ```
7. For **Add arguments (optional)**, enter:
   ```
   shut-up-system-windows.py
   ```
8. For **Start in (optional)**, enter:
   ```
   C:\Users\YourUsername\Documents\sus-windows
   ```
9. Click Finish

(Optional)  
10. Go to the Task Scheduler Library tab and refresh to check that the new task is running  
11. Log in and out and check system volume. It should be 0  
12. Increase the volume and verify that it goes back to 0 (this may take up to a minute)

## Troubleshooting
- Ensure your virtual environment is activated and dependencies are installed.
- If the script does not mute system sounds, check that `pycaw` is installed and working.
- Make sure the paths in Task Scheduler are correct for your system.
