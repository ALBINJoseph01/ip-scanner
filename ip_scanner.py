import os
import platform
import socket
import sys
import subprocess
from datetime import datetime
./ .banner
def clear_screen():
    
    if platform.system() == "Windows":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)

def scan_ip(target_ip):
   
    response = subprocess.run(["ping", "-c", "1", "-W", "1", target_ip],
                              stdout=subprocess.DEVNULL,
                              stderr=subprocess.DEVNULL)
    return response.returncode == 0

def main():
    clear_screen()
    
   
    subnet = input("Enter the subnet to scan : ")

    
    if not subnet:
        print("Please enter a valid subnet.")
        sys.exit()

    
    start_time = datetime.now()
    active_ips = []

    try:
        print(f"\nScanning subnet {subnet}.0/24...\n")
        end = int(input("Enter the Last Number: "))
        for i in range(end):
            target_ip = f"{subnet}.{i}"
            if scan_ip(target_ip):
                print(f"Host {target_ip} is active.")
                active_ips.append(target_ip)

    except KeyboardInterrupt:
        print("\n\nScan interrupted by user. Exiting...")
        sys.exit()

    except Exception as e:
        print(f"\nAn error occurred: {e}")
        sys.exit()

    finally:
        end_time = datetime.now()
        total_time = end_time - start_time
        print(f"\nScan completed in {total_time}.")
        
        if active_ips:
            print("\nActive IP addresses:")
            for ip in active_ips:
                print(ip)
        else:
            print("\nNo active IP addresses found.")

if __name__ == "__main__":
    main()
