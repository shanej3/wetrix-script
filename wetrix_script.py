import win32api
import win32con
import os

# Set desired resolution, path, and, app name
# Keep the r in front of the "path"  for raw string

desiredGamingResolution = (800, 600)
desiredNormalResolution = (1920, 1080)
wetrixPath = r"Desired/Absolute/File/Path/Here"
appName = "Wetrix.exe"

def change_resolution(width, height):
    # Get current display settings
    devmode = win32api.EnumDisplaySettings(None, win32con.ENUM_CURRENT_SETTINGS)

    # Modify resolution
    devmode.PelsWidth, devmode.PelsHeight = width, height
    devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT

    # Apply the changes
    result = win32api.ChangeDisplaySettings(devmode, 0)

    # Check result
    if result == win32con.DISP_CHANGE_SUCCESSFUL:
        print(f"Resolution changed to {width}x{height}")
    else:
        print(f"Failed to change resolution. Error code: {result}")

def open_wetrix(filePath, appName):
    os.chdir(filePath)
    os.startfile(appName)

# Runs upon script opening
change_resolution(*desiredGamingResolution)
open_wetrix(wetrixPath, appName)

# Runs infinitely waiting for input
while True:
    user_input = input("Type 'exit' when done playing: ")
    if user_input.lower() == "exit":
        change_resolution(*desiredNormalResolution)
        quit()
        break




    
