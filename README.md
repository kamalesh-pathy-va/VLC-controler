# VLC-controler
I just wanted to create a controler (using my phone) to controll certain features of VLC media player running on my pc.

# About
Guys I'm not a pro, I just wanted to create something intresting so I made this.
I used HTML to create a web page which can act as video controler, that has buttons like Play, Pause, Rewind, Volume up, Full screen, etc.
I created node server using the "express" library(Please use 'npm install express' to install) so that the data can be sent to the server which is displayed on another web page "Reciver"(which is buggy, but still its an additional feature that is buggy).
The main.py is the main file which is needed to be executed, this file uses two module "Selenium" and "Pyautogui".
The selenium module is to read the data on the recivers page and takes the requred actions.
I used AutoHotkey script (which is converted to exe file) to press certain keys on the keyboard so that on what ever window you are in it will go to the VLC media player and perform the action. For example if you've pressed the play button on the web page the VLC media player gets focused and the action is taken.
(To be continued)...
