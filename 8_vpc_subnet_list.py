# ==============================
# Project: AWS VPC and Subnet Inventory with Logging
# Language: Python 3
# AWS Library: Boto3
# Output: CSV file with VPC and Subnet info
# Log: Saves actions to a log file
# ==============================

# Step-by-Step Explanation:
#
# 1. import boto3
#       → Lets Python connect to AWS services (EC2, S3, etc.).
# 2. import csv
#       → Allows Python to save data into CSV files.
# 3. import logging
#       → Allows Python to save logs of script actions for tracking.
# 4. Setup logging
#       → logging.basicConfig(filename="8_aws_inventory.log", ...)
#       → All actions will be recorded in a log file with timestamp and level.
# 5. Create EC2 client
#       → ec2 = boto3.client("ec2")
#       → EC2 service contains VPCs and Subnets, so we use this client to get network info.
# 6. Get all VPCs
#       → vpcs = ec2.describe_vpcs()
#       → Fetches all VPCs in your AWS account.
# 7. Get all Subnets
#       → subnets = ec2.describe_subnets()
#       → Fetches all Subnets in your AWS account.
# 8. Open CSV file to write
#       → csv_file = "8_network_inventory.csv"
#       → with open(csv_file, "w", newline="") as file:
#       → Creates a CSV file to save the data.
# 9. Write header row
#       → writer.writerow(["ResourceType", "ID", "CIDR_Block"])
#       → Column names for CSV: Type (VPC/Subnet), ID, CIDR block.
# 10. Write VPC data
#       → Loop through each VPC and write its ID and CIDR block to CSV.
# 11. Write Subnet data
#       → Loop through each Subnet and write its ID and CIDR block to CSV.
# 12. Log each step
#       → logging.info(...) records every action to the log file.
# 13. Print confirmation message
#       → Shows CSV file has been saved successfully.

import boto3      # AWS SDK for Python
import csv        # For saving data into CSV
import logging    # For logging script actions

# --- Setup logging ---
logging.basicConfig(
    filename="8_aws_inventory.log",  # Log file name
    level=logging.INFO,              # Log level: INFO
    format="%(asctime)s - %(levelname)s - %(message)s"  # Log format with timestamp
)

# Create EC2 client
ec2 = boto3.client("ec2")

# --- Get all VPCs ---
print("Getting VPC information...")
logging.info("Fetching VPC information from AWS...")
vpcs = ec2.describe_vpcs()

# --- Get all Subnets ---
print("Getting Subnet information...")
logging.info("Fetching Subnet information from AWS...")
subnets = ec2.describe_subnets()

# --- Save data into CSV file ---
csv_file = "8_network_inventory.csv"
with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)

    # Write CSV header
    writer.writerow(["ResourceType", "ID", "CIDR_Block"])
    logging.info("CSV header written.")

    # Write VPC data
    for vpc in vpcs["Vpcs"]:
        writer.writerow(["VPC", vpc["VpcId"], vpc["CidrBlock"]])
    logging.info(f"{len(vpcs['Vpcs'])} VPC(s) written to CSV.")

    # Write Subnet data
    for subnet in subnets["Subnets"]:
        writer.writerow(["Subnet", subnet["SubnetId"], subnet["CidrBlock"]])
    logging.info(f"{len(subnets['Subnets'])} Subnet(s) written to CSV.")

print(f"✅ VPC and Subnet info saved to {csv_file}")
logging.info(f"VPC and Subnet information saved to {csv_file}")
