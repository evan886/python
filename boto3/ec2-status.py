import  boto3
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_instance_status.html
import schedule
ec2_client = boto3.client('ec2',region_name="eu-central-1")
ec2_resource = boto3.resource('ec2',region_name="eu-central-1")
print('start')
def check_instance_status():
    statuses = ec2_client.describe_instance_status(
        IncludeAllInstances=True
    )
    for status in statuses['InstanceStatuses']:
        ins_status = status['InstanceStatus']['Status']
        sys_status = status['SystemStatus']['Status']
        state = status['InstanceState']['Name']
        print(
            f"Instance {status['InstanceId']}  is {state} with status is {ins_status} and  system status is  {sys_status}")

# schedule.every(5).minutes.do(check_instance_staus)
schedule.every(5).seconds.do(check_instance_status)
# schedule.every().day.at("1:00")
while True:
    schedule.run_pending()

""" 
reservations  = ec2_client.describe_instances()
for  reservation in reservations['Reservations']:
     instances = reservation['Instances']
     for instance in instances:
         print(f" Status of instance {instance['InstanceId']} is:    {instance['State']['Name']}")
         #print(instance['InstanceId'])
    # print(reservation['Instances'])
 """
# statuses = ec2_client.describe_instance_status()
# for status   in statuses['InstanceStatuses']:
#     ins_status = status['InstanceStatus']['Status']
#     sys_status = status['SystemStatus']['Status']
#     state = status['InstanceState']['Name']
#     print(f"Instance {status['InstanceId']}  is {state} with status is {ins_status} and  system status is  {sys_status}")

'''
Instance i-0f0cda6215959df27  is running with status is ok and  system status is  ok
Instance i-032d0021299aed717  is running with status is ok and  system status is  ok
  
specific

Instance i-0f0cda6215959df27  is {'Code': 16, 'Name': 'running'} with status is ok and  system status is  ok
Instance i-032d0021299aed717  is {'Code': 16, 'Name': 'running'} with status is ok and  system status is  ok

'''

# Instance i-0f0cda6215959df27 status is ok and  system status is  ok
# Instance i-032d0021299aed717 status is ok and  system status is  ok

#describe_instance_status separately

 # Status of instance i-060ea3ed5dcf78277 is:           running
 # Status of instance i-0f0cda6215959df27 is:           running
 # Status of instance i-032d0021299aed717 is:           running

# Status of instance i-060ea3ed5dcf78277 is:    shutting-down
#  Status of instance i-0f0cda6215959df27 is:    running
#  Status of instance i-032d0021299aed717 is:    running

