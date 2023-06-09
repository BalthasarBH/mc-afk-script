from time import sleep
import random
import keyboard
import sys

global stop
global warten
global pause
stop = False
# Diese Werte dürfen verändert werden
warten = random
pause = random.randrange(6)
# - - - - - - - - - - - - - - - - - -
def afkscript():
    while True:
        if stop == False:
            auswahl = random.randrange(6)
            sleep(pause)
            if auswahl.__int__() == 1:  # W
                keyboard.press('w')
                sleep(warten)
                keyboard.press('s')

            elif auswahl.__int__() == 2:  # A
                keyboard.press('a')
                sleep(warten)
                keyboard.press('d')

            elif auswahl.__int__() == 3:  # S
                keyboard.press('s')
                sleep(warten)
                keyboard.press('w')

            elif auswahl.__int__() == 4:  # D
                keyboard.press('d')
                sleep(warten)
                keyboard.press('a')

            elif auswahl.__int__() == 5:  # SPACE
                keyboard.press('space')
        elif stop == True:
            print("Danke das du mein Script benutzt :D")
            print("Komm auf mein Discord ;D")
            print("https://discord.gg/4PJysZcUVT")
            keyboard.wait('enter')
            sys.exit()
              # Stattdessen von exit() zu sys.exit() wechseln

def stop_script():
    global stop
    stop = True

print("Drücke ENTER zum starten")
print("Um das Script zu stoppen, drücke Q")
keyboard.add_hotkey('q', stop_script)  # Füge die Funktion stop_script() hinzu
keyboard.wait('enter')
print("Los geht's!")
afkscript()