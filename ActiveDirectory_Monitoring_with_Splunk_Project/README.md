# MyDFIR Active Directory Home Lab Project

## Overview

This project guides you through building a hands-on, fully functional Active Directory (AD) home lab environment designed for cybersecurity learning and practice. The lab includes domain setup, attack simulation via Kali Linux, telemetry ingestion with Splunk, and Active Detection using Atomic Red Team.

You will learn:

- How to build and diagram an AD environment.
- Install and configure Windows Server (AD) and Windows 10 Target Machine.
- Set up Splunk as your SIEM for log ingestion and analysis.
- Deploy Kali Linux as an attacker machine with brute force tools.
- Perform attacks and monitor telemetry.
- Install and run Atomic Red Team tests to simulate attacker techniques.

---

## Lab Components

- **Windows Server 2022**: Acts as Domain Controller and Splunk Forwarder.
- **Windows 10 Machine**: Target endpoint joined to the domain with telemetry.
- **Kali Linux**: Attacker machine configured with penetration tools.
- **Splunk Enterprise (Ubuntu Server)**: SIEM platform collecting logs from DC and Target.
- **Atomic Red Team**: Framework for simulating attacker behaviors and generating telemetry.

---

## Hardware & Software Requirements

- Minimum 16 GB RAM recommended for VM stability.
- 250 GB disk space.
- VirtualBox preferred virtualization platform.
- Download links and setup instructions provided per part.

---

## Part 1: Project Introduction & Lab Design

- Project objective and outcomes.
- Create a logical network diagram using draw.io or equivalent.
- Define IP addressing and host roles:
  - Domain: `Blueteam.local`
  - Splunk Server: `192.168.10.10`
  - AD Domain Controller: `192.168.10.7`
  - Target Machine: DHCP assigned, joined to domain
  - Kali Linux Attacker: `192.168.10.250`

---

## Part 2: Installing Initial Components

- Download required ISOs:
  - Windows Server 2022
  - Windows 10
  - Kali Linux
  - Ubuntu Server (for Splunk)
- Install and configure VirtualBox VMs.
- Set static IP addresses on Splunk Server and Kali Linux.
- Update Kali Linux (`sudo apt update && sudo apt upgrade`).
- Prepare attacker environment with Crowbar for brute force.

---

## Part 3: Setting Up Telemetry & Logging

- Install and configure Sysmon on Domain Controller and Target.
- Install Splunk Universal Forwarder on Windows servers and targets.
- Configure Splunk Enterprise on Ubuntu VM to receive and index logs.
- Verify event ingestion and create basic queries.
- Key logs to monitor: Windows Security Event IDs 4624 (success), 4625 (failure).

---

## Part 4: Active Directory & Domain Setup

- Promote Windows Server to Domain Controller.
- Create new domain users such as `tsmith` and `jenny`.
- Enable RDP on Target machine and domain join.
- Assign RDP permissions to domain users.
- Validate RDP connectivity manually from Kali.

---

## Part 5: Attack Simulation & Monitoring

- Use Crowbar on Kali to brute force RDP logins.
- Customize and use a reduced password list (`passwords.txt`).
- Monitor Telemetry and security events in Splunk related to brute force attempts.
- Install Atomic Red Team on Target Windows machine:
  - Set PowerShell Execution Policy:  
    ```
    Set-ExecutionPolicy Bypass -Scope CurrentUser
    ```
  - Add Defender exclusion for C: drive.
  - Run installation script:  
    ```
    IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/install-atomicredteam.ps1'); Install-AtomicRedTeam -GetAtomics
    ```
- Run Atomic Red Team tests (e.g., technique `T1366.001`) and observe generated telemetry.
- Understand gaps in telemetry and elevate monitoring.

---

## Usage Notes & Best Practices

- Always perform attacks in authorized lab environments.
- Customize diagrams and IP addressing for your environment.
- Use snapshots in VirtualBox to save working lab states.
- Slow down brute force attempts to avoid lockouts.
- Extend telemetry monitoring and visualization in Splunk for real-world SOC skills.

---

## Additional Resources

- MyDFIR SOC Analyst Course: https://academy.mydfir.com/p/soc
- Official Atomic Red Team GitHub: https://github.com/redcanaryco/invoke-atomicredteam
- Rockyou Password List: `/usr/share/wordlists/rockyou.txt` on Kali Linux
- Draw.io for network diagrams: https://app.diagrams.net/

---

## Summary

This project builds core blue and red team skills by integrating lab setup, attack techniques, telemetry ingestion, and threat simulation. It lays a strong foundation for aspiring SOC analysts or cybersecurity professionals to understand AD environments, brute force attacks, SIEM usage, and adversary behavior simulation.

---

## Topology Diagram

![Blueteam Home Lab Topology](./blueteam_exact_topology.png)



**Disclaimer:**  
This lab environment is intended for educational purposes only. Only use it in authorized lab settings.

