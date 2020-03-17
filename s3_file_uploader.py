import os
import shutil
import re
import sys

from botocore.exceptions import ClientError
from sqs_queue import send_msg
from connection_util import get_s3_client, get_sqs_client


video_path = '/home/pi/recorded_videos'
#video_path = '../Videos/'
bucketname = 'videodatainputbucket'


def move_video(filename):
    shutil.move(video_path + '/' + filename, video_path + '/processed/' + filename)
    return


def download_file_from_s3(bucket_id, file_name, path):
        s3 = get_s3_client()
        s3.download_file(bucket_id, file_name, path + '/' + file_name)


def upload_file_to_s3(path, bucket_name, file_name):
    s3 = get_s3_client()
    res = s3.upload_file(path, bucket_name, file_name)
    return res


def process_videos():
    # Get files from the folder to upload to S3
    files = os.listdir(video_path)
    regex = re.compile(r'.*\.h264')
    files_to_upload = list(filter(regex.search, files))
    print(files_to_upload)
    sqs = get_sqs_client()
    if len(files_to_upload) == 0:
        print("No files to upload")
    else:
        for file in files_to_upload:
            try:
                response = upload_file_to_s3(video_path + '/' + file, bucketname, file)
                print(response)
                # Move the video to the processed folder
                move_video(file)

                # Send message to SQS queue
                send_msg(sqs, file, bucketname)

            except ClientError as e:
                print("Error uploading file")


if __name__ == '__main__':
    process_videos()