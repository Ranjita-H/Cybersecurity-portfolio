# MITRE ATT&CK Framework

## Overview
[MITRE ATT&CK](https://attack.mitre.org/) (Adversarial Tactics, Techniques, and Common Knowledge) is a globally accessible knowledge base of cyber adversary behavior. It provides a structured way to analyze, detect, and respond to cybersecurity threats based on real-world attack techniques.

## Key Components
MITRE ATT&CK is divided into several matrices, with the most widely used being:
- **Enterprise Matrix** (Windows, Linux, macOS, Cloud, Network, Containers)
- **Mobile Matrix** (Android, iOS)
- **ICS Matrix** (Industrial Control Systems)

Each matrix consists of:
1. **Tactics** – The "why" behind an attack (e.g., Persistence, Defense Evasion).
2. **Techniques & Sub-Techniques** – The "how" attackers achieve their goal (e.g., Phishing, Process Injection).
3. **Procedures** – Real-world methods used by threat actors to implement a technique.

## ATT&CK Tactics
Some key **tactics** in the MITRE ATT&CK framework include:

| Tactic                | Description |
|----------------------|-------------|
| **Initial Access**   | Gaining a foothold (e.g., Spearphishing, Exploiting Public-Facing Applications). |
| **Execution**        | Running malicious code (e.g., PowerShell, Scheduled Tasks). |
| **Persistence**      | Maintaining access (e.g., Registry Run Keys, Startup Items). |
| **Privilege Escalation** | Gaining higher-level permissions (e.g., Kernel Exploits, Sudo Exploitation). |
| **Defense Evasion**  | Avoiding detection (e.g., Obfuscated Files, Code Injection). |
| **Credential Access** | Stealing sensitive credentials (e.g., Keylogging, Credential Dumping). |
| **Discovery**        | Learning about the environment (e.g., System Information Discovery). |
| **Lateral Movement** | Moving within a network (e.g., Remote Desktop Protocol (RDP), Pass the Hash). |
| **Collection**       | Gathering data (e.g., Screen Capture, Browser Session Hijacking). |
| **Exfiltration**     | Sending stolen data outside the organization (e.g., Cloud Storage, Encrypted Channels). |
| **Impact**          | Disrupting, destroying, or modifying systems (e.g., Ransomware, Data Destruction). |

## ATT&CK Techniques
Each **tactic** consists of multiple **techniques** and **sub-techniques** that describe how adversaries achieve their objectives.  
You can explore them in detail via the **[MITRE ATT&CK Navigator](https://attack.mitre.org/)**.

## Use Cases of MITRE ATT&CK
Organizations use ATT&CK for:
- **Threat Intelligence** – Understanding real-world attack behavior.
- **Red Teaming** – Simulating attacks for testing security defenses.
- **SOC Operations** – Detecting and responding to threats.
- **Incident Response** – Investigating and mitigating breaches.

## MITRE ATT&CK Diagram
```mermaid
graph TD;
    A[Tactics] -->|Why?| B[Techniques];
    B -->|How?| C[Procedures];
    C -->|Real-World Attacks| D[Threat Actors];
