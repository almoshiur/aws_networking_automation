# ==============================
# Project: Ping server first, then SSH login directly
# Language: Python 3
# Libraries: os, platform, paramiko, getpass
# ==============================

# -------------------------------
# Step-by-Step Explanation:
# -------------------------------
# 1. Ask the user for the server IP.
# 2. Ping the server to check if it is reachable.
#    - Windows uses '-n' for ping count
#    - Linux/Mac uses '-c' for ping count
# 3. If ping is successful:
#    - Ask the user for SSH username and password
#    - Create an SSH client using paramiko
#    - Automatically accept unknown host keys (AutoAddPolicy)
#    - Connect to the server using provided credentials
#    - Confirm that SSH login is successful
# 4. If ping fails:
#    - Inform the user that the server is not reachable
# 5. Close the SSH connection in all cases (finally block)
# -------------------------------

import os         # To run ping command from Python
import platform   # To detect the operating system
import paramiko   # To perform SSH connection
import getpass    # To safely input password (hidden)

# -------------------------------
# Step 1: Ask for server IP
# -------------------------------
hostname = input("Enter server IP: ")  # Example: 192.168.1.100

# -------------------------------
# Step 2: Detect OS and set ping parameter
# -------------------------------
# Windows requires '-n', Linux/Mac requires '-c'
param = "-n" if platform.system().lower() == "windows" else "-c"

# -------------------------------
# Step 3: Ping the server
# -------------------------------
print(f"\n🔍 Pinging {hostname} ...")
response = os.system(f"ping {param} 1 {hostname}")  # Ping the server once

# -------------------------------
# Step 4: Check ping result
# -------------------------------
if response == 0:  # Ping successful
    print(f"✅ {hostname} is reachable!\n")

    # -------------------------------
    # Step 5: Ask for SSH login details
    # -------------------------------
    username = input("Enter SSH username: ")  # SSH username
    password = getpass.getpass("Enter SSH password: ")  # SSH password (hidden)

    # -------------------------------
    # Step 6: Setup SSH client
    # -------------------------------
    ssh = paramiko.SSHClient()  # Create SSH client object
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Auto accept unknown host keys

    # -------------------------------
    # Step 7: Connect to the server
    # -------------------------------
    try:
        print(f"\n🔌 Connecting to {hostname} ...")
        ssh.connect(hostname, username=username, password=password)  # Connect via SSH
        print("✅ SSH Connected successfully!\n")

        # Step 8: Confirm login (no command execution)
        print(f"🎉 You are now logged into {hostname} as {username}")

    except Exception as e:
        print(f"❌ SSH Connection failed: {e}")  # Show error if connection fails

    finally:
        # Step 9: Close SSH connection
        ssh.close()
        print("\n🔒 Connection closed.")

else:
    # Ping failed → server not reachable
    print(f"❌ {hostname} is not reachable. Check IP or network.")
