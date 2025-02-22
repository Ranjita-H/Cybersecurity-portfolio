# Network Forensics

## Introduction
Network Forensics is a specialized subdomain of forensics focused on analyzing network traffic for security and investigative purposes. It involves capturing, recording, and analyzing network packets to detect malicious activities, security breaches, compliance violations, and overall network health.

## Key Investigation Factors
The investigation process revolves around identifying:
- **Who**: Source IP and port
- **What**: Data/Payload
- **Where**: Destination IP and port
- **When**: Time and date
- **Why**: How and what happened

A systematic approach is necessary to ensure accurate data collection and analysis.

## Use Cases
### Common Applications of Network Forensics:
1. **Network Discovery** – Identifies connected devices, rogue hosts, and network load.
2. **Packet Reassembling** – Reconstructs packets to analyze unencrypted traffic.
3. **Data Leakage Detection** – Detects abnormal data transfers.
4. **Malicious Activity Detection** – Identifies vulnerabilities, threats, and anomalies.
5. **Regulatory Compliance** – Ensures adherence to policies like GDPR, HIPAA, PCI DSS, etc.

## Advantages
- **Availability of Network-Based Evidence** – Easier to collect than logs.
- **Low Noise Data Collection** – Unlike traditional log-based approaches.
- **Hard to Destroy Evidence** – Network traffic exists independently of local logs.
- **Memory and Non-Residential Threat Analysis** – Detects malware operating in memory.

## Challenges
- **What to Investigate?** – Deciding on investigation scope.
- **Data Collection Issues** – Short capture times, missing full packets, encryption.
- **Privacy Concerns** – GDPR and legal compliance.
- **Time Zone Mismatches** – Correlation issues across different regions.
- **Lack of Logs** – Attackers often erase logs to evade detection.

## Sources of Network Evidence
Network traffic can be captured from:
- **Network Devices:** TAPS, SPAN ports, inline devices, hubs, switches, routers
- **Servers:** DHCP, DNS, Authentication, Firewalls, Web proxies
- **Logs:** IDS/IPS, OS, Application, Central log servers

## Primary Purposes
1. **Security Operations (SOC):** Continuous monitoring and threat detection.
2. **Incident Response & Threat Hunting:** Post-incident investigations and root cause analysis.

## Investigated Data Types
- **Live Traffic** – Captured in real time.
- **Traffic Captures** – Full packet captures (PCAP) and network flows.
- **Log Files** – Supporting correlation and event reconstruction.

## NetworkMiner Overview
NetworkMiner is a powerful tool for processing live and recorded traffic.

### Capabilities:
| Feature | Description |
|---------|-------------|
| Traffic Sniffing | Captures network traffic |
| Parsing PCAP | Processes captured traffic files |
| Protocol Analysis | Identifies communication protocols |
| OS Fingerprinting | Detects operating system signatures |
| File Extraction | Extracts files from traffic data |
| Credential Grabbing | Recovers stored credentials from traffic |
| Keyword Parsing | Identifies cleartext strings in traffic |

### Operating Modes:
1. **Sniffer Mode** – Captures live network traffic (Windows-only, not highly reliable).
2. **Packet Parsing** – Processes and analyzes previously captured traffic.

### Pros & Cons of NetworkMiner
**Pros:**
✅ OS fingerprinting
✅ Easy file extraction
✅ Credential recovery
✅ Clear text keyword parsing
✅ Quick traffic overview

**Cons:**
❌ Limited active sniffing
❌ Inefficient for large PCAPs
❌ Basic filtering options
❌ Not suitable for deep manual investigation

## Differences Between NetworkMiner & Wireshark
While both tools analyze traffic, they serve different purposes:

| Feature | NetworkMiner | Wireshark |
|---------|-------------|----------|
| Quick Overview | ✅ | ❌ |
| In-Depth Analysis | ❌ | ✅ |
| OS Fingerprinting | ✅ | ❌ |
| Keyword Discovery | ✅ | Manual |
| Credential Recovery | ✅ | ✅ |
| File Extraction | ✅ | ✅ |
| Advanced Filtering | ❌ | ✅ |
| Protocol Analysis | ❌ | ✅ |
| Payload Analysis | ❌ | ✅ |
| Statistical Analysis | ❌ | ✅ |

### Best Practice:
1. Capture traffic for offline analysis.
2. Use NetworkMiner for quick insights.
3. Conduct deep investigations with Wireshark.

## Key NetworkMiner Features
### 1. Hosts Overview
Displays:
- IP/MAC addresses
- OS type
- Open ports
- Data transfer statistics

### 2. Sessions Analysis
- Identifies communication between hosts
- Filters data by frame number, protocol, and ports

### 3. DNS Queries
- Tracks domain queries and responses
- Identifies suspicious DNS activity

### 4. Credentials Extraction
- Recovers login credentials from protocols like:
  - Kerberos
  - NTLM
  - RDP, HTTP, FTP, IMAP, SMTP

### 5. File Extraction
- Extracts images, HTML files, emails, and attachments

### 6. Message Analysis
- Investigates emails and chat messages

### 7. Keyword Discovery
- Extracts clear text keywords from traffic
- Supports regex and multi-word filtering

## Version Differences
### Major Differences (v1.6 vs v2.7):
| Feature | v1.6 | v2.7 |
|---------|------|------|
| MAC Address Processing | ❌ | ✅ |
| Frame Analysis | ✅ | ❌ |
| Parameter Extraction | Limited | Extensive |
| Cleartext Data Analysis | ✅ | ❌ |

## Conclusion
Network Forensics is essential for identifying security threats, investigating breaches, and ensuring compliance. NetworkMiner provides an efficient way to analyze captured network traffic before deep-diving with tools like Wireshark. 

---
### 📌 Recommended Next Steps:
- Explore **Wireshark** for deep packet analysis
- Set up **network traffic monitoring** in a lab environment
- Experiment with **real-world PCAP files** to enhance investigative skills


