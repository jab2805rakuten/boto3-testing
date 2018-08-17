# coding: utf-8
vpc = session.resource('vpc')
vpc = session.client('vpc')
vpc = session.client('ec2')
vpc.terminate_instances
ec2_res = boto3.resource('ec2', region_name=eu-central-1)
ec2_res = boto3.resource('ec2', region_name='eu-central-1')
ec2_clnt = boto3.client('ec2', region_name='eu-central-1')
ec2_clnt.terminate_instances('i-0e81267a8dce83095')
ec2.instances.filter(InstanceIds=ids).terminate()
ec2_clnt.instances.filter(InstanceIds='i-0e81267a8dce83095').terminate()
ec2_clnt.instances.filter(InstanceIds='i-0e81267a8dce83095').terminate()
5'
r = ec2_clnt.Instance('i-0e81267a8dce83095')
r = ec2_res.Instance('i-0e81267a8dce83095')
r.terminate()
get_ipython().run_line_magic('save', '03session 1-16')
