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
flowertable = Vision('flowertable.jpg')
sow = Vision('Sow.jpg')
ok = Vision('ok.jpg')
line = Vision('rest1.jpg')
restaurant = Vision('Inrestaurant.jpg')
flower1 = Vision('daisy.jpg')
flower2 = Vision('sunflower.jpg')
flower3 = Vision('rose.jpg')
flower4 = Vision('bluebell.jpg')


xcord1 = [820, 820, 940, 940, 1070, 1070]
xcord2 = [840, 840, 960, 960, 1090, 1090]
ycord1 = [460, 630, 460, 630, 460, 630]
ycord2 = [480, 660, 480, 660, 480, 660]

operation1LastRanAt = time.time()-60*(80-75)
operation2LastRanAt = time.time()-60*(120-4)
operation3LastRanAt = time.time()-60*(200-68)
operation4LastRanAt = time.time()-60*(320-177)
operation5LastRanAt = time.time()
print("starttime " + time.ctime())

timer1 = 80*60
timer2 = 120*60
timer3 = 200*60
timer4 = 320*60
timer5 = 60*10


def runBot():

    # Change the working directory to the folder this script is in.
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Focus on FFXIV
    w = WindowMgr()
    w.find_window(None, 'BlueStacks 1')
    w.set_foreground()

    # Initialize window capturing and event to compare to
    wincap = WindowCapture('BlueStacks 1')

    while(True):

        global operation1LastRanAt
        global operation2LastRanAt
        global operation3LastRanAt
        global operation4LastRanAt
        global operation5LastRanAt

        screenshot = wincap.get_screenshot()

        botstopper1 = alright.find(
            screenshot, 0.8, 'rectangles')

        orderfound = claim.find(
            screenshot, 0.8, 'rectangles')

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

        if orderfound:
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

        pyautogui.moveTo(random.randint(1150, 1180), random.randint(
            920, 990), 0.05, pyautogui.easeInQuad)
        pyautogui.click(clicks=random.randrange(10, 25), interval=0.2)
        time.sleep(random.uniform(.3, 1))
        pyautogui.moveTo(random.randint(1150, 1180), random.randint(
            920, 990), 0.05, pyautogui.easeInQuad)
        pyautogui.click(clicks=random.randrange(15, 25), interval=0.2)
        time.sleep(random.uniform(.3, 1))
        pyautogui.moveTo(random.randint(1150, 1180), random.randint(
            920, 990), 0.05, pyautogui.easeInQuad)
        pyautogui.click(clicks=random.randrange(10, 25), interval=0.2)
        time.sleep(random.uniform(.3, 1))

        if operation5LastRanAt + timer5 <= time.time():
            for xx1, xx2, yy1, yy2 in zip(xcord1, xcord2, ycord1, ycord2):
                pyautogui.moveTo(random.randint(xx1, xx2), random.randint(
                    yy1, yy2), 0.05, pyautogui.easeInQuad)
                pyautogui.click(
                    clicks=random.randrange(4, 5), interval=0.3)

                screenshot = wincap.get_screenshot()

                time.sleep(1)

                orderaccept = ok.find(
                    screenshot, 0.7, 'rectangles')

                botstopper1 = alright.find(screenshot, 0.8, 'rectangles')

                orderfound = claim.find(
                    screenshot, 0.8, 'rectangles')

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

                if orderfound:
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

                if orderaccept:
                    target_path = 'ok.jpg'

                    target_pos = pyautogui.locateOnScreen(
                        target_path, confidence=.5)
                    x, y, w, h = target_pos
                    x1 = random.randrange(x, x + w)
                    y1 = random.randrange(y, y + h)
                    t1 = random.uniform(0.25, 1)

                    pyautogui.moveTo(x1, y1, t1, pyautogui.easeOutQuad)
                    pyautogui.click()
                    print(5, time.ctime())
                    time.sleep(1)

            operation5LastRanAt = time.time()

        # daisy

        if operation1LastRanAt + timer1 <= time.time():

            # navigate to garden

            while(True):
                screenshot = wincap.get_screenshot()
                inRestaurant = restaurant.find(screenshot, 0.8, 'rectangles')
                inGarden = flowertable.find(screenshot, 0.7, 'rectangles')

                if inRestaurant:
                    pyautogui.moveTo(random.randint(676, 699), random.randint(
                        522, 550), 0.05, pyautogui.easeInQuad)
                    pyautogui.click()
                    time.sleep(random.uniform(1, 1.5))

                if inGarden:
                    break

            # havest loop

            while(True):
                screenshot = wincap.get_screenshot()
                prompt = sow.find(screenshot, 0.7, 'rectangles')

                botstopper1 = alright.find(screenshot, 0.8, 'rectangles')

                orderfound = claim.find(
                    screenshot, 0.8, 'rectangles')

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

                if orderfound:
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

                if not prompt:

                    # harvest
                    pyautogui.moveTo(random.randint(820, 850), random.randint(
                        450, 490), 0.05, pyautogui.easeInQuad)
                    pyautogui.click()
                    time.sleep(random.uniform(1, 1.5))

                    # place
                    screenshot = wincap.get_screenshot()

                    hDaisy = flower1.find(screenshot, 0.6, 'rectangles')

                    if hDaisy:
                        target_path = 'daisy.jpg'

                        target_pos = pyautogui.locateOnScreen(
                            target_path, confidence=.5)
                        x, y, w, h = target_pos
                        x1 = random.randrange(x, x + w)
                        y1 = random.randrange(y, y + h)
                        t1 = random.uniform(0.25, 1)

                        pyautogui.moveTo(x1, y1, t1, pyautogui.easeOutQuad)
                        pyautogui.click()
                        time.sleep(1)

                    # plant
                    pyautogui.moveTo(random.randint(820, 850), random.randint(
                        450, 490), 0.05, pyautogui.easeInQuad)
                    pyautogui.click()
                    time.sleep(random.uniform(1, 1.5))

                if prompt:
                    target_path = 'sow.jpg'

                    target_pos = pyautogui.locateOnScreen(
                        target_path, confidence=.5)
                    x, y, w, h = target_pos
                    x1 = random.randrange(x, x + w)
                    y1 = random.randrange(y, y + h)
                    t1 = random.uniform(0.25, 1)

                    pyautogui.moveTo(x1, y1, t1, pyautogui.easeOutQuad)
                    pyautogui.click()
                    time.sleep(1)
                    break

            # navigate to restaurant

            while(True):
                screenshot = wincap.get_screenshot()
                time.sleep(1)
                inGarden = flowertable.find(screenshot, 0.7, 'rectangles')
                inRestaurant = restaurant.find(screenshot, 0.8, 'rectangles')

                if inGarden:
                    pyautogui.moveTo(random.randint(1185, 1200), random.randint(
                        522, 550), 0.05, pyautogui.easeInQuad)

                    pyautogui.click()
                    time.sleep(1)

                if inRestaurant:
                    break

            operation1LastRanAt = time.time()
            print(1, time.ctime())

        # sunflower

        if operation2LastRanAt + timer2 <= time.time():

            # navigate to garden

            while(True):
                screenshot = wincap.get_screenshot()
                time.sleep(1)
                inRestaurant = restaurant.find(screenshot, 0.8, 'rectangles')
                inGarden = flowertable.find(screenshot, 0.7, 'rectangles')

                if inRestaurant:
                    pyautogui.moveTo(random.randint(676, 699), random.randint(
                        522, 550), 0.05, pyautogui.easeInQuad)
                    pyautogui.click()
                    time.sleep(random.uniform(1, 1.5))

                if inGarden:
                    break

            # havest

            while(True):
                screenshot = wincap.get_screenshot()
                prompt = sow.find(screenshot, 0.7, 'rectangles')

                botstopper1 = alright.find(screenshot, 0.8, 'rectangles')

                orderfound = claim.find(
                    screenshot, 0.8, 'rectangles')

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

                if orderfound:
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

                if not prompt:

                    # harvest
                    pyautogui.moveTo(random.randint(1035, 1060), random.randint(
                        450, 490), 0.05, pyautogui.easeInQuad)
                    pyautogui.click()
                    time.sleep(random.uniform(1, 1.5))

                    # place in vase
                    screenshot = wincap.get_screenshot()

                    hSunflower = flower2.find(screenshot, 0.6, 'rectangles')

                    if hSunflower:
                        target_path = 'sunflower.jpg'

                        target_pos = pyautogui.locateOnScreen(
                            target_path, confidence=.5)
                        x, y, w, h = target_pos
                        x1 = random.randrange(x, x + w)
                        y1 = random.randrange(y, y + h)
                        t1 = random.uniform(0.25, 1)

                        pyautogui.moveTo(x1, y1, t1, pyautogui.easeOutQuad)
                        pyautogui.click()
                        time.sleep(1)

                    # plant
                    pyautogui.moveTo(random.randint(1035, 1060), random.randint(
                        450, 490), 0.05, pyautogui.easeInQuad)
                    pyautogui.click()
                    time.sleep(random.uniform(1, 1.5))

                if prompt:
                    target_path = 'sow.jpg'

                    target_pos = pyautogui.locateOnScreen(
                        target_path, confidence=.5)
                    x, y, w, h = target_pos
                    x1 = random.randrange(x, x + w)
                    y1 = random.randrange(y, y + h)
                    t1 = random.uniform(0.25, 1)

                    pyautogui.moveTo(x1, y1, t1, pyautogui.easeOutQuad)
                    pyautogui.click()
                    time.sleep(1)
                    break

            # navigate to restaurant

            while(True):
                screenshot = wincap.get_screenshot()
                time.sleep(1)
                inGarden = flowertable.find(screenshot, 0.7, 'rectangles')
                inRestaurant = restaurant.find(screenshot, 0.8, 'rectangles')

                if inGarden:
                    pyautogui.moveTo(random.randint(1185, 1200), random.randint(
                        522, 550), 0.05, pyautogui.easeInQuad)

                    pyautogui.click()
                    time.sleep(1)

                if inRestaurant:
                    break

            operation2LastRanAt = time.time()
            print(2, time.ctime())

        # rose

        if operation3LastRanAt + timer3 <= time.time():

            # navigate to garden

            while(True):
                screenshot = wincap.get_screenshot()
                time.sleep(1)
                inRestaurant = restaurant.find(screenshot, 0.8, 'rectangles')
                inGarden = flowertable.find(screenshot, 0.7, 'rectangles')

                if inRestaurant:
                    pyautogui.moveTo(random.randint(676, 699), random.randint(
                        522, 550), 0.05, pyautogui.easeInQuad)
                    pyautogui.click()
                    time.sleep(random.uniform(1, 1.5))

                if inGarden:
                    break

            # havest loop

            while(True):
                screenshot = wincap.get_screenshot()
                prompt = sow.find(screenshot, 0.7, 'rectangles')

                botstopper1 = alright.find(screenshot, 0.8, 'rectangles')

                orderfound = claim.find(
                    screenshot, 0.8, 'rectangles')

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

                if orderfound:
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

                if not prompt:

                    # harvest
                    pyautogui.moveTo(random.randint(820, 850), random.randint(
                        600, 640), 0.05, pyautogui.easeInQuad)
                    pyautogui.click()
                    time.sleep(random.uniform(1, 1.5))

                    # place
                    screenshot = wincap.get_screenshot()

                    hRose = flower3.find(screenshot, 0.6, 'rectangles')

                    if hRose:
                        target_path = 'rose.jpg'

                        target_pos = pyautogui.locateOnScreen(
                            target_path, confidence=.5)
                        x, y, w, h = target_pos
                        x1 = random.randrange(x, x + w)
                        y1 = random.randrange(y, y + h)
                        t1 = random.uniform(0.25, 1)

                        pyautogui.moveTo(x1, y1, t1, pyautogui.easeOutQuad)
                        pyautogui.click()
                        time.sleep(1)

                    # plant
                    pyautogui.moveTo(random.randint(820, 850), random.randint(
                        600, 640), 0.05, pyautogui.easeInQuad)
                    pyautogui.click()
                    time.sleep(random.uniform(1, 1.5))

                if prompt:
                    target_path = 'sow.jpg'

                    target_pos = pyautogui.locateOnScreen(
                        target_path, confidence=.5)
                    x, y, w, h = target_pos
                    x1 = random.randrange(x, x + w)
                    y1 = random.randrange(y, y + h)
                    t1 = random.uniform(0.25, 1)

                    pyautogui.moveTo(x1, y1, t1, pyautogui.easeOutQuad)
                    pyautogui.click()
                    time.sleep(1)
                    break

            # navigate to restaurant

            while(True):
                screenshot = wincap.get_screenshot()
                time.sleep(1)
                inGarden = flowertable.find(screenshot, 0.7, 'rectangles')
                inRestaurant = restaurant.find(screenshot, 0.8, 'rectangles')

                if inGarden:
                    pyautogui.moveTo(random.randint(1185, 1200), random.randint(
                        522, 550), 0.05, pyautogui.easeInQuad)

                    pyautogui.click()
                    time.sleep(1)

                if inRestaurant:
                    break

            operation3LastRanAt = time.time()
            print(3, time.ctime())

        # bluebell

        if operation4LastRanAt + timer4 <= time.time():

            # navigate to garden

            while(True):
                screenshot = wincap.get_screenshot()
                time.sleep(1)
                inRestaurant = restaurant.find(screenshot, 0.8, 'rectangles')
                inGarden = flowertable.find(screenshot, 0.7, 'rectangles')

                if inRestaurant:
                    pyautogui.moveTo(random.randint(676, 699), random.randint(
                        522, 550), 0.05, pyautogui.easeInQuad)
                    pyautogui.click()
                    time.sleep(random.uniform(1, 1.5))

                if inGarden:
                    break

            # havest

            while(True):
                screenshot = wincap.get_screenshot()
                prompt = sow.find(screenshot, 0.7, 'rectangles')

                botstopper1 = alright.find(screenshot, 0.8, 'rectangles')

                orderfound = claim.find(
                    screenshot, 0.8, 'rectangles')

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

                if orderfound:
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

                if not prompt:

                    # harvest
                    pyautogui.moveTo(random.randint(1035, 1060), random.randint(
                        600, 640), 0.05, pyautogui.easeInQuad)
                    pyautogui.click()
                    time.sleep(random.uniform(1, 1.5))

                    # place in vase
                    screenshot = wincap.get_screenshot()

                    hBluebell = flower4.find(screenshot, 0.6, 'rectangles')

                    if hBluebell:
                        target_path = 'bluebell.jpg'

                        target_pos = pyautogui.locateOnScreen(
                            target_path, confidence=.5)
                        x, y, w, h = target_pos
                        x1 = random.randrange(x, x + w)
                        y1 = random.randrange(y, y + h)
                        t1 = random.uniform(0.25, 1)

                        pyautogui.moveTo(x1, y1, t1, pyautogui.easeOutQuad)
                        pyautogui.click()
                        time.sleep(1)

                    # plant
                    pyautogui.moveTo(random.randint(1035, 1060), random.randint(
                        600, 640), 0.05, pyautogui.easeInQuad)
                    pyautogui.click()
                    time.sleep(random.uniform(1, 1.5))

                if prompt:
                    target_path = 'sow.jpg'

                    target_pos = pyautogui.locateOnScreen(
                        target_path, confidence=.5)
                    x, y, w, h = target_pos
                    x1 = random.randrange(x, x + w)
                    y1 = random.randrange(y, y + h)
                    t1 = random.uniform(0.25, 1)

                    pyautogui.moveTo(x1, y1, t1, pyautogui.easeOutQuad)
                    pyautogui.click()
                    time.sleep(1)
                    break

            # navigate to restaurant

            while(True):
                screenshot = wincap.get_screenshot()
                time.sleep(1)
                inGarden = flowertable.find(screenshot, 0.7, 'rectangles')
                inRestaurant = restaurant.find(screenshot, 0.8, 'rectangles')

                if inGarden:
                    pyautogui.moveTo(random.randint(1185, 1200), random.randint(
                        522, 550), 0.05, pyautogui.easeInQuad)

                    pyautogui.click()
                    time.sleep(1)

                if inRestaurant:
                    break

            operation4LastRanAt = time.time()
            print(4, time.ctime())


runBot()
