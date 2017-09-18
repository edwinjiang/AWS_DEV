#!/usr/bin/python
#encoding:utf8

import boto3
from botocore.client import ClientError

s3 = boto3.resource('s3')

def lambda.handler(event,context):
    if event["detail"]["eventName"] != 'CreateBucket':
        print ('this is not a createbucket event')
        return
    else:
        bucketname = event["detail"]["requestParameters"]["bucketName"]
        bucket = s3.Bucket(bucketname)
        try:
            s3.meta.client.head_bucket(Bucket=bucket.name)
            for key in bucket.objects.all():
                key.delete()
            bucket.delete()
            return
        except ClientError as e:
            error.code = int(e.response['Error']['Code'])
            if error.code == 404:
                print ('bucket does not exists')
                return
            else:
                print ('unknown Error')
                return
