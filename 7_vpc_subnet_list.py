# ==============================
# Project: AWS VPC and Subnet Inventory
# Language: Python 3
# AWS Library: Boto3
# Output: CSV file with VPC and Subnet info
# ==============================

# Step-by-Step Explanation:
#
# 1. import boto3
#       → Lets Python connect to AWS services (EC2, S3, etc.).
# 2. import csv
#       → Allows Python to save data into CSV files.
# 3. Create EC2 client
#       → ec2 = boto3.client("ec2")
#       → EC2 service contains VPCs and Subnets, so we use this client to get network info.
# 4. Get all VPCs
#       → vpcs = ec2.describe_vpcs()
#       → Fetches all VPCs in your AWS account.
# 5. Get all Subnets
#       → subnets = ec2.describe_subnets()
#       → Fetches all Subnets in your AWS account.
# 6. Open CSV file to write
#       → with open("network_inventory.csv", "w", newline="") as file:
#       → Creates a file called network_inventory.csv to save the data.
# 7. Write header row
#       → writer.writerow(["ResourceType", "ID", "CIDR_Block"])
#       → Column names for CSV: Type (VPC/Subnet), ID, CIDR block.
# 8. Write VPC data
#       → Loop through each VPC and write its ID and CIDR block to CSV.
# 9. Write Subnet data
#       → Loop through each Subnet and write its ID and CIDR block to CSV.
# 10. Print confirmation message
#       → Shows the CSV file has been saved successfully.

import boto3     # AWS SDK for Python
import csv       # For saving data to CSV

# Create EC2 client
ec2 = boto3.client("ec2")

# --- Get all VPCs ---
print("Getting VPC information...")
vpcs = ec2.describe_vpcs()   # Fetch all VPC details

# --- Get all Subnets ---
print("Getting Subnet information...")
subnets = ec2.describe_subnets()   # Fetch all Subnet details

# --- Save data into CSV file ---
with open("network_inventory.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Write CSV header
    writer.writerow(["ResourceType", "ID", "CIDR_Block"])

    # Write VPC data
    for vpc in vpcs["Vpcs"]:
        writer.writerow(["VPC", vpc["VpcId"], vpc["CidrBlock"]])

    # Write Subnet data
    for subnet in subnets["Subnets"]:
        writer.writerow(["Subnet", subnet["SubnetId"], subnet["CidrBlock"]])

print("✅ VPC and Subnet info saved to network_inventory.csv")
