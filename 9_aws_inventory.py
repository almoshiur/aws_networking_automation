import boto3

# EC2 client
ec2 = boto3.client("ec2")
# S3 client
s3 = boto3.client("s3")

print("=== EC2 INSTANCES ===")
for reservation in ec2.describe_instances()["Reservations"]:
    for instance in reservation["Instances"]:
        print(f"ID: {instance['InstanceId']} | State: {instance['State']['Name']}")

print("\n=== S3 BUCKETS ===")
for bucket in s3.list_buckets()["Buckets"]:
    print(f"Name: {bucket['Name']} | Created: {bucket['CreationDate']}")

print("\n=== VPCs ===")
for vpc in ec2.describe_vpcs()["Vpcs"]:
    print(f"VPC ID: {vpc['VpcId']} | CIDR: {vpc['CidrBlock']}")

print("\n=== SUBNETS ===")
for subnet in ec2.describe_subnets()["Subnets"]:
    print(f"Subnet ID: {subnet['SubnetId']} | CIDR: {subnet['CidrBlock']}")
