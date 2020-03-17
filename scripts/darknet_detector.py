#!/usr/bin/env python
# coding: utf-8
import os
from s3_file_uploader import upload_file_to_s3


def run_darknet_detector():
    for fname in os.listdir('/home/pi/darknet'):
        if fname.endswith('.h264') or fname.endswith('.mp4'):
            output_file = fname.split(".")[0]
            os.system("rm -rf /home/pi/output_" + output_file + ".txt")
            os.system(
                "./darknet detector demo cfg/coco.data cfg/yolov3-tiny.cfg yolov3-tiny.weights " + fname + " >> "
                "/home/pi/output_" + output_file + ".txt")
            # os.system("rm -rf /home/pi/out.txt")
            #os.system("truncate -s 0 /home/pi/result.txt")
            upload_file_to_s3("/home/pi/output_" + output_file + ".txt", "outputresultbucket", "output_" + output_file + ".txt")
            break
        else:
            print('No')


if __name__ == '__main__':
    run_darknet_detector()