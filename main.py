import time
import pyautogui

pyautogui.FAILSAFE = False
while True:
    time.sleep(15)
    for i in range(0, 50):
        pyautogui.moveTo(i * 10, i * 10)
    for i in range(0, 2):
        pyautogui.press('shift')
    for i in range(0, 3):
        pyautogui.press('ctrl')

# print(pyautogui.size())
# time.sleep(2)
# pyautogui.scroll(-7000)
# pyautogui.moveTo(250, 900)