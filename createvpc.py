import boto3

ec2 = boto3.resource('ec2')

vpc = ec2.create_vpc(CidrBlock='10.2.0.0/16')
subnet = vpc.create_subnet(CidrBlock='10.2.0.0/25')
gateway = ec2.create_internet_gateway()

newvpcid = vpc[0].id
newsubnetid = subnet[0].id
newgatewayid = gateway[0].id

print newvpcid
print newsubnetid
print newgatewayid

# Needs work to return gateway id and use to attach to VPC
gateway.attach_to_vpc(VpcId=newvpcid
gateway.detach_from_vpc(VpcId=newvpcid)