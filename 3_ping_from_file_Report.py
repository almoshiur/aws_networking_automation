import os
import platform
from datetime import datetime

# -------------------------------
# Step 1: Read IPs from ip_list.txt
# -------------------------------
try:
    with open("ip_list.txt", "r") as file:
        ips = [line.strip() for line in file if line.strip()]  # Remove empty lines
except FileNotFoundError:
    print("IP list file not found. Please create 'ip_list.txt'.")
    exit()

# -------------------------------
# Step 2: Detect OS for ping
# -------------------------------
if platform.system().lower() == "windows":
    ping_param = "-n"  # Windows
else:
    ping_param = "-c"  # Linux/macOS

# -------------------------------
# Step 3: Open report file with UTF-8 encoding
# -------------------------------
report_file = "ping_report.txt"
with open(report_file, "w", encoding="utf-8") as report:  # <-- FIXED HERE
    report.write("Ping Report\n")
    report.write(f"Generated on: {datetime.now()}\n")
    report.write("="*40 + "\n\n")

    # -------------------------------
    # Step 4: Ping each IP
    # -------------------------------
    print("\n=== Starting Ping Test ===\n")

    for ip in ips:
        print(f"Pinging {ip} ...")
        response = os.system(f"ping {ping_param} 1 {ip}")

        if response == 0:
            result = f"{ip} is reachable ✅"
        else:
            result = f"{ip} is not reachable ❌"

        print(result + "\n")        # Show on screen
        report.write(result + "\n") # Save to file

    print("=== Ping Test Completed ===")
    report.write("\n=== Ping Test Completed ===\n")

print(f"\n✅ Report saved to {report_file}")
