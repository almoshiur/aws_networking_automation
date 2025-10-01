import boto3     # Import boto3 (AWS SDK for Python)
import csv       # Import csv library to save data into CSV file

# Create EC2 client (because VPC and Subnets are part of EC2 service)
ec2 = boto3.client("ec2")

# --- Get all VPCs ---
print("Getting VPC information...")
vpcs = ec2.describe_vpcs()   # This will return all VPC details

# --- Get all Subnets ---
print("Getting Subnet information...")
subnets = ec2.describe_subnets()   # This will return all Subnet details

# --- Save data into CSV file ---
with open("network_inventory.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Write CSV column names (header row)
    writer.writerow(["ResourceType", "ID", "CIDR_Block"])

    # Write VPC data into CSV
    for vpc in vpcs["Vpcs"]:
        writer.writerow(["VPC", vpc["VpcId"], vpc["CidrBlock"]])

    # Write Subnet data into CSV
    for subnet in subnets["Subnets"]:
        writer.writerow(["Subnet", subnet["SubnetId"], subnet["CidrBlock"]])

print("✅ VPC and Subnet info saved to network_inventory.csv")
