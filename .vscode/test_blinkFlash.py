from machine import Pin
import time

p = Pin(4, Pin.OUT)

def toogle(max):
    lap = 0

    while lap < max:
        p.value(1)
        time.sleep(1)
        p.value(0)
        time.sleep(1)
        lap += 1

toogle(5)

