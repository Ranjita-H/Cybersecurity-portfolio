# Brim - Network Forensics and Threat Hunting

## Introduction  

Brim is an open-source desktop application designed for processing and analyzing **pcap files** and **log files**, primarily focusing on search and analytics. It provides a powerful GUI and integrates with **Zeek** and **Suricata** for detection and event correlation.  

## Why Use Brim?  

- Handles large **pcap files** efficiently  
- Provides **Zeek log processing** and **Suricata rule detection**  
- Supports **filtering, sorting, and visualization** of network traffic  
- Allows for **threat hunting** through advanced queries  
- Integrates with **Wireshark** for deeper packet analysis  

## Folder Structure  

This repository is structured to provide a comprehensive guide to Brim, including **usage**, **comparison with other tools**, **advanced query techniques**, and **real-world threat-hunting scenarios**.  


## **📖 Overview**  
Brim is an open-source forensic and network traffic analysis tool designed to handle large PCAP files efficiently. It integrates with **Zeek**, **Suricata**, and **Wireshark**, enabling advanced search and filtering to detect cyber threats.

### **🛠️ Key Features**  
✅ **Efficient Large PCAP Handling** – Analyze massive network captures.  
✅ **Powerful Search & Filtering** – Supports structured queries using **Zed Language**.  
✅ **Threat Detection** – Identify **malware**, **C2 communication**, and **exfiltration**.  
✅ **Log Analysis** – Process **Zeek**, **Suricata**, and **other logs**.  
✅ **Wireshark Integration** – Deep packet inspection with a single click.  


## **🚀 Installation & Setup**  

### **🔹 Step 1: Download Brim**  
Download the latest version from [Brim Official Website](https://www.brimdata.io/).  

### **🔹 Step 2: Install on Your OS**  
- **Windows** – Run the `.exe` installer.  
- **macOS** – Install via `.dmg`.  
- **Linux** – Use `.tar.gz` or install via **Snap**.  

### **🔹 Step 3: Launch Brim**  
- Open **Brim**.  
- Import **PCAP** or **log files**.  
- Start investigating network events!  

---

## **🖥️ Brim User Interface Overview**  

### **1️⃣ Pools Panel**  
- Displays imported **PCAP/log files**.  
- Shows **timestamps, stats, and indexed data**.  

### **2️⃣ Query Panel**  
- Write **custom queries** to search logs.  
- Supports **Zed query language**.  

### **3️⃣ Log Results Panel**  
- Displays **query results** in a table format.  
- Can export logs for further analysis.  

### **4️⃣ Wireshark Integration**  
- **Right-click** a log entry → **"View Packets in Wireshark"**.  
- **Wireshark opens the relevant packet** for deeper inspection.  

---

## **🔍 Searching & Filtering in Brim**  

### **📌 Basic Queries**  

🔹 **Search for a specific IP address**  
```sh
10.0.0.1
```

🔹 **View only connection logs**  
```sh
_path=="conn"
```

🔹 **Filter logs by time range**  
```sh
ts >= 2024-01-01T00:00:00Z and ts <= 2024-01-02T00:00:00Z
```

🔹 **Find unique hosts communicating**  
```sh
_path=="conn" | cut id.orig_h, id.resp_h | sort | uniq
```

---

## **🕵️‍♂️ Threat Hunting with Brim**  

### **📌 1. Detecting Malware C2 (Command & Control) Communication**  
```sh
_path=="dns" | count() by query | sort -r
```
🔍 **Why?** This helps identify unusual **DNS queries** from malware beaconing to a C2 server.  

---

### **📌 2. Detecting Data Exfiltration**  
```sh
_path=="conn" | put total_bytes := orig_bytes + resp_bytes | sort -r total_bytes
```
🔍 **Why?** Shows connections **transferring large amounts of data**, which could indicate data theft.  

---

### **📌 3. SMB Exploitation & Lateral Movement**  
```sh
_path=="dce_rpc" OR _path=="smb_mapping"
```
🔍 **Why?** **Detects suspicious SMB activity**, often used in ransomware attacks like **WannaCry**.  

---

## **📜 Advanced Query Examples**  

### **🔍 Extract Unique User-Agent Strings from HTTP Logs**  
```sh
_path=="http" | cut user_agent | sort | uniq
```

### **🔍 Identify Connections to Suspicious External Networks**  
```sh
_path=="conn" | put classnet := network_of(id.resp_h) | cut classnet | count() by classnet | sort -r
```

### **🔍 Detect Long-Lived Connections (Possible Backdoors)**  
```sh
_path=="conn" | put duration_sec := duration / 1000 | filter duration_sec > 600
```

---

## **⚖️ Brim vs. Wireshark vs. Zeek**  

| Feature                  | Brim           | Wireshark      | Zeek            |
|--------------------------|---------------|---------------|----------------|
| **GUI**                  | ✅ Yes         | ✅ Yes         | ❌ No          |
| **Traffic Sniffing**      | ❌ No         | ✅ Yes         | ✅ Yes        |
| **Pcap Processing**       | ✅ Yes        | ✅ Yes        | ✅ Yes       |
| **Log Processing**        | ✅ Yes        | ❌ No        | ✅ Yes       |
| **Filtering**            | ✅ Yes        | ✅ Yes        | ✅ Yes       |
| **Signature Support**    | ✅ Yes        | ❌ No        | ✅ Yes       |
| **Handling Large Pcaps** | ⭐⭐⭐ (Medium) | ⭐⭐ (Slow) | ⭐⭐⭐⭐ (Fast) |

---

## **🔥 Real-World Threat Hunting Cases**  

### **📌 Case 1: Suspicious DNS Requests (DGA Malware)**
1️⃣ **Identify Unusual DNS Requests**  
```sh
_path=="dns" | count() by query | sort -r
```
2️⃣ **Investigate the Most Frequent Queries**  
```sh
_path=="dns" | filter query in ("bad-domain.com", "randomized-dga.com")
```
📌 **Why?** Malware like **Emotet** & **TrickBot** use **DGA (Domain Generation Algorithms)** for C2 communication.

---

### **📌 Case 2: Lateral Movement via SMB**
1️⃣ **Detect SMB Logins**  
```sh
_path=="smb_mapping" | filter username!=""
```
2️⃣ **Find Hosts Making SMB Connections**  
```sh
_path=="conn" | filter id.resp_p == 445
```
📌 **Why?** **Lateral movement** using SMB is common in **ransomware attacks**.

---

## **📤 Exporting Data**  
1. **Click Export**  
2. **Choose CSV or JSON**  
3. **Save results** for reporting or further analysis.  

---

## **📚 Additional Resources**  
📖 [Brim Official Docs](https://docs.brimdata.io/)  
📖 [Zeek Documentation](https://zeek.org/documentation/)  

---

## **💡 Conclusion**  
Brim is a **powerful forensic tool** for **large-scale PCAP analysis**, **threat hunting**, and **incident response**. It seamlessly integrates with Wireshark, Zeek, and Suricata, making it an **essential tool for cybersecurity professionals**.

---
