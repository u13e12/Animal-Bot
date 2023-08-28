import os
import time
import pyautogui
import enum
import random
import threading
import asyncio
import cv2 as cv
import numpy as np
import requests
import pydirectinput


from windowcapture import WindowCapture
from windowmanager import WindowMgr
from vision import Vision


# Change the working directory to the folder this script is in.
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# Global variables
promo = Vision('promo.jpg')
food1 = Vision('food1.jpg')
food2 = Vision('food1.jpg')
food3 = Vision('food1.jpg')
food4 = Vision('food1.jpg')
fish1 = Vision('fish1.jpg')
fish2 = Vision('fish2.jpg')
fish3 = Vision('fish3.jpg')
alright = Vision('alright.jpg')
green = Vision('Green.jpg')
claim = Vision('claim.jpg')
# okorder = Vision('okorder.jpg')

xcord1 = [820, 820, 940, 940, 1070, 1070]
xcord2 = [840, 840, 960, 960, 1090, 1090]
ycord1 = [450, 660, 450, 660, 450, 660]
ycord2 = [480, 690, 480, 690, 480, 690]


def runBot():

    # Change the working directory to the folder this script is in.
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Focus on FFXIV
    w = WindowMgr()
    w.find_window(None, 'BlueStacks 3')
    w.set_foreground()

    # Initialize window capturing and event to compare to
    wincap = WindowCapture('BlueStacks 3')

    while(True):

        timeout = time.time()+3600

        while(True):

            now = time.time()

            screenshot = wincap.get_screenshot()

            botstopper1 = alright.find(
                screenshot, 0.9, 'rectangles')

            botstopper2 = claim.find(
                screenshot, 0.7, 'rectangles')

            emptyline = green.find(
                screenshot, 0.7, 'rectangles')

            if botstopper1:
                target_path = 'alright.jpg'

                target_pos = pyautogui.locateOnScreen(
                    target_path, confidence=.5)
                x, y, w, h = target_pos
                x1 = random.randrange(x, x + w)
                y1 = random.randrange(y, y + h)
                t1 = random.uniform(0.25, 1)

                pyautogui.moveTo(x1, y1, t1, pyautogui.easeOutQuad)
                pyautogui.click()
                time.sleep(1)

            if botstopper2:
                target_path = 'claim.jpg'

                target_pos = pyautogui.locateOnScreen(
                    target_path, confidence=.5)
                x, y, w, h = target_pos
                x1 = random.randrange(x, x + w)
                y1 = random.randrange(y, y + h)
                t1 = random.uniform(0.25, 1)

                pyautogui.moveTo(x1, y1, t1, pyautogui.easeOutQuad)
                pyautogui.click()
                time.sleep(1)

            time.sleep(random.uniform(.1, 2))
            pyautogui.moveTo(random.randint(1150, 1180), random.randint(
                920, 990), 0.05, pyautogui.easeInQuad)
            pyautogui.click(clicks=random.randrange(10, 20), interval=0.2)
            time.sleep(random.uniform(.3, 1))
            pyautogui.moveTo(random.randint(1150, 1180), random.randint(
                920, 990), 0.05, pyautogui.easeInQuad)
            pyautogui.click(clicks=random.randrange(15, 25), interval=0.2)
            time.sleep(random.uniform(.1, 1))
            pyautogui.moveTo(random.randint(1150, 1180), random.randint(
                920, 990), 0.05, pyautogui.easeInQuad)
            pyautogui.click(clicks=random.randrange(10, 25), interval=0.2)
            time.sleep(random.uniform(.1, 1))

            if now > timeout:
                for x1, x2, y1, y2 in zip(xcord1, xcord2, ycord1, ycord2):
                    pyautogui.moveTo(random.randint(xcord1, xcord2), random.randint(
                        ycord1, ycord2), 0.05, pyautogui.easeInQuad)
                    pyautogui.click(
                        clicks=random.randrange(3, 5), interval=0.3)

                    screenshot = wincap.get_screenshot()

                    orderfound = claim.find(
                        screenshot, 0.7, 'rectangles')

                    if botstopper1:
                        target_path = 'alright.jpg'

                        target_pos = pyautogui.locateOnScreen(
                            target_path, confidence=.5)
                        x, y, w, h = target_pos
                        x1 = random.randrange(x, x + w)
                        y1 = random.randrange(y, y + h)
                        t1 = random.uniform(0.25, 1)

                        pyautogui.moveTo(x1, y1, t1, pyautogui.easeOutQuad)
                        pyautogui.click()
                        time.sleep(1)


runBot()
