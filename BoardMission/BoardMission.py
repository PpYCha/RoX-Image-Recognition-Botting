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


#image region daily 
xDailyMouse = 250
yDailyMouse = 271
wDailyRegion = 37
yDailyRegion = 16
xDailyClick = 250
yDailyClick = 271

#image region pathFinding
xPath = 640
yPath = 275
wRegionPath = 25
hRegionPath = 28
#mouse pointer location click

#skip image region
xSkipRegion = 1028
ySkipRegion = 124
wSkipRegion = 102
hSkipRegion = 37
xSkipClick = 1075
ySkipClick = 139

#channel close
xChannel = 835
yChannel = 208
wChannel = 30
hChannel = 30
xChannelClick = 848
yChannelClick = 220

#mission quest board to detect quest completed
xmissionBoard = 217
ymissionBoard = 146
wmissionBoard = 938
hmissionBoard = 466

#submit mission board
xSubmit = 619
ySubmit = 522
wSubmit = 151
hSubmit = 47
xSubmitClick = 694
ySubmitClick = 539

#close mission board
xCloseMb = 1085
yCloseMb = 125
wCloseMb = 69
hCloseMb = 62
xCloseMbClick = 1117
yCloseMbClick = 161

#Appease Bird
xAppeaseBird = 814
yAppeaseBird = 285
wAppeaseBird = 77
hAppeaseBird = 71
xAppeaseBirdClick = 853
yAppeaseBirdClick = 316

#check
xCheck = 977
yCheck = 205
wCheck = 72
hCheck = 69
xCheckClick = 1015
yCheckClick = 240

#check2
xCheck2 = 820
yCheck2 = 284
wCheck2 = 69
hCheck2 = 71
xCheckClick2 = 856
yCheckClick2 = 317

#check2
xCheck3 = 820
yCheck3 = 284
wCheck3 = 69
hCheck3 = 71
xCheckClick3 = 847
yCheckClick3 = 315

#Hand over
xHandOver = 940
yHandOver = 479
wHandOver = 82
hHandOver = 30
xHandOverClick = 1000
yHandOverClick = 490

#Hand over item
xHandOverItem = 895
yHandOverItem = 550
wHandOverItem = 155
hHandOverItem = 50
xHandOverClickItem = 967
yHandOverClickItem = 576

# Resurrect 
xResurrect =  952
yResurrect = 575
wResurrect = 109
hResurrect = 39
xResurrectClick = 1000
yResurrectClick = 593

#AutoAttack
xAutoAttack = 795
yAutoAttack = 500
wAutoAttack = 50
hAutoAttack = 50

#  or pyautogui.locateOnScreen('autoAttack.png', region=(xAutoAttack,yAutoAttack,wAutoAttack,hAutoAttack), grayscale=True, confidence=0.8) != None 

