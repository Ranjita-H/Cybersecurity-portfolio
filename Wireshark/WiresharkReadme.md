# Wireshark: A Comprehensive Guide  

Wireshark is one of the most powerful network traffic analysis tools, widely used for troubleshooting, security monitoring, and protocol analysis. This guide provides an overview of Wireshark’s features, functionalities, and best practices.

## 📌 Table of Contents  
- [Introduction](#introduction)  
- [Key Features](#key-features)  
- [Wireshark GUI](#wireshark-gui)  
- [Packet Analysis](#packet-analysis)  
- [Traffic Sniffing](#traffic-sniffing)  
- [Filtering and Searching](#filtering-and-searching)  
- [Exporting and Saving Data](#exporting-and-saving-data)  
- [Expert Information](#expert-information)  

## 🔍 Introduction  
Wireshark is a network protocol analyzer that enables users to capture and inspect packets in real-time. It is widely used for:  
✔️ Troubleshooting network congestion & failures  
✔️ Detecting security anomalies  
✔️ Learning and analyzing network protocols  

> **Note:** Wireshark is *not* an Intrusion Detection System (IDS). It does not modify network traffic but only allows for detailed packet inspection.

## 🚀 Key Features  
- **Real-time packet capture** from various network interfaces  
- **Deep packet inspection** with multi-pane analysis  
- **Powerful filtering capabilities** for targeted analysis  
- **Support for numerous protocols**, including TCP, UDP, HTTP, and FTP  
- **Color-coding of packets** for quick analysis  
- **Ability to merge, export, and save capture files**  

## 🖥️ Wireshark GUI Overview  
Wireshark’s interface consists of five primary sections:  
1. **Toolbar** – Shortcuts for capturing, filtering, and analyzing packets  
2. **Display Filter Bar** – Allows users to apply queries for precise packet inspection  
3. **Packet List Pane** – Displays captured packets with source, destination, protocol, etc.  
4. **Packet Details Pane** – Breaks down packet structure based on OSI layers  
5. **Packet Bytes Pane** – Shows raw hexadecimal and ASCII data  

## 📊 Packet Analysis  
Wireshark provides detailed packet dissection across OSI layers:  
- **Layer 1 (Physical)** – Frame details  
- **Layer 2 (Data Link)** – MAC addresses  
- **Layer 3 (Network)** – Source & destination IPs  
- **Layer 4 (Transport)** – Protocol (TCP/UDP), port numbers  
- **Layer 5 (Application)** – Protocol-specific details (HTTP, FTP, SMB, etc.)  

### Packet Numbering  
Wireshark assigns **unique numbers** to each packet, making it easier to track events and conversations.

## 🕵️ Traffic Sniffing  
Wireshark allows **live network traffic capture** using available network interfaces. Key functionalities include:  
- Start sniffing with the **blue shark button**  
- Stop sniffing with the **red button**  
- Restart capture with the **green button**  
- Merge multiple capture files via `File → Merge`  

## 🔍 Filtering and Searching  
Wireshark supports two types of filters:  
1. **Capture Filters** – Applied before capturing packets to limit data collection  
2. **Display Filters** – Applied after capture to refine visible data  

### Common Display Filters:  
```sh
ip.src == 192.168.1.1      # Filter packets from a specific IP  
ip.dst == 192.168.1.2      # Filter packets to a specific IP  
tcp.port == 80             # Show only HTTP traffic  
http.request               # Show HTTP requests  
```
Other features include:
✅ Packet marking – Highlight specific packets for review
✅ Search packets – Locate packets by content, regex, or hex values
✅ Conversation filtering – Show all packets in a communication session

📂 Exporting and Saving Data
Wireshark allows users to export packets for further analysis.

Export packets (File → Export) to save relevant traffic
Extract transferred files (HTTP, SMB, FTP) from captured streams
Save only marked packets to reduce noise
🛠️ Expert Information
Wireshark categorizes potential issues using Expert Info, which assigns severity levels:

🔵 Chat (Info) – Normal workflow details
🔹 Note (Cyan) – Notable events or error codes
🟡 Warning (Yellow) – Potential issues
🔴 Error (Red) – Malformed packets or protocol violations
Use Analyze → Expert Information to review detected anomalies.

🎯 Conclusion
Wireshark is a must-have tool for network engineers, cybersecurity analysts, and IT professionals. Mastering its filtering, packet analysis, and exporting features will enhance your ability to diagnose and troubleshoot network issues effectively.
