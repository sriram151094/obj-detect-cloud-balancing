#!/usr/bin/python

'''
SETUP:

    -   -->     GND     -->     PIN6
    +   -->     5V      -->     PIN4
    S   -->     GPIO18  -->     PIN12

'''

import RPi.GPIO as GPIO
import subprocess
import time
import sys
from video_recorder import record_video
sensor = 11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor, GPIO.IN)

on = 0
off = 0
while True:
    i=GPIO.input(sensor)
    if i == 0:
        print "No intruders"
        time.sleep(5)
    elif i == 1:
        print "Intruder detected"
	record_video()
        time.sleep(5)
        
