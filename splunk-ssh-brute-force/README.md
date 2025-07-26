#  Splunk: SSH Brute Force Detection

This project simulates SSH brute-force attacks on a Linux machine and detects them using Splunk. It covers the full workflow—log collection, parsing, SPL-based detection, and dashboarding. It's built to reflect real-world SIEM analysis scenarios.

---

##  What This Project Does

- Simulates SSH brute-force attempts from an attacker machine
- Parses `/var/log/auth.log` from the Linux VM into Splunk
- Extracts key fields like `src_ip`, `user`, and `status`
- Builds SPL searches to detect Indicators of Compromise (IOCs)
- Visualizes detection results in a custom Splunk dashboard

---

##  Tools Used

- **Splunk Free Edition (local install)**
- **Linux VM (Ubuntu/Kali)** for log generation
- **VirtualBox** for VM setup
- **Custom Bash script** for SSH brute-force simulation (optional)
- **SPL (Search Processing Language)** for detection logic

---

##  Folder Structure

.
├── README.md
├── data/
│ └── sample_auth.log
├── spl/
│ ├── failed_attempts_by_ip.spl
│ └── all_queries.txt
├── screenshots/
│ ├── raw_logs_splunk.png
│ ├── ioc_detection_search.png
│ ├── dashboard_overview.png
│ ├── dashboard_panel_spl.png
│ └── source_of_log_data.png



---

##  Log Source

**File Monitored:** `/var/log/auth.log`

This file contains all SSH login activity on the Linux system.

**Sample Logs:**

```log
Jul 25 12:15:23 ubuntu sshd[1211]: Failed password for invalid user test from 192.168.1.50 port 50222 ssh2
Jul 25 12:15:27 ubuntu sshd[1211]: Accepted password for root from 192.168.1.50 port 50224 ssh2
These logs were ingested into Splunk via a Universal Forwarder or manual import.
```
## SPL Queries
## Failed Attempts by IP
```
index=auth_log sourcetype=linux_secure "Failed password"
| rex "from (?<src_ip>\d{1,3}(?:\.\d{1,3}){3})"
| stats count by src_ip
| where count > 1
```
Use: Identify source IPs attempting brute-force logins.

## Screenshots
All screenshots are located in the /screenshots folder:

|Filename|	Description|
|raw_logs_splunk.png|	Raw SSH logs ingested in Splunk|
|ioc_detection_search.png|	|IOC SPL search with highlighted results|
|dashboard_overview.png|	Full dashboard visual|
|dashboard_panel_spl.png|	Panel-level SPL query logic|
|source_of_log_data.png	|Proof of log file source (auth.log)|

## What I Learned
How brute-force SSH attacks appear in real logs

Writing SPL queries for threat detection

Creating dashboards for analyst workflows

Parsing custom log fields in Splunk

Simulating attacker behavior safely in a lab