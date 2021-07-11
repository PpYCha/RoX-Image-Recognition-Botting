#This script saves the image of the region 660,350,600,400 as savedimage.png in the path "C:\Users\Antec\Desktop\Tutorial\savedimage.png" C:\Users\Mew\source\repos\Image-Recognition-Botting-Tutorial

import pyautogui

im1 = pyautogui.screenshot(region=(762,300,78,70))
im1.save(r"./gathering.png")
