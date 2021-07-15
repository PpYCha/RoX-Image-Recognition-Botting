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
xMouse = 953
yMouse = 446
wRegion = 143
yRegion = 144
#mouse pointer location click
xClick = 1020
yClick = 510

while keyboard.is_pressed('q') == False:
    if pyautogui.locateOnScreen('SouthGate.png', region=(xMouse,yMouse,wRegion,yRegion), grayscale=True, confidence=0.8) != None:
        print("cast")
        time.sleep(0.5)
        click(xClick,yClick)
    
    if pyautogui.locateOnScreen('SouthGateReel.png', region=(xMouse,yMouse,wRegion,yRegion), confidence=0.8) != None:
       
         pic = pyautogui.screenshot(region=(xMouse,yMouse,wRegion,yRegion))
         width, height = pic.size
         for x in range(0,width,5):
          for y in range(0,height,5):

            r,g,b = pic.getpixel((x,y))

            if b == 114:
               click(xClick,yClick)
               print("reel")
               break
        


