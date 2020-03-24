#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from connection_util import get_sqs_client
from sqs_queue import queue_url, get_queue_length
from s3_file_uploader import download_file_from_s3
import subprocess
import getpass

# create a boto3 client
client = get_sqs_client()

while True:
    if get_queue_length(client) > 0:
        messages = client.receive_message(QueueUrl=queue_url)
        print(messages)
        # adjust MaxNumberOfMessages if needed
        # when the queue is exhausted, the response dict contains no 'Messages' key
        if len(messages) > 0 and 'Messages' in messages:
            message = messages['Messages'][0]
            # Process the messages
            print(message['Body'])
            bucket = json.loads(message['Body'])['bucketId']
            filename = json.loads(message['Body'])['fileName']
            username = getpass.getuser()
            download_file_from_s3(bucket, filename, '/home/' + username + '/videos/downloaded_videos')

            # Call shell script to run darknet detector
            #subprocess.call(['echo "/home/pi/scripts/detector.sh >> /home/pi/log.txt"'])
            subprocess.call(['/home/pi/scripts/detector.sh'])

            # Next, we delete the message from the queue so no one else will process it again
            client.delete_message(QueueUrl=queue_url, ReceiptHandle=message['ReceiptHandle'])