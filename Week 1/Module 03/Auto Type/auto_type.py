# if your system did not have auto gui packege then this code work
# install coment: pip install PyAutoGUI
import pyautogui
from time import sleep
sleep(5)
for i in range(0,3):
    pyautogui.write("Name Md Al Amin", interval=0.25)
    pyautogui.press('enter')