while keyboard.is_pressed('q') == False:
    daily = ['daily', 'daily2', 'daily3', 'daily4','daily5', 'daily6', 'daily7','daily8','dailyRow1', 'dailyRow2', 'dailyRow3', 'dailyRow4']
        
    for d in daily:

     if pyautogui.locateOnScreen('pathFinding.png', region=(xPath,yPath,wRegionPath,hRegionPath), grayscale=True, confidence=0.8) != None  :
                print("goin the location")      
                break
     else:    
                start1 = pyautogui.locateOnScreen('./images/' + d + '.png', region=(250,271,158,116), grayscale=True,  confidence=0.8) 
                print(start1)
                pyautogui.moveTo(start1)#Moves the mouse to the coordinates of the image
                pos1 = pyautogui.position()
                if  start1 != None  :
                        click(pos1.x,pos1.y)
                        print(d)
                        time.sleep(5)
                

    if pyautogui.locateOnScreen('skip.png', region=(xSkipRegion,ySkipRegion,wSkipRegion,hSkipRegion), grayscale=True, confidence=0.8) != None or pyautogui.locateOnScreen('skip2.png', region=(xSkipRegion,ySkipRegion,wSkipRegion,hSkipRegion), grayscale=True, confidence=0.8) != None  :
        print("skip detected")
        click(xSkipClick,ySkipClick)
        time.sleep(1.5)

    if pyautogui.locateOnScreen('closeChannel.png', region=(xChannel,yChannel,wChannel,hChannel), grayscale=True, confidence=0.8) != None :
        print("1= closeChannel")
        click(xChannelClick,yChannelClick)
        time.sleep(1.5)

    if pyautogui.locateOnScreen('questCompleted.png', region=(xmissionBoard,ymissionBoard,wmissionBoard,hmissionBoard), grayscale=True, confidence=0.8) != None :
        
        start = pyautogui.locateOnScreen('questCompleted.png', region=(xmissionBoard,ymissionBoard,wmissionBoard,hmissionBoard), grayscale=True, confidence=0.8) 
        print(start)
        pyautogui.moveTo(start)#Moves the mouse to the coordinates of the image
        pos = pyautogui.position()
        
        click(pos.x,pos.y)
        print("click quest completed")
        time.sleep(2.5)
    else:
        if pyautogui.locateOnScreen('closeMb.png', region=(xCloseMb,yCloseMb,wCloseMb,hCloseMb), grayscale=True, confidence=0.8) != None :
                time.sleep(2.5)
                click(xCloseMbClick, yCloseMbClick)
                print("close mission board")

    if pyautogui.locateOnScreen('submit.png', region=(xSubmit,ySubmit,wSubmit,hSubmit), grayscale=True, confidence=0.8) != None :
            print("1= submit")
            click(xSubmitClick,ySubmitClick)
            time.sleep(2.5)

    if pyautogui.locateOnScreen('check.png', region=(xCheck,yCheck,wCheck,hCheck), grayscale=True, confidence=0.8) != None :
            print("1= check")
            click(xCheckClick,yCheckClick)
            time.sleep(2.5)

    if pyautogui.locateOnScreen('check2.png', region=(xCheck2,yCheck2,wCheck2,hCheck2), grayscale=True, confidence=0.8) != None :
            print("1= check")
            click(xCheckClick2,yCheckClick2)
            time.sleep(2.5)   

    if pyautogui.locateOnScreen('check3.png', region=(xCheck3,yCheck3,wCheck3,hCheck2), grayscale=True, confidence=0.8) != None :
                print("1= check")
                click(xCheckClick3,yCheckClick3)
                time.sleep(2.5)    

    if pyautogui.locateOnScreen('pick.png', region=(xCheck3,yCheck3,wCheck3,hCheck2), grayscale=True, confidence=0.8) != None :
                print("1= pick")
                click(xCheckClick3,yCheckClick3)
                time.sleep(2.5)  
                
    if pyautogui.locateOnScreen('search.png', region=(814,285,77,71), grayscale=True, confidence=0.8) != None :
                print("1= pick")
                click(xCheckClick3,yCheckClick3)
                time.sleep(2.5)                
    
    if pyautogui.locateOnScreen('appeaseBird.png', region=(xAppeaseBird,yAppeaseBird,wAppeaseBird,hAppeaseBird), grayscale=True, confidence=0.8) != None or pyautogui.locateOnScreen('catch.png', region=(xAppeaseBird,yAppeaseBird,wAppeaseBird,hAppeaseBird), grayscale=True, confidence=0.8) != None :
            print("appease bird clicked")
            click(xAppeaseBirdClick,yAppeaseBirdClick)
            time.sleep(2.5)


    if pyautogui.locateOnScreen('handOver.png', region=(xHandOver,yHandOver,wHandOver,hHandOver), grayscale=True, confidence=0.8) != None or  pyautogui.locateOnScreen('handOver2.png', region=(xHandOver,yHandOver,wHandOver,hHandOver), grayscale=True, confidence=0.8) != None or pyautogui.locateOnScreen('handOver3.png', region=(xHandOver,yHandOver,wHandOver,hHandOver), grayscale=True, confidence=0.8) != None or pyautogui.locateOnScreen('handOver4.png', region=(xHandOver,yHandOver,wHandOver,hHandOver), grayscale=True, confidence=0.8) != None :
                print("handOver")
                click(xHandOverClick,yHandOverClick)
                time.sleep(2.5)

    if pyautogui.locateOnScreen('handOverItem.png', region=(xHandOverItem,yHandOverItem,wHandOverItem,hHandOverItem), grayscale=True, confidence=0.8) != None :
                print("handOverItem")
                click(xHandOverClickItem,yHandOverClickItem)
                time.sleep(2.5)

    if pyautogui.locateOnScreen('resurrect.png', region=(xResurrect,yResurrect,wResurrect,hResurrect), grayscale=True, confidence=0.8) != None :
                print("resurrect click")
                click(xResurrectClick,yResurrectClick)
                time.sleep(2.5)