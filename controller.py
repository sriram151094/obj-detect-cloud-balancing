# !/usr/bin/env scripts
# coding: utf-8

import random
from s3_file_uploader import get_sqs_client
from sqs_queue import get_queue_length
from ec2_instance_util import get_ec2_client, create_ec2_instances, get_running_ec2_instances, \
    get_all_ec2_instances, get_ec2_resource, start_instances, get_idle_instances

video_path = '/home/pi/recorded_videos'
# video_path = './Videos/'
bucketname = 'videodatainputbucket'

MAX_NO_OF_INSTANCES = 6


def run_object_detection_in_ec2():
    msg_queue = get_sqs_client()
    resource = get_ec2_resource()
    while 1:
        queue_attr = get_queue_length(msg_queue)
        queue_len = int(queue_attr['Attributes']['ApproximateNumberOfMessages'])
        while queue_len > 0:
            # all_instances = get_all_ec2_instances(resource)
            active_instances = get_running_ec2_instances(resource)
            idle_instances = get_idle_instances(resource)

            # total_inst = sum(1 for _ in all_instances)
            num_active_inst = sum(1 for _ in active_instances)
            idle_num = sum(1 for _ in idle_instances)

            if queue_len > MAX_NO_OF_INSTANCES:
                create_ec2_instances(MAX_NO_OF_INSTANCES - num_active_inst - idle_num, resource)
                start_idle_instances(idle_instances, idle_num)
            elif queue_len <= idle_num:
                start_idle_instances(idle_instances, queue_len)
            elif queue_len > idle_num:
                create_ec2_instances(queue_len - idle_num, resource)
                start_idle_instances(idle_instances, idle_num)


def start_idle_instances(idle_ids, no_of_instances):
    if no_of_instances > 0:
        client = get_ec2_client()
        start_instances(random.sample(idle_ids, no_of_instances), client)


if __name__ == '__main__':
    run_object_detection_in_ec2()
