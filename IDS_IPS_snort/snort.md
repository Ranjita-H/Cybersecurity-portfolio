# Intrusion Detection & Prevention Systems (IDS/IPS) and Snort Documentation

This documentation covers the fundamentals of Intrusion Detection Systems (IDS) and Intrusion Prevention Systems (IPS) as well as an in-depth overview of [Snort](https://www.snort.org/), an open-source tool used for network intrusion detection and prevention.

---

# 🛡️ Snort: Intrusion Detection & Prevention System (IDS/IPS) Guide  

## 📌 Table of Contents  
1. [Introduction to Intrusion Detection Systems (IDS)](#introduction-to-intrusion-detection-systems-ids)  
2. [Types of IDS/IPS](#types-of-idsips)  
3. [What is Snort?](#what-is-snort)  
4. [Installation](#installation)  
5. [Running Snort in Different Modes](#running-snort-in-different-modes)  
6. [Understanding Snort Rule Syntax](#understanding-snort-rule-syntax)  
7. [Real-World Attack Detection Examples](#real-world-attack-detection-examples)  
8. [Logging & File Permissions](#logging--file-permissions)  
9. [Performance Tuning & Optimization](#performance-tuning--optimization)  
10. [Conclusion](#conclusion)  

---

## 🔍 Introduction to Intrusion Detection Systems (IDS)  
An **Intrusion Detection System (IDS)** monitors network traffic to detect **malicious activity, unauthorized access, and policy violations**.  

### **Detection Techniques:**  
- ✅ **Signature-Based Detection** – Matches known attack patterns.  
- ✅ **Anomaly-Based Detection** – Flags unusual activity based on behavior analysis.  
- ✅ **Hybrid Detection** – Combines both methods for better accuracy.  

---

## ⚔️ Types of IDS/IPS  

| Type | Description | Example |  
|------|------------|---------|  
| **NIDS (Network-Based IDS)** | Monitors entire network traffic. | Snort, Suricata |  
| **HIDS (Host-Based IDS)** | Monitors logs & files on a single system. | OSSEC, Tripwire |  
| **NIPS (Network-Based IPS)** | Blocks suspicious network activity. | Snort (IPS Mode), Suricata |  
| **HIPS (Host-Based IPS)** | Blocks malware on an endpoint. | Windows Defender ATP |  

💡 **IDS detects, IPS prevents.**  

---

## 🛡️ What is Snort?  
Snort is an **open-source** Intrusion Detection and Prevention System (IDS/IPS) that **monitors network traffic in real-time** and **detects attacks** using a flexible rule-based language.  

### **Key Features:**  
✔ **Packet Sniffing** – Captures network traffic.  
✔ **Packet Logging** – Stores packets for later analysis.  
✔ **Intrusion Detection** – Alerts on suspicious activity.  
✔ **Intrusion Prevention** – Blocks threats when in IPS mode.  

---

## ⚙️ Installation  

### **For Debian/Ubuntu:**  
```bash
sudo apt update
sudo apt install snort -y
```

### **For CentOS/RHEL:**  
```bash
sudo yum install snort -y
```

### **Verify Installation:**  
```bash
snort -V
```
---

## Snort Modes & Parameters

### Common Parameters:
- **`-v`**: Verbose mode (displays detailed packet info).
- **`-i <interface>`**: Specify the network interface (e.g., `eth0`).
- **`-l <directory>`**: Define the logging directory.
- **`-c <config_file>`**: Load a specific configuration file.
- **`-T`**: Run self-test on configuration.
- **`-q`**: Quiet mode (suppress startup banners).

### IDS/IPS Specific Modes:
- **Inline Mode:** Enables Snort to drop or reject packets (IPS functionality) when used with DAQ modules like `afpacket`.
- **Packet Logger Mode:** Logs packets for post-analysis.
- **Sniffer Mode:** Simply captures and displays traffic without logging.

---
---

## 🚀 Running Snort in Different Modes  

### **1️⃣ Packet Sniffer Mode**  
```bash
snort -v
```

### **2️⃣ Packet Logger Mode**  
```bash
snort -dev -l /var/log/snort/
```

### **3️⃣ Intrusion Detection Mode**  
```bash
snort -c /etc/snort/snort.conf
```

💡 **Run Snort as root to avoid permission issues.**  

---

## 📝 Understanding Snort Rule Syntax  

A Snort rule follows this format:  
```
[action] [protocol] [source IP] [source port] -> [destination IP] [destination port] (options)
```

### **Example: Detecting a Ping Scan**  
```bash
alert icmp any any -> any any (msg:"ICMP Ping Detected"; sid:1000001;)
```

**🔍 Breakdown:**  
- `alert` → Triggers an alert.  
- `icmp` → Protocol (ICMP = ping).  
- `any any -> any any` → Monitors all traffic.  
- `msg:"ICMP Ping Detected"` → Alert message.  
- `sid:1000001;` → Unique rule ID.  

---

## 🚨 Real-World Attack Detection Examples  

### **1️⃣ Detecting a SQL Injection Attack**  
```bash
alert tcp any any -> any 80 (msg:"SQL Injection Attempt"; content:"' OR '1'='1"; sid:1000002;)
```

### **2️⃣ Detecting an SSH Brute Force Attack**  
```bash
alert tcp any any -> any 22 (msg:"Possible SSH Brute Force"; flags:S; threshold:type threshold, track by_src, count 5, seconds 30; sid:1000003;)
```

### **3️⃣ Detecting a Malicious File Download**  
```bash
alert tcp any any -> any 80 (msg:"Malicious EXE Download"; content:".exe"; sid:1000004;)
```

---

## 📂 Logging & File Permissions  

### **Change Snort Log Directory Permissions**  
```bash
sudo chown -R snort:snort /var/log/snort/
```

### **Run Snort with Elevated Privileges**  
```bash
sudo snort -c /etc/snort/snort.conf -A fast
```

---

## ⚡ Performance Tuning & Optimization  

### **1️⃣ Enable Fast Pattern Matching**  
Modify `snort.conf`:  
```bash
config detection: search-method ac-bnfa
```
💡 **Improves rule processing speed.**  

### **2️⃣ Exclude Internal Traffic**  
Modify rules to ignore LAN traffic:  
```bash
not src 192.168.1.0/24
```
💡 **Reduces false positives.**  

### **3️⃣ Use a Dedicated Logging Disk**  
```bash
mkdir /mnt/snort_logs
sudo mount /dev/sdb1 /mnt/snort_logs
snort -l /mnt/snort_logs/
```
💡 **Prevents disk I/O bottlenecks.**  

---

## 🎯 Conclusion  

Snort is a **powerful** IDS/IPS that helps detect and prevent cyberattacks. By **optimizing rules, using logging best practices, and applying real-world attack detection techniques,** you can maximize its effectiveness.  

### Further Reading:
- [Snort Official Documentation](https://www.snort.org/documents)
- [Understanding Berkeley Packet Filter (BPF)](https://en.wikipedia.org/wiki/Berkeley_Packet_Filter)
- [Snort Rule Writing Basics](https://www.snort.org/faq)

---
