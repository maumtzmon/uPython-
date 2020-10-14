import camera
from machine import Pin
import time

# ESP32-CAM (default configuration) - https://bit.ly/2Ndn8tN
p = Pin(4,Pin.OUT)
p.value(1)
time.sleep(0.5)
p.value(0)

camera.init(0, format=camera.JPEG)  
buf = None
# M5Camera (Version B) - https://bit.ly/317Xb74
#camera.init(0, d0=32, d1=35, d2=34, d3=5, d4=39, d5=18, d6=36, d7=19, format=camera.JPEG, xclk_freq=camera.XCLK_10MHz, href=26, vsync=25, reset=15, sioc=23, siod=22, xclk=27, pclk=21)

# # These parameters: format=camera.JPEG, xclk_freq=camera.XCLK_10MHz are standard for both cameras.
# # You can try using a faster xclk (20MHz), this also worked with the esp32-cam and m5camera 
# # but the image was pixelated and somehow green.

buf = camera.capture()

if buf != None:
    while True:
        p.value(1)
        time.sleep(1)
        p.value(0)
        time.sleep(2)
elif buf == None:
    while True:
        p.value(1)
        time.sleep(0.2)
        p.value(0)
        time.sleep(0.2)
        p.value(1)
        time.sleep(0.2)
        p.value(0)
        time.sleep(0.2)
        p.value(1)
        time.sleep(0.2)
        p.value(0)
        time.sleep(2)
else:
    while True:
        p.value(1)
        time.sleep(0.1)
        p.value(0)
        time.sleep(0.1)
        p.value(1)
        time.sleep(0.1)
        p.value(0)
        time.sleep(2)