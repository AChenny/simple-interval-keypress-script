from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

print("Welcome.\nClose this window to stop the keyboard inputs.")

while (True):
    time.sleep(5)
    keyboard.press('w')
    keyboard.release('w')
    time.sleep(10)
    keyboard.press('s')
    keyboard.release('s')
    
