#!/usr/bin/env python3.7 



import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_regions()
region_list = []
for r in (response['Regions']):
    region_list.append(r['RegionName'])

response = ec2.describe_availability_zones()



def allinstances(region):
    ec2_res = boto3.resource('ec2', region_name=region)
    for i in ec2_res.instances.all():
        print ('----- {} ----'.format(region))
        print (i.state)
        print (i.vpc)
        print (i.vpc)
        print (i.key_name)
        print (i.instance_type)
        print (i.tags)
        print (i.id)
        print (i.instance_id)



for r in region_list:
    allinstances(r)
    




#attach_volume', 'block_device_mappings', 'classic_address', 'client_token', 'console_output', 'cpu_options', 'create_image', 'create_tags', 'delete_tags', 'describe_attribute', 'detach_classic_link_vpc', 'detac', 'modify_attribute', 'monitor', 'monitoring', 'network_interfaces', 'network_interfaces_attribute', 'password_data', 'placement', 'placement_grouph_volume', 'ebs_optimized', 'elastic_gpu_associations', 'ena_support', 'get_available_subresources', 'hypervisor', 'iam_instance_profile', 'id', 'image', 'image_id', 'instance_id', 'instance_lifecycle', 'instance_type', 'kernel_id', 'key_name', 'key_pair', 'launch_time', 'load', 'meta', 'modify_attribute', 'monitor', 'monitoring', 'network_interfaces', 'network_interfaces_attribute', 'password_data', 'placement', 'placement_group', 'platform', 'private_dns_name', 'private_ip_address', 'product_codes', 'public_dns_name', 'public_ip_address', 'ramdisk_id', 'reboot', 'reload', 'report_status', 'reset_attribute', 'reset_kernel', 'reset_ramdisk', 'reset_source_dest_check', 'root_device_name', 'root_device_type', 'security_groups', 'source_dest_check', 'spot_instance_request_id', 'sriov_net_support', 'start', 'state', 'state_reason', 'state_transition_reason', 'stop', 'subnet', 'subnet_id', 'tags', 'terminate', 'unmonitor', 'virtualization_type', 'volumes', 'vpc', 'vpc_addresses', 'vpc_id', 'wait_until_exists', 'wait_until_running', 'wait_until_stopped', 'wait_until_terminated']
