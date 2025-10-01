import boto3      # AWS SDK for Python
import csv        # For saving data into CSV file
import logging    # For logging actions

# --- Setup logging ---
logging.basicConfig(
    filename="8_aws_inventory.log",  # log file name changed here
    level=logging.INFO,              # log level: INFO
    format="%(asctime)s - %(levelname)s - %(message)s"  # log format with time
)

# Create EC2 client (VPC and Subnets are part of EC2 service)
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
csv_file = "8_network_inventory.csv"   # changed file name here
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
