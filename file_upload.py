#!/usr/bin/env python
# coding: utf-8
import os

from s3_file_uploader import upload_file_to_s3, get_sqs_client
from sys import argv


def upload_files_to_s3(file_path, fname):
    upload_file_to_s3(file_path + '/' + fname, 'outputresultbucket', fname)


if __name__ == '__main__':
    upload_files_to_s3(argv[1], argv[2])
