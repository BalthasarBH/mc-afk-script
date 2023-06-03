from time import sleep
import random
from pyautogui import press
def afkscript():
    while True:
        nummer = random.randrange(5)
        randomzeit = random.randrange(4)
        sleep(randomzeit)
        if nummer.__int__() == 1:
            press('w')
            break
        elif nummer.__int__() == 2:
            press('a')
            break
        elif nummer.__int__() == 3:
            press('s')
            break
        elif nummer.__int__() == 4:
            press('d')
            break
        elif nummer.__int__() == 5:
            press('space')
            break
print("Script startet in 10 sekunden!!!")
sleep(12)
