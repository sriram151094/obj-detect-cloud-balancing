#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import boto3


def get_ec2_resource():
    ec2 = boto3.resource('ec2')
    return ec2


def get_ec2_client():
    ec2 = boto3.client('ec2')
    return ec2


def get_s3_client():
    s3 = boto3.client('s3')
    return s3


def get_sqs_client():
    sqs = boto3.client('sqs')
    return sqs
