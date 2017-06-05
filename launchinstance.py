import boto3
import sys
import time

ec2Client = boto3.client('ec2')
ec2 = boto3.resource('ec2')
VPNPeerIP = ""

launchec2 = ec2.create_instances(
                ImageId='ami-01ccc867',
                SubnetId="subnet-d07809a6",
                MinCount=1, 
                MaxCount=1,
                KeyName="NAT-INSTANCE",
                PrivateIpAddress = '10.10.0.1',
                InstanceType="t2.micro"),
                
                # launch ec2 in subnet by subnet tag!
                # SubnetId = ec2.get_id_from_nametag('subnets', 'examplesubnet')

mynewinstance = launchec2[0].id
print mynewinstance

# wait for instance state 'running'
launchec2[0].wait_until_running()

# assoicate eip
eip = ec2Client.allocate_address(DryRun=dryRun, Domain='vpc')
# Associate the elastic IP address with the instance launched above
ec2Client.associate_address(
    #  DryRun = dryRun,
     InstanceId = launchec2[0].id,
     AllocationId = eip["AllocationId"])

# disassoicate eip CLI
ec2Client.disassociate_address(
    # DryRun = 
    InstanceId = launchec2[0].id,
    Associatation)
#  aws ec2 disassociate-address --association-id eipassoc-2bebb745

# CloudWatch event
# CloudWatch event to detect if primary instance is down
# CloudWatch event to detect if the secondary instance is down (may not be needed as the primary will always have the EIP attached)

# Ec2
# Identify instances with the use of tags and obtain Instance ID
# Identify primary instance - EIP assigned
# disasscoiate eip from primary
# assoicate to secondary
# update routing tables and test connectivity.

# scratch
# power off instance (might not be needed!)
# instance = ec2.Instance(launchec2[0].id)
# response = instance.stop()
# launchec2[0].id.terminate()
# print response