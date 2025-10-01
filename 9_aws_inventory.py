# ==============================
# Project: Full AWS Inventory (EC2, S3, VPC, Subnets)
# Language: Python 3
# AWS Library: Boto3
# Output: Prints all EC2 instances, S3 buckets, VPCs, and Subnets
# ==============================

# Step-by-Step Explanation:
#
# 1. import boto3
#       → Lets Python connect and interact with AWS services.
# 2. Create EC2 client
#       → ec2 = boto3.client("ec2")
#       → EC2 client is needed to get information about EC2, VPCs, and Subnets.
# 3. Create S3 client
#       → s3 = boto3.client("s3")
#       → S3 client is needed to get information about storage buckets.
# 4. List EC2 instances
#       → Loop through each reservation and instance.
#       → Print instance ID and state (running/stopped).
# 5. List S3 buckets
#       → Loop through each bucket.
#       → Print bucket name and creation date.
# 6. List VPCs
#       → Loop through each VPC.
#       → Print VPC ID and CIDR block.
# 7. List Subnets
#       → Loop through each Subnet.
#       → Print Subnet ID and CIDR block.

import boto3   # AWS SDK for Python

# --- Create AWS clients ---
ec2 = boto3.client("ec2")  # EC2 client for instances, VPCs, subnets
s3 = boto3.client("s3")    # S3 client for buckets

# --- EC2 Instances ---
print("=== EC2 INSTANCES ===")
for reservation in ec2.describe_instances()["Reservations"]:
    for instance in reservation["Instances"]:
        print(f"ID: {instance['InstanceId']} | State: {instance['State']['Name']}")

# --- S3 Buckets ---
print("\n=== S3 BUCKETS ===")
for bucket in s3.list_buckets()["Buckets"]:
    print(f"Name: {bucket['Name']} | Created: {bucket['CreationDate']}")

# --- VPCs ---
print("\n=== VPCs ===")
for vpc in ec2.describe_vpcs()["Vpcs"]:
    print(f"VPC ID: {vpc['VpcId']} | CIDR: {vpc['CidrBlock']}")

# --- Subnets ---
print("\n=== SUBNETS ===")
for subnet in ec2.describe_subnets()["Subnets"]:
    print(f"Subnet ID: {subnet['SubnetId']} | CIDR: {subnet['CidrBlock']}")
