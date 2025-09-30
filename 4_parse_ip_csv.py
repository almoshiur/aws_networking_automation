# ==============================
# Project: Parse CSV of IPs/Subnets
# Language: Python 3
# ==============================

# Step-by-Step Explanation:
# 1. Read IPs from a CSV file (ip_list.csv).
# 2. Use ipaddress module to check each IP.
# 3. If IP belongs to a private range → mark as PRIVATE.
# 4. Otherwise → mark as PUBLIC.
# 5. Display results and save to report file.

import csv
import ipaddress
from datetime import datetime

# -------------------------------
# Step 1: Read IPs from CSV file
# -------------------------------
csv_file = "ip_list.csv"
report_file = "ip_report.txt"

try:
    with open(csv_file, "r") as file:
        reader = csv.DictReader(file)
        ips = [row["ip"].strip() for row in reader if row["ip"].strip()]
except FileNotFoundError:
    print("CSV file not found. Please create 'ip_list.csv' with an 'ip' column.")
    exit()

# -------------------------------
# Step 2: Process IPs
# -------------------------------
results = []
for ip in ips:
    try:
        ip_obj = ipaddress.ip_address(ip)
        if ip_obj.is_private:
            results.append(f"{ip} → PRIVATE")
        else:
            results.append(f"{ip} → PUBLIC")
    except ValueError:
        results.append(f"{ip} → INVALID IP")

# -------------------------------
# Step 3: Save Report
# -------------------------------
with open(report_file, "w", encoding="utf-8") as report:
    report.write("IP Report\n")
    report.write(f"Generated on: {datetime.now()}\n")
    report.write("="*40 + "\n\n")
    for line in results:
        report.write(line + "\n")

# -------------------------------
# Step 4: Print Results
# -------------------------------
print("\n=== IP Classification ===\n")
for line in results:
    print(line)
print(f"\n✅ Report saved to {report_file}")
