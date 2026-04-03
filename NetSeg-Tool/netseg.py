#!/usr/bin/env python3
import os
import sys
import subprocess
import re

def clear():
    os.system('clear')

def validate_input(user_input):
    if not re.match(r"^[a-zA-Z0-9./-]+$", user_input):
        return False
    return True

def main():
    while True:
        clear()
        print("==========================================")
        print("     NETSEG.PY - IT-SUPPORT-24 PRO")
        print("==========================================")
        print("1. Network Quick Scan (nmap -sn)")
        print("2. Service Detection Scan (nmap -sV)")
        print("3. Malware Scan (clamscan)")
        print("4. IP Subnet Calculator")
        print("5. Generate System Report")
        print("6. EXIT")
        print("------------------------------------------")
        
        choice = input("Select option [1-6]: ")

        if choice == '1':
            net = input("Enter Network: ")
            if validate_input(net):
                subprocess.run(["nmap", "-sn", net])
            else:
                print("Invalid input detected.")
            input("\nDone. Press Enter...")
        
        elif choice == '2':
            ip = input("Enter Target IP: ")
            if validate_input(ip):
                subprocess.run(["nmap", "-sV", "-T4", ip])
            else:
                print("Invalid input detected.")
            input("\nDone. Press Enter...")
            
        elif choice == '3':
            path = input("Path (Default .): ") or "."
            if validate_input(path):
                subprocess.run(["clamscan", "-r", path])
            else:
                print("Invalid input detected.")
            input("\nDone. Press Enter...")
            
        elif choice == '4':
            print("\n--- Subnet Mode Active ---")
            print("Feature under development. Logic coming soon.")
            input("\nDone. Press Enter...")
            
        elif choice == '5':
            with open("report.txt", "w") as f:
                subprocess.run(["uname", "-a"], stdout=f)
            print("Saved to report.txt")
            input("\nDone. Press Enter...")
            
        elif choice == '6':
            sys.exit()
        else:
            input("Invalid selection. Enter...")

if __name__ == "__main__":
    main()
