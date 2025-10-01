import boto3   # boto3 হলো AWS এর জন্য Python লাইব্রেরি

# -------- EC2 Instances --------
# EC2 client বানাচ্ছি
ec2 = boto3.client("ec2")

print("=== EC2 INSTANCES ===")
# সব instance এর তথ্য আনছি
response = ec2.describe_instances()

# describe_instances() অনেক nested data দেয়, তাই loop ব্যবহার করছি
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        # প্রতিটি instance এর ID আর State (running/stopped) দেখাবো
        print(f"ID: {instance['InstanceId']} | State: {instance['State']['Name']}")

# -------- S3 Buckets --------
# S3 client বানাচ্ছি
s3 = boto3.client("s3")

print("\n=== S3 BUCKETS ===")
# সব bucket এর লিস্ট আনছি
buckets = s3.list_buckets()

# প্রতিটি bucket এর নাম আর কবে তৈরি হয়েছে তা দেখাবো
for bucket in buckets["Buckets"]:
    print(f"Name: {bucket['Name']} | Created: {bucket['CreationDate']}")
