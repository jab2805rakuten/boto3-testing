# coding: utf-8
import boto3
session = boto3.Session(profile_name='jbrewster')
s3 = session.resource('s3')
ec2_clnt = session.client('ec2')
