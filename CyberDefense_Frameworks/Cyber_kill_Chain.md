# Cyber Kill Chain Framework

## Overview
The **Cyber Kill Chain**, developed by **Lockheed Martin**, is a structured framework for understanding cyberattack behavior. It outlines the stages attackers follow, allowing defenders to detect and mitigate threats at each phase.

## Cyber Kill Chain Stages
The Cyber Kill Chain consists of **seven stages**:

| Stage | Description |
|--------|------------|
| **1. Reconnaissance** | Attackers gather intelligence on targets (e.g., scanning networks, phishing, OSINT). |
| **2. Weaponization** | Malicious tools and payloads are developed (e.g., malware creation, exploit kits). |
| **3. Delivery** | Attackers send malicious payloads to the victim (e.g., phishing emails, USB drops, drive-by downloads). |
| **4. Exploitation** | The payload exploits vulnerabilities in the target system (e.g., buffer overflow, privilege escalation). |
| **5. Installation** | Malware is installed on the system to establish persistence (e.g., backdoors, remote access trojans). |
| **6. Command & Control (C2)** | Attackers establish communication channels with the compromised system (e.g., botnets, C2 servers). |
| **7. Actions on Objectives** | The attackers achieve their goal (e.g., data exfiltration, ransomware deployment, system disruption). |

## Cyber Kill Chain Diagram
```mermaid
graph LR;
    A[Reconnaissance] --> B[Weaponization];
    B --> C[Delivery];
    C --> D[Exploitation];
    D --> E[Installation];
    E --> F[Command & Control];
    F --> G[Actions on Objectives];
