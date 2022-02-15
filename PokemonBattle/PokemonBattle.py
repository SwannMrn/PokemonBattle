import time
import numpy as np
import sys
import pokedex as pok

# delay printing (like in pokemon games)
def delay_print(s: str):
    # prints one char at a time
    for char in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)

class Pokemon:
    def __init__(self, name, EVs, health='==================='):
        # save variables as attributes
        self.name = name
        self.types = ''
