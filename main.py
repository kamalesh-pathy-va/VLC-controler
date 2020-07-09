from selenium import webdriver
import time
import pyautogui
import os


print("If you dont have vlc media player opened, Please do it.\nStarting some required applicaion...\nStarting 'videoControler.exe'")
os.startfile("videoControler.exe")
print("Starting runapps.bat")
os.startfile("runapps.bat")
time.sleep(3)
with open("ipconfiglog(pleaseDoNotModifyThisFiel).log", 'r') as logfile:
    lines = logfile.readlines()

for line in lines:
    if "IPv4 Address. . . . . . . . . . . : " in line:
        print('To use the controler, enter this URL in your browser:', line.lstrip(
            "   IPv4 Address. . . . . . . . . . . : ").rstrip("\n"), ':4382')

os.remove("ipconfiglog(pleaseDoNotModifyThisFiel).log")

print("Opening the Webpage for the logs...(doesn't require internet)")
browser = webdriver.Chrome()
print("Loading the page...")
browser.get("http://127.0.0.1:4382/reciver.html")

commands = []
print("Everything looks fine and you can start using it in...\n3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(0.3)
print("Setup's over controler is online!")
pyautogui.hotkey('ctrl', 'win', 'alt', 'v')
pyautogui.hotkey('ctrl', 'win', 'alt', 'p')
while True:
    theCommand = browser.find_element_by_id("log").text
    if theCommand not in commands:
        commands.append(theCommand)
        if 'Play' in theCommand:
            print("play button")
            pyautogui.hotkey('ctrl', 'win', 'alt', 'v')
            pyautogui.hotkey('ctrl', 'win', 'alt', 'p')
        elif 'Pause' in theCommand:
            print("pause button")
            pyautogui.hotkey('ctrl', 'win', 'alt', 'v')
            pyautogui.hotkey('ctrl', 'win', 'alt', 'p')
        elif 'Mute' in theCommand:
            print('mute button')
            pyautogui.hotkey('ctrl', 'win', 'alt', 'v')
            pyautogui.hotkey('ctrl', 'win', 'alt', 'm')
        elif 'Unmute' in theCommand:
            print('unmute button')
            pyautogui.hotkey('ctrl', 'win', 'alt', 'v')
            pyautogui.hotkey('ctrl', 'win', 'alt', 'm')
        elif 'Fastforward' in theCommand:
            print('fastforward button')
            pyautogui.hotkey('ctrl', 'win', 'alt', 'v')
            pyautogui.hotkey('ctrl', 'win', 'alt', 'f')
        elif 'Rewind' in theCommand:
            print("rewind button")
            pyautogui.hotkey('ctrl', 'win', 'alt', 'v')
            pyautogui.hotkey('ctrl', 'win', 'alt', 'r')
        elif 'VolumeUp' in theCommand:
            print('volumup button')
            pyautogui.hotkey('ctrl', 'win', 'alt', 'v')
            pyautogui.hotkey('ctrl', 'win', 'alt', 'u')
        elif 'VolumeDown' in theCommand:
            print('volumedown button')
            pyautogui.hotkey('ctrl', 'win', 'alt', 'v')
            pyautogui.hotkey('ctrl', 'win', 'alt', 'd')
        elif 'FullScreen' in theCommand:
            print('full screen button')
            pyautogui.hotkey('ctrl', 'win', 'alt', 'v')
            pyautogui.hotkey('ctrl', 'win', 'alt', 'b')
        elif 'ExitFullScreen' in theCommand:
            print('exit full screen button')
            pyautogui.hotkey('ctrl', 'win', 'alt', 'v')
            pyautogui.hotkey('ctrl', 'win', 'alt', 'b')
        else:
            print("Some how you've messed up the HTML, or a new feature is add that I can't understand.")
    # print(commands)
    time.sleep(0.3)
