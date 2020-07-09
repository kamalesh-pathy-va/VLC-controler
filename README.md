# VLC-controler
I just wanted to create a controler (using my phone) to controll certain features of VLC media player running on my pc.

# About
Guys I'm not a pro, I just wanted to create something intresting so I made this.<br>
I used HTML to create a web page which can act as video controler, that has buttons like Play, Pause, Rewind, Volume up, Full screen, etc.<br>
I created node server using the "express" library so that the data can be sent to the server which is displayed on another web page "Reciver"(which is buggy, but still its an additional feature that is buggy).<br>
The main.py is the main file which is needed to be executed, this file uses two module "Selenium" and "Pyautogui".<br>
The selenium module is to read the data on the recivers page and takes the requred actions.<br>
I used AutoHotkey script (which is converted to exe file) to press certain keys on the keyboard so that on what ever window you are in it will go to the VLC media player and perform the action. For example if you've pressed the play button on the web page the VLC media player gets focused and the action is taken.<br>

# Requirements
I've used some different programming languages to do this thing(rubbish!!).<br>
You should have *python 3* installed before hand<br>
Open CMD and run <code>*pip install -r requirements.txt*</code>, it will install all the required python modules.<br>
You should have *node* installed before hand<br>
Open CMD and point to the directory where all these files are located, then run <code>*npm install express*</code>.<br>
Thats all for the dependencies.
