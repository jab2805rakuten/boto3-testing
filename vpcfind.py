#!/usr/bin/python3.6
import boto3


ec2_res = boto3.resource('ec2', region_name='us-east-1')
ec2_clnt = boto3.client('ec2')

#print (dir(ec2_clnt))
response = ec2_clnt.describe_vpcs()
for r in response["ResponseMetadata"]:
    print (r)
print ("--------------------------------------------------------------")

for r in response["Vpcs"]:
    print (r["CidrBlock"])
    print (r["VpcId"])
    print (r)
    print ("--------------------------------------------------------------")

print ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--------------------------------------------------------------")

for vpc  in ec2_res.vpcs.all():
     print (vpc)
     for sub in vpc.subnets.all():
         print (vpc, "all", sub)


#for e in dir(ec2_res):
#    print (e)
#
#v = ec2_res.vpcs

#print (v)
#response = ec2.describe_regions()
#region_list = []
#for r in (response['Regions']):
#    region_list.append(r['RegionName'])


    

##def allvpc(region):
#   vpc _res = boto3.resource('vpc', region_name=region)
#   for i in ec2_res.instances.all():
#        print ('----- {} ----'.format(region))
#        print (i.tags)
#        print (i.id)


#
#for r in region_list:
#    allvpc(r)
    




