# Intrusion Detection & Prevention Systems (IDS/IPS) and Snort Documentation

This documentation covers the fundamentals of Intrusion Detection Systems (IDS) and Intrusion Prevention Systems (IPS) as well as an in-depth overview of [Snort](https://www.snort.org/), an open-source tool used for network intrusion detection and prevention.

---

## Table of Contents
1. [Introduction](#introduction)
2. [IDS vs. IPS Overview](#ids-vs-ips-overview)
3. [Detection & Prevention Techniques](#detection--prevention-techniques)
4. [Snort Overview](#snort-overview)
5. [Snort Modes & Parameters](#snort-modes--parameters)
6. [Snort Configuration & Rule Basics](#snort-configuration--rule-basics)
7. [Example Commands](#example-commands)
8. [Conclusion & Further Resources](#conclusion--further-resources)

---

## Introduction
**Intrusion Detection Systems (IDS)** are passive monitoring solutions designed to detect suspicious or malicious activities and generate alerts. In contrast, **Intrusion Prevention Systems (IPS)** actively block or terminate such activities as soon as they are detected.

---

## IDS vs. IPS Overview

- **IDS (Intrusion Detection System)**
  - **Function:** Monitors network or host activities, generates alerts when suspicious behavior is detected.
  - **Types:**
    - **Network IDS (NIDS):** Monitors traffic across entire subnets.
    - **Host-based IDS (HIDS):** Monitors activities on individual endpoints.

- **IPS (Intrusion Prevention System)**
  - **Function:** Not only detects threats but also takes immediate action to block them.
  - **Types:**
    - **Network IPS (NIPS):** Protects entire network segments by terminating malicious connections.
    - **Behaviour-Based IPS (Network Behavior Analysis):** Learns “normal” traffic patterns during a training period and detects anomalies.
    - **Wireless IPS (WIPS):** Secures wireless networks.
    - **Host-based IPS (HIPS):** Actively monitors and blocks threats on a single device.

---

## Detection & Prevention Techniques

IDS/IPS solutions typically use three detection methods:

- **Signature-Based:**  
  Detects threats by matching known malicious patterns.

- **Behaviour-Based:**  
  Identifies unknown threats by comparing current activity against established normal behavior.

- **Policy-Based:**  
  Flags deviations from predefined security policies.

---

## Snort Overview
[Snort](https://www.snort.org/) is an open-source, rule-based tool that can be deployed in multiple modes:

- **Sniffer Mode:** Reads and displays IP packets (similar to tcpdump).
- **Packet Logger Mode:** Logs network traffic for further analysis.
- **IDS/IPS Mode:** Uses user-defined rules to detect and, if configured, block malicious traffic.

**Key Capabilities:**
- Live traffic analysis
- Attack/probe detection
- Protocol analysis and packet logging
- Real-time alerting with customizable outputs

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

## Snort Configuration & Rule Basics

### Configuration File (`snort.conf`)
- **Network Variables:** Define `HOME_NET`, `EXTERNAL_NET`, and rule paths.
- **Preprocessors:** Modules to normalize or modify packets before analysis.
- **Rule Inclusion:** Include user-created rules (typically in `local.rules`).

### Example Snort Rule:
```snort
alert icmp any any <> any any (msg:"ICMP Packet Detected"; sid:100001; rev:1;)
```

- **Action:** `alert` (generate an alert).
- **Protocol:** `icmp`
- **Traffic Direction:** `any any <> any any`
- **Options:** Includes a message (`msg`), a unique rule ID (`sid`), and a revision number (`rev`).

---

## Example Commands

### Starting Snort in Sniffer Mode:
```bash
sudo snort -v -i eth0
```

### Running Snort in Packet Logger Mode:
```bash
sudo snort -dev -l /path/to/logs
```

### Testing Snort Configuration:
```bash
sudo snort -T -c /etc/snort/snort.conf
```

### Running Snort in IDS/IPS Mode:
```bash
sudo snort -A fast -c /etc/snort/snort.conf -i eth0
```

---

## Conclusion & Further Resources
IDS and IPS are fundamental for effective network security. Snort, with its flexible deployment modes and rich rule-based detection, is an essential tool for both monitoring and actively defending networks.

### Further Reading:
- [Snort Official Documentation](https://www.snort.org/documents)
- [Understanding Berkeley Packet Filter (BPF)](https://en.wikipedia.org/wiki/Berkeley_Packet_Filter)
- [Snort Rule Writing Basics](https://www.snort.org/faq)

---
