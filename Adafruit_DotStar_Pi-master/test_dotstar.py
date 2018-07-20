#!/usr/bin/python

#The following is an example LED program that flashes the LEDs in
#random colors.

import time
from dotstar import Adafruit_DotStar
import random

numpixels = 2 # Number of LEDs in strip
strip    = Adafruit_DotStar(numpixels, 12000000)

strip.begin()           # Initialize pins for output
strip.setBrightness(64) # Limit brightness to ~1/4 duty cycle

head  = 0               # First LED in the ball
tail  = 1               # Second LED int the ball
head_color = 0xFF0000   # Color of first LED
tail_color = 0x00FF00   # Color of second LED

while True:
	strip.setPixelColor(head, head_color)
	strip.setPixelColor(tail, tail_color)
	strip.show()                     

        #Delay for a time before the colors switch
	time.sleep(0.4)

        #scroll the color across the two leds in the ball
        #generate a new random color each time (from red to white)
        tail_color = head_color
        head_color = random.randint(255, 16777215)
