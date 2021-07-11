#This script locates the image stickman.png in the region we give it and tell you if it can see it

from pyautogui import * 
import pyautogui 
import time 
import keyboard 
import random
import win32api, win32con


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


def move(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


#image region 
xMouse = 762
yMouse = 300
wRegion = 78
yRegion = 70
#mouse pointer location click
xClick = 806
yClick = 323

while keyboard.is_pressed('q') == False:
    if pyautogui.locateOnScreen('gathering.png', region=(xMouse,yMouse,wRegion,yRegion), grayscale=True, confidence=0.8) == None:
        print("gathering")
        click(xClick,yClick)
        time.sleep(0.5)
    
    
