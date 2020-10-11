import pyautogui
import time

comments = ["Hi","Just commenting for fun","Challeneg accepted","Just for fun","this is awesome","Do not mess with me"]

time.sleep(5)
var = 1
while var == 1: 
    pyautogui.typewrite(comments[var])
    pyautogui.typewrite("\n")
    time.sleep(2)
