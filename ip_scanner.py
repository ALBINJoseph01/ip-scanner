import os
import platform
import socket
import sys
import subprocess
from datetime import datetime
GREEN = "\33[32m"
END= "\033[0m"
banner = f"""
  {GREEN}



 _____           _         _                                                                                              
|_   _|         | |    _  (_)                                                                                             
  | | ___   ___ | |   (_)  _ _ __   ___  ___ __ _ _ __  _ __   ___ _ __                                                   
  | |/ _ \ / _ \| |       | | '_ \ / __|/ __/ _` | '_ \| '_ \ / _ | '__|                                                  
  | | (_) | (_) | |    _  | | |_) |\__ | (_| (_| | | | | | | |  __| |                                                     
  \_/\___/ \___/|_|   (_) |_| .__/ |___/\___\__,_|_| |_|_| |_|\___|_|                                                     
                            | |______                                                                                     
                            |_|______|                                                                                    
  ___        _   _                               ___  _    ______ _____ _   _   ___                      _     _____ __   
 / _ \      | | | |                 _     ____  / _ \| |   | ___ |_   _| \ | | |_  |                    | |   |  _  /  |  
/ /_\ \_   _| |_| |__   ___  _ __  (_)   / __ \/ /_\ | |   | |_/ / | | |  \| |   | | ___  ___  ___ _ __ | |__ | |/' `| |  
|  _  | | | | __| '_ \ / _ \| '__|      / / _` |  _  | |   | ___ \ | | | . ` |   | |/ _ \/ __|/ _ | '_ \| '_ \|  /| || |  
| | | | |_| | |_| | | | (_) | |     _  | | (_| | | | | |___| |_/ /_| |_| |\  /\__/ | (_) \__ |  __| |_) | | | \ |_/ _| |_ 
\_| |_/\__,_|\__|_| |_|\___/|_|    (_)  \ \__,_\_| |_\_____\____/ \___/\_| \_\____/ \___/|___/\___| .__/|_| |_|\___/\___/ 
                                         \____/                                                   | |                     
                                                                                                  |_|                     


{END}"""  
print(banner)
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
