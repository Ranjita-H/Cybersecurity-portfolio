# Unified Kill Chain Framework

## Overview
The **Unified Kill Chain**, developed by Paul Pols in 2017, expands upon the Cyber Kill Chain by integrating **MITRE ATT&CK** techniques and addressing **modern attack methods** like lateral movement and persistence.

## Unified Kill Chain Phases
This framework consists of **three core phases** divided into **18 steps**:

### 1️⃣ **Initial Foothold**
| Stage | Description |
|--------|------------|
| **1. Reconnaissance** | Gathering information about the target (e.g., OSINT, network scanning). |
| **2. Resource Development** | Attackers prepare tools, infrastructure, and credentials. |
| **3. Initial Compromise** | Exploiting vulnerabilities to gain access (e.g., phishing, exploit kits). |
| **4. Establish Foothold** | Deploying malware or backdoors for persistent access. |
| **5. Escalate Privileges** | Gaining higher-level access on the system. |

### 2️⃣ **Network Propagation**
| Stage | Description |
|--------|------------|
| **6. Defense Evasion** | Hiding malicious activity from security tools. |
| **7. Credential Access** | Stealing usernames, passwords, and authentication tokens. |
| **8. Discovery** | Identifying network assets and security measures. |
| **9. Lateral Movement** | Moving across the network to reach valuable targets. |
| **10. Maintain Presence** | Ensuring long-term access through persistence techniques. |

### 3️⃣ **Mission Completion**
| Stage | Description |
|--------|------------|
| **11. Collection** | Gathering sensitive data (e.g., financial records, credentials). |
| **12. Attack Objectives** | Executing malicious actions (e.g., data theft, ransomware). |
| **13. Impact** | Disrupting systems (e.g., wiping data, launching DDoS). |
| **14. Exfiltration** | Transmitting stolen data outside the network. |
| **15. Monetization** | Selling stolen data or demanding ransom. |

## Unified Kill Chain Diagram
```mermaid
graph TD;
    A[Initial Foothold] -->|Recon| B[Resource Development];
    B --> C[Initial Compromise];
    C --> D[Establish Foothold];
    D --> E[Privilege Escalation];
    E --> F[Network Propagation];
    F --> G[Defense Evasion];
    G --> H[Credential Access];
    H --> I[Discovery];
    I --> J[Lateral Movement];
    J --> K[Maintain Presence];
    K --> L[Mission Completion];
    L --> M[Collection];
    M --> N[Attack Objectives];
    N --> O[Impact];
    O --> P[Exfiltration];
    P --> Q[Monetization];
