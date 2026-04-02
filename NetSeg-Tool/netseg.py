#!/usr/bin/env python3
import os
import sys
import subprocess

def clear():
    os.system('clear')

def main():
    while True:
        clear()
        print("==========================================")
        print("      NETSEG.PY - IT-SUPPORT-24 PRO")
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
            subprocess.run(f"nmap -sn {net}", shell=True)
            input("\nDone. Press Enter...")
        elif choice == '2':
            ip = input("Enter Target IP: ")
            subprocess.run(f"nmap -sV -T4 {ip}", shell=True)
            input("\nDone. Press Enter...")
        elif choice == '3':
            path = input("Path (Default .): ") or "."
            subprocess.run(f"clamscan -r {path}", shell=True)
            input("\nDone. Press Enter...")
        elif choice == '4':
            print("\n--- Subnet Mode Active ---")
            input("\nDone. Press Enter...")
        elif choice == '5':
            subprocess.run("uname -a > report.txt", shell=True)
            print("Saved to report.txt")
            input("\nDone. Press Enter...")
        elif choice == '6':
            sys.exit()
        else:
            input("Invalid selection. Enter...")

if __name__ == "__main__":
    main()
