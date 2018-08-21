#!/usr/bin/python
import boto3
from botocore.exceptions import ClientError
import pandas as pd

pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)


labels = ["Group_Name", "Group_id", "Vpc_id", "Ip_Proto", "Cidr", "To_Port", "From_Port"]

ec2 = boto3.resource('ec2')
groups = list(ec2.security_groups.all())

allrows = []
for gps in groups: 
    row = []
    row.append(gps.group_name)
    row.append(gps.group_id)
    row.append(gps.vpc_id)
    row.append(gps.ip_permissions[0]['IpProtocol'])
    try:
        row.append(gps.ip_permissions[0]['IpRanges'][0]['CidrIp'])
    except IndexError:
        row.append("-")
    try:
        row.append(gps.ip_permissions[0]['ToPort'])
        row.append(gps.ip_permissions[0]['FromPort'])
    except KeyError:
       row.append("-")
    allrows.append(row)

df = pd.DataFrame.from_records(allrows, columns=labels)
df.to_csv('/tmp/ingresrules.csv', header = True, index = True, na_rep = '-')
#df.to_html('/tmp/ingresrules.html')

print df

