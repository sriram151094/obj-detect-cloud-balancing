#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import picamera
import time

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    for filename in camera.record_sequence('/home/pi/recorded_videos/%s.h264' % str(time.time()).split(".")[0] for i in range(1, 11)):
        camera.wait_recording(5)