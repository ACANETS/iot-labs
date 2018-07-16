 #!/usr/bin/env python

'''

example code of GPIO operation on Pi Zero W

Reference: https://medium.freecodecamp.org/hello-gpio-blinking-led-using-raspberry-pi-zero-wh-65af81718c14

'''

from gpiozero import LED 
from time import sleep

led = LED(25)
while True: 
    led.on() 
    sleep(1)
    led.off() 
    sleep(1)