# /home/evan/data/github/python/devops /.venv/boto3/bin/python" /home/evan/data/github/python/boto3/ec2-status.py
# [{'Architecture': 'x86_64', 'BlockDeviceMappings': [{'DeviceName': '/dev/xvda', 'Ebs': {'AttachTime': datetime.datetime(2026, 2, 8, 6, 47, 20, tzinfo=tzutc()), 'DeleteOnTermination': True, 'Status': 'attached', 'VolumeId': 'vol-0a3e265b410c8111e', 'EbsCardIndex': 0}}], 'ClientToken': 'terraform-20260208064718566500000003', 'EbsOptimized': False, 'EnaSupport': True, 'Hypervisor': 'xen', 'NetworkInterfaces': [{'Association': {'IpOwnerId': 'amazon', 'PublicDnsName': '', 'PublicIp': '63.180.218.215'}, 'Attachment': {'AttachTime': datetime.datetime(2026, 2, 8, 6, 47, 19, tzinfo=tzutc()), 'AttachmentId': 'eni-attach-00e90d7d1cfd5f184', 'DeleteOnTermination': True, 'DeviceIndex': 0, 'Status': 'attached', 'NetworkCardIndex': 0}, 'Description': '', 'Groups': [{'GroupId': 'sg-0bfd86e38a79bb03c', 'GroupName': 'myapp-sg'}], 'Ipv6Addresses': [], 'MacAddress': '02:cc:4b:f8:98:6d', 'NetworkInterfaceId': 'eni-0953ffeacc518647e', 'OwnerId': '092611985600', 'PrivateIpAddress': '10.0.10.221', 'PrivateIpAddresses': [{'Association': {'IpOwnerId': 'amazon', 'PublicDnsName': '', 'PublicIp': '63.180.218.215'}, 'Primary': True, 'PrivateIpAddress': '10.0.10.221'}], 'SourceDestCheck': True, 'Status': 'in-use', 'SubnetId': 'subnet-05c1eec666d443fe4', 'VpcId': 'vpc-0a72063c7e93184b5', 'InterfaceType': 'interface', 'Operator': {'Managed': False}}], 'RootDeviceName': '/dev/xvda', 'RootDeviceType': 'ebs', 'SecurityGroups': [{'GroupId': 'sg-0bfd86e38a79bb03c', 'GroupName': 'myapp-sg'}], 'SourceDestCheck': True, 'Tags': [{'Key': 'Name', 'Value': 'dev-server-three'}], 'VirtualizationType': 'hvm', 'CpuOptions': {'CoreCount': 1, 'ThreadsPerCore': 1}, 'CapacityReservationSpecification': {'CapacityReservationPreference': 'open'}, 'HibernationOptions': {'Configured': False}, 'MetadataOptions': {'State': 'applied', 'HttpTokens': 'optional', 'HttpPutResponseHopLimit': 1, 'HttpEndpoint': 'enabled', 'HttpProtocolIpv6': 'disabled', 'InstanceMetadataTags': 'disabled'}, 'EnclaveOptions': {'Enabled': False}, 'PlatformDetails': 'Linux/UNIX', 'UsageOperation': 'RunInstances', 'UsageOperationUpdateTime': datetime.datetime(2026, 2, 8, 6, 47, 19, tzinfo=tzutc()), 'PrivateDnsNameOptions': {'HostnameType': 'ip-name', 'EnableResourceNameDnsARecord': False, 'EnableResourceNameDnsAAAARecord': False}, 'MaintenanceOptions': {'AutoRecovery': 'default', 'RebootMigration': 'default'}, 'CurrentInstanceBootMode': 'legacy-bios', 'NetworkPerformanceOptions': {'BandwidthWeighting': 'default'}, 'Operator': {'Managed': False}, 'InstanceId': 'i-06271ca230354b199', 'ImageId': 'ami-0ecd75ef7998d592e', 'State': {'Code': 16, 'Name': 'running'}, 'PrivateDnsName': 'ip-10-0-10-221.eu-central-1.compute.internal', 'PublicDnsName': '', 'StateTransitionReason': '', 'KeyName': 'myapp-key', 'AmiLaunchIndex': 0, 'ProductCodes': [], 'InstanceType': 't2.micro', 'LaunchTime': datetime.datetime(2026, 2, 8, 6, 47, 19, tzinfo=tzutc()), 'Placement': {'AvailabilityZoneId': 'euc1-az2', 'GroupName': '', 'Tenancy': 'default', 'AvailabilityZone': 'eu-central-1a'}, 'Monitoring': {'State': 'disabled'}, 'SubnetId': 'subnet-05c1eec666d443fe4', 'VpcId': 'vpc-0a72063c7e93184b5', 'PrivateIpAddress': '10.0.10.221', 'PublicIpAddress': '63.180.218.215'}]
# [{'Architecture': 'x86_64', 'BlockDeviceMappings': [{'DeviceName': '/dev/xvda', 'Ebs': {'AttachTime': datetime.datetime(2026, 2, 8, 6, 47, 20, tzinfo=tzutc()), 'DeleteOnTermination': True, 'Status': 'attached', 'VolumeId': 'vol-09d8a09b7a490fd42', 'EbsCardIndex': 0}}], 'ClientToken': 'terraform-20260208064718566600000004', 'EbsOptimized': False, 'EnaSupport': True, 'Hypervisor': 'xen', 'NetworkInterfaces': [{'Association': {'IpOwnerId': 'amazon', 'PublicDnsName': '', 'PublicIp': '35.159.120.253'}, 'Attachment': {'AttachTime': datetime.datetime(2026, 2, 8, 6, 47, 19, tzinfo=tzutc()), 'AttachmentId': 'eni-attach-067a67a6c7fb019c3', 'DeleteOnTermination': True, 'DeviceIndex': 0, 'Status': 'attached', 'NetworkCardIndex': 0}, 'Description': '', 'Groups': [{'GroupId': 'sg-0bfd86e38a79bb03c', 'GroupName': 'myapp-sg'}], 'Ipv6Addresses': [], 'MacAddress': '02:c7:cc:26:70:c5', 'NetworkInterfaceId': 'eni-0abfc4d539e3f920a', 'OwnerId': '092611985600', 'PrivateIpAddress': '10.0.10.12', 'PrivateIpAddresses': [{'Association': {'IpOwnerId': 'amazon', 'PublicDnsName': '', 'PublicIp': '35.159.120.253'}, 'Primary': True, 'PrivateIpAddress': '10.0.10.12'}], 'SourceDestCheck': True, 'Status': 'in-use', 'SubnetId': 'subnet-05c1eec666d443fe4', 'VpcId': 'vpc-0a72063c7e93184b5', 'InterfaceType': 'interface', 'Operator': {'Managed': False}}], 'RootDeviceName': '/dev/xvda', 'RootDeviceType': 'ebs', 'SecurityGroups': [{'GroupId': 'sg-0bfd86e38a79bb03c', 'GroupName': 'myapp-sg'}], 'SourceDestCheck': True, 'Tags': [{'Key': 'Name', 'Value': 'dev-server'}], 'VirtualizationType': 'hvm', 'CpuOptions': {'CoreCount': 1, 'ThreadsPerCore': 1}, 'CapacityReservationSpecification': {'CapacityReservationPreference': 'open'}, 'HibernationOptions': {'Configured': False}, 'MetadataOptions': {'State': 'applied', 'HttpTokens': 'optional', 'HttpPutResponseHopLimit': 1, 'HttpEndpoint': 'enabled', 'HttpProtocolIpv6': 'disabled', 'InstanceMetadataTags': 'disabled'}, 'EnclaveOptions': {'Enabled': False}, 'PlatformDetails': 'Linux/UNIX', 'UsageOperation': 'RunInstances', 'UsageOperationUpdateTime': datetime.datetime(2026, 2, 8, 6, 47, 19, tzinfo=tzutc()), 'PrivateDnsNameOptions': {'HostnameType': 'ip-name', 'EnableResourceNameDnsARecord': False, 'EnableResourceNameDnsAAAARecord': False}, 'MaintenanceOptions': {'AutoRecovery': 'default', 'RebootMigration': 'default'}, 'CurrentInstanceBootMode': 'legacy-bios', 'NetworkPerformanceOptions': {'BandwidthWeighting': 'default'}, 'Operator': {'Managed': False}, 'InstanceId': 'i-0b19be68ddd2f4c8e', 'ImageId': 'ami-0ecd75ef7998d592e', 'State': {'Code': 16, 'Name': 'running'}, 'PrivateDnsName': 'ip-10-0-10-12.eu-central-1.compute.internal', 'PublicDnsName': '', 'StateTransitionReason': '', 'KeyName': 'myapp-key', 'AmiLaunchIndex': 0, 'ProductCodes': [], 'InstanceType': 't2.micro', 'LaunchTime': datetime.datetime(2026, 2, 8, 6, 47, 19, tzinfo=tzutc()), 'Placement': {'AvailabilityZoneId': 'euc1-az2', 'GroupName': '', 'Tenancy': 'default', 'AvailabilityZone': 'eu-central-1a'}, 'Monitoring': {'State': 'disabled'}, 'SubnetId': 'subnet-05c1eec666d443fe4', 'VpcId': 'vpc-0a72063c7e93184b5', 'PrivateIpAddress': '10.0.10.12', 'PublicIpAddress': '35.159.120.253'}]
# [{'Architecture': 'x86_64', 'BlockDeviceMappings': [{'DeviceName': '/dev/xvda', 'Ebs': {'AttachTime': datetime.datetime(2026, 2, 8, 6, 47, 20, tzinfo=tzutc()), 'DeleteOnTermination': True, 'Status': 'attached', 'VolumeId': 'vol-0341685bdc1a588c8', 'EbsCardIndex': 0}}], 'ClientToken': 'terraform-20260208064718566300000002', 'EbsOptimized': False, 'EnaSupport': True, 'Hypervisor': 'xen', 'NetworkInterfaces': [{'Association': {'IpOwnerId': 'amazon', 'PublicDnsName': '', 'PublicIp': '63.180.252.250'}, 'Attachment': {'AttachTime': datetime.datetime(2026, 2, 8, 6, 47, 19, tzinfo=tzutc()), 'AttachmentId': 'eni-attach-0c48cdd7edd7f3e60', 'DeleteOnTermination': True, 'DeviceIndex': 0, 'Status': 'attached', 'NetworkCardIndex': 0}, 'Description': '', 'Groups': [{'GroupId': 'sg-0bfd86e38a79bb03c', 'GroupName': 'myapp-sg'}], 'Ipv6Addresses': [], 'MacAddress': '02:79:76:75:19:e9', 'NetworkInterfaceId': 'eni-084155c642a443aca', 'OwnerId': '092611985600', 'PrivateIpAddress': '10.0.10.15', 'PrivateIpAddresses': [{'Association': {'IpOwnerId': 'amazon', 'PublicDnsName': '', 'PublicIp': '63.180.252.250'}, 'Primary': True, 'PrivateIpAddress': '10.0.10.15'}], 'SourceDestCheck': True, 'Status': 'in-use', 'SubnetId': 'subnet-05c1eec666d443fe4', 'VpcId': 'vpc-0a72063c7e93184b5', 'InterfaceType': 'interface', 'Operator': {'Managed': False}}], 'RootDeviceName': '/dev/xvda', 'RootDeviceType': 'ebs', 'SecurityGroups': [{'GroupId': 'sg-0bfd86e38a79bb03c', 'GroupName': 'myapp-sg'}], 'SourceDestCheck': True, 'Tags': [{'Key': 'Name', 'Value': 'dev-server-two'}], 'VirtualizationType': 'hvm', 'CpuOptions': {'CoreCount': 1, 'ThreadsPerCore': 1}, 'CapacityReservationSpecification': {'CapacityReservationPreference': 'open'}, 'HibernationOptions': {'Configured': False}, 'MetadataOptions': {'State': 'applied', 'HttpTokens': 'optional', 'HttpPutResponseHopLimit': 1, 'HttpEndpoint': 'enabled', 'HttpProtocolIpv6': 'disabled', 'InstanceMetadataTags': 'disabled'}, 'EnclaveOptions': {'Enabled': False}, 'PlatformDetails': 'Linux/UNIX', 'UsageOperation': 'RunInstances', 'UsageOperationUpdateTime': datetime.datetime(2026, 2, 8, 6, 47, 19, tzinfo=tzutc()), 'PrivateDnsNameOptions': {'HostnameType': 'ip-name', 'EnableResourceNameDnsARecord': False, 'EnableResourceNameDnsAAAARecord': False}, 'MaintenanceOptions': {'AutoRecovery': 'default', 'RebootMigration': 'default'}, 'CurrentInstanceBootMode': 'legacy-bios', 'NetworkPerformanceOptions': {'BandwidthWeighting': 'default'}, 'Operator': {'Managed': False}, 'InstanceId': 'i-08d9e57baaabb9188', 'ImageId': 'ami-0ecd75ef7998d592e', 'State': {'Code': 16, 'Name': 'running'}, 'PrivateDnsName': 'ip-10-0-10-15.eu-central-1.compute.internal', 'PublicDnsName': '', 'StateTransitionReason': '', 'KeyName': 'myapp-key', 'AmiLaunchIndex': 0, 'ProductCodes': [], 'InstanceType': 't2.micro', 'LaunchTime': datetime.datetime(2026, 2, 8, 6, 47, 19, tzinfo=tzutc()), 'Placement': {'AvailabilityZoneId': 'euc1-az2', 'GroupName': '', 'Tenancy': 'default', 'AvailabilityZone': 'eu-central-1a'}, 'Monitoring': {'State': 'disabled'}, 'SubnetId': 'subnet-05c1eec666d443fe4', 'VpcId': 'vpc-0a72063c7e93184b5', 'PrivateIpAddress': '10.0.10.15', 'PublicIpAddress': '63.180.252.250'}]
