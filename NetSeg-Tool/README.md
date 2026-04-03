# 🛡️ NETSEG.PY - Network Segmentation & Security Tool

Professional Python tool developed for network reconnaissance, security scanning, and CIDR calculations. Built with a "Security-First" mindset to assist IT Support and Security Engineers.

---

## 🚀 Key Features
* **Network Discovery**: Fast host discovery using `nmap -sn` (Ping Sweep).
* **Service Enumeration**: Detailed service version detection and OS fingerprinting (`nmap -sV`).
* **Subnet Calculator**: Advanced IPv4 calculation (Network ID, Broadcast, Host Range) using the `ipaddress` library.
* **Security Reporting**: Automated system status and network vulnerability reporting.
* **Malware Integration**: Local directory scanning capabilities via `clamscan`.

---

## 🔒 Security Hardening (Anti-Injection)
This tool has been specifically audited and hardened against **OS Command Injection** attacks:
* **Input Validation**: Strict Regex filtering for all user-provided IP addresses and hostnames.
* **Safe Subprocesses**: Eliminated `shell=True` risks by using list-based arguments in `subprocess.run()`.
* **Error Handling**: Robust try-except blocks to prevent information leakage during crashes.

---

## 🛠️ Installation & Usage
1. **Clone the repository**:
   ```bash
   git clone [https://github.com/simeonikolov/cybersecurity-portfolio.git](https://github.com/simeonikolov/cybersecurity-portfolio.git)
