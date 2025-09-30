# ==============================
# Project: Ping Multiple IPs (from file)
# Language: Python 3
# ==============================

# Step-by-Step Explanation of Ping Script:
#
# 1. import os       → Lets Python run system commands like ping.
# 2. import platform → Detects if you are on Windows, Linux, or macOS.
# 3. IPs are stored in a text file (ip_list.txt) → The script reads them automatically.
# 4. Detect OS       → Windows uses -n for ping count, Linux/macOS uses -c.
# 5. Ping loop       → For each IP:
#       a. Show message "Pinging ..."
#       b. Ping the IP once (1)
#       c. Check result (0 = success, anything else = failure)
#       d. Print result → Reachable ✅ or Not reachable ❌

import os
import platform

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
# Step 3: Ping each IP
# -------------------------------
print("\n=== Starting Ping Test ===\n")

for ip in ips:
    print(f"Pinging {ip} ...")
    response = os.system(f"ping {ping_param} 1 {ip}")
    
    if response == 0:
        print(f"{ip} is reachable ✅\n")
    else:
        print(f"{ip} is not reachable ❌\n")

print("=== Ping Test Completed ===")
