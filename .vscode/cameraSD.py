import camera
import machine
import os
import uos
#import time
from machine import RTC


#init hardware
rtc= RTC()
rtc.init((2020,10,1,0,16,30,0,0))

uos.mount(machine.SDCard(), "/sd")

count= 0

listDirectory  = os.listdir('/sd')

camera.init(0, format=camera.JPEG)
camera.framesize(camera.FRAME_QVGA)

print('camera ready')

while count <= 50:
    timeStamp=rtc.datetime()
    name= str(timeStamp[0])+str(timeStamp[1])+str(timeStamp[2])+str(timeStamp[4])+str(timeStamp[5])+str(timeStamp[6])
    picture = open('/sd/'+name+'.jpg', 'w+b')  
    picture.write(camera.capture())
    picture.close()    
    print('took image '+ str(count))
    count+=1
    machine.sleep(1000)
else:
    machine.deepsleep()

