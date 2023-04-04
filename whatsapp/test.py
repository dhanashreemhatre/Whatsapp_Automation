import pyautogui as pg
import time

while True:
    time.sleep(4)
    x,y=pg.position()
    print(x,y)
    
