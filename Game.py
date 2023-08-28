import pyautogui
import cv2 as cv
import time
import random
import os
import json

pyautogui.FAILSAFE = True


def main():
    start_game()


def start_game():

    script_dir = os.path.dirname(__file__)
    print(script_dir)
    target_path = os.path.join(script_dir, 'targets', 'fish1.png')
    print(target_path)
    target = cv.imread(target_path, cv.IMREAD_UNCHANGED)

    target_pos = pyautogui.locateOnScreen(
        target_path, confidence=.8)
    target_center = pyautogui.locateCenterOnScreen(target_path)
    print(target_pos)
    print(target_center)
    x, y, w, h = target_pos

    x1 = random.randrange(x, x + w)
    y1 = random.randrange(y, y + h)
    t1 = random.uniform(0.25, 1)

    pyautogui.moveTo(x1, y1, t1, pyautogui.easeOutQuad)
    pyautogui.click()
    time.sleep(.5)


if __name__ == "__main__":
    main()
