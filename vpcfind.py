#!/usr/bin/python3.6


import boto3

response = ec2.describe_regions()
region_list = []
for r in (response['Regions']):
    region_list.append(r['RegionName'])

def allvpc(region):
   vpc _res = boto3.resource('vpc', region_name=region)
    for i in ec2_res.instances.all():
        print ('----- {} ----'.format(region))
        print (i.tags)
        print (i.id)



for r in region_list:
    allvpc(r)
    




