#!/bin/bash
#exec 3>&1 4>&2
#trap 'exec 2>&4 1>&3' 0 1 2 3
#exec 1>log.out 2>&1
user=$(whoami)
cd /home/${user}/darknet
Xvfb :1 & export DISPLAY=:1
pwd
direct="/home/${user}/videos/*"
mkdir -p /home/${user}/processed
for fname in $direct
do
        echo "Full filename: $fname"
        proccessed=$(b=${fname##*/}; echo ${b%.*})
        echo "/home/${user}/output_${proccessed}"
        echo "Processed filename: ${fname##*/}"
	if [[ $fname == *.h264 ]]
	then
                echo "Darknet command running"
                pwd
		./darknet detector demo cfg/coco.data cfg/yolov3-tiny.cfg yolov3-tiny.weights $fname >> /home/${user}/output_${proccessed}.txt
                mv $fname /home/${user}/processed
                rm -rf $fname
                scripts /home/${user}/scripts/file_upload.py /home/${user} output_${proccessed}.txt
                echo "Processed and moved"
	fi
done
