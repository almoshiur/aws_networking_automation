# ==============================
# Project: Ping Multiple IPs
# Python 3
# ==============================

# Step-by-Step Explanation:
# 1. import os       → Lets Python run system commands like ping.
# 2. import platform → Detects if you are on Windows, Linux, or macOS.
# 3. ips = [...]     → List of IP addresses you want to check. You can add more.
# 4. Detect OS       → Windows uses -n for ping count, Linux/macOS uses -c.
# 5. Ping loop       → For each IP:
#       a. Show message "Pinging ..."
#       b. Ping the IP once (1)
#       c. Check result (0 = success, anything else = failure)
#       d. Print result → Reachable ✅ or Not reachable ❌

import os       # Run system commands
import platform # Detect operating system

# -------------------------------
# Step 1: List of IPs to check
# -------------------------------
ips = ["8.8.8.8", "192.168.1.1"]  # Add your own IPs here

# -------------------------------
# Step 2: Detect your OS
# -------------------------------
# Windows uses -n, Linux/macOS uses -c
if platform.system().lower() == "windows":
    ping_param = "-n"
else:
    ping_param = "-c"

# -------------------------------
# Step 3: Ping each IP
# -------------------------------
print("=== Starting Ping Test ===\n")

for ip in ips:
    print(f"Pinging {ip} ...")  # Show which IP is being pinged
    response = os.system(f"ping {ping_param} 1 {ip}")  # Ping once
    
    # Check if ping was successful
    if response == 0:
        print(f"{ip} is reachable ✅\n")  # Ping worked
    else:
        print(f"{ip} is not reachable ❌\n")  # Ping failed

print("=== Ping Test Completed ===")
