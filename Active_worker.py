# requirement - pip install pyautogui

import pyautogui
import time

while True:
    #move your cursor 10 pixels
    pyautogui.moveRel(0, 10)

    # pauses your code from running for 2 seconds
    time.sleep(2)