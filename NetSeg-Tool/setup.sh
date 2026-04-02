#!/bin/bash
sudo apt update && sudo apt install -y clamav clamav-daemon
sudo freshclam
chmod +x netseg.py
