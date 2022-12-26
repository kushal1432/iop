import random
import pyautogui as pg
import time
message=('I love you')
time.sleep(5)
for i in range(200):
    a=random.choice(message)
    pg.write("I love pubg")
    pg.press('Enter')
