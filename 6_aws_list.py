# ==============================
# Project: List AWS EC2 Instances and S3 Buckets
# Language: Python 3
# AWS Library: Boto3
# ==============================

# Step-by-Step Explanation of AWS Inventory Script:
#
# 1. import boto3
#       → Allows Python to interact with AWS services like EC2 and S3.
#
# 2. Create EC2 client
#       → ec2 = boto3.client("ec2")
#       → This “client” lets Python talk to AWS EC2 to get instance info.
#
# 3. Get all EC2 instances
#       → response = ec2.describe_instances()
#       → Fetches details of all instances in your AWS account.
#
# 4. Loop through instances
#       → response["Reservations"] contains groups of instances.
#       → Each reservation may have one or more instances.
#       → For each instance, we print:
#           a. Instance ID → Unique identifier
#           b. State       → running, stopped, etc.
#
# 5. Create S3 client
#       → s3 = boto3.client("s3")
#       → This “client” lets Python talk to AWS S3 to get bucket info.
#
# 6. Get all S3 buckets
#       → buckets = s3.list_buckets()
#       → Fetches the list of all S3 buckets in your account.
#
# 7. Loop through buckets
#       → For each bucket, print:
#           a. Bucket Name → Name of the storage bucket
#           b. Creation Date → When the bucket was created
#
# Result:
#       → Console output will show all EC2 instances and S3 buckets.

import boto3   # Import AWS SDK for Python

# -------- EC2 Instances --------
ec2 = boto3.client("ec2")  # Create EC2 client
print("=== EC2 INSTANCES ===")
response = ec2.describe_instances()  # Fetch all EC2 instances

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        print(f"ID: {instance['InstanceId']} | State: {instance['State']['Name']}")

# -------- S3 Buckets --------
s3 = boto3.client("s3")  # Create S3 client
print("\n=== S3 BUCKETS ===")
buckets = s3.list_buckets()  # Fetch all S3 buckets

for bucket in buckets["Buckets"]:
    print(f"Name: {bucket['Name']} | Created: {bucket['CreationDate']}")
