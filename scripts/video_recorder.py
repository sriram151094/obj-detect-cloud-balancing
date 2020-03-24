#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 18:12:18 2020
@author: srihariravi
"""

import picamera
from sys import argv
import getpass
import time
import subprocess


def record_video():
    username = getpass.getuser()
    file_name = str(time.time()).split(".")[0] + '.h264'
    subprocess.call('raspivid -o /home/' + username + '/videos/tmp/' + file_name + ' -t 5000', shell=True)
    subprocess.call('mv /home/' + username + '/videos/tmp/' + file_name + ' /home/' + username + '/videos/', shell=True)
    # with picamera.PiCamera() as camera:
    #    camera.resolution = (640, 480)
    #    for filename in camera.record_sequence('/home/'+username+'/videos/%s.h264' % str(time.time()).split(".")[0] for i in range(1, 11)):
    #       camera.wait_recording(2)


if __name__ == '__main__':
    record_video()

