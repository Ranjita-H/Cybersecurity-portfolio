Understanding the Basics of Threat Intelligence & Its Classifications

What is Threat Intelligence?

Threat intelligence (TI) is actionable information about cyber threats and threat actors that helps organizations detect, prevent, and mitigate cyber risks. It provides insights into attack methods, indicators of compromise (IoCs), and tactics, techniques, and procedures (TTPs) used by adversaries.

Types of Threat Intelligence

Threat intelligence is broadly classified into four categories:

Strategic Intelligence

High-level, non-technical insights for executives and decision-makers.

Example: Reports on emerging cyber threats affecting the financial sector.

Tactical Intelligence

Provides insights into specific TTPs used by cybercriminals.

Example: Understanding how phishing campaigns target banking customers.

Operational Intelligence

Focuses on real-time attack data, often used by SOC analysts.

Example: IoCs (IPs, domains, hashes) linked to active malware campaigns.

Technical Intelligence

Deals with forensic-level data, including malware samples and vulnerabilities.

Example: Reverse engineering malware to analyze its behavior.

Using UrlScan.io to Scan for Malicious URLs

What is UrlScan.io?

UrlScan.io is a powerful online service for scanning and analyzing URLs. It helps in identifying malicious websites, phishing pages, and fraudulent activities by providing:

Website snapshots.

Domain reputation analysis.

Network request logs and redirects.

How to Use UrlScan.io for Threat Intelligence

Visit https://urlscan.io.

Enter the URL you want to scan.

Click Submit and wait for the scan to complete.

Analyze the results:

Screenshot: Check the visual representation of the website.

Domain Analysis: Verify WHOIS details and hosting information.

Request Log: Identify third-party requests and suspicious redirects.

Cross-check against known threat feeds (e.g., VirusTotal, OpenPhish).

Use Case: Investigate phishing URLs received in suspicious emails.

Using Abuse.ch to Track Malware and Botnet Indicators

What is Abuse.ch?

Abuse.ch provides real-time tracking of malware, botnets, and cyber threats. It offers threat intelligence feeds that help security professionals:

Identify active malware samples.

Detect command-and-control (C2) infrastructure.

Monitor domains/IPs involved in cybercrime.

Key Abuse.ch Threat Intelligence Feeds

URLhaus: Tracks malicious URLs distributing malware.

ThreatFox: Community-driven threat intelligence platform.

MalwareBazaar: Repository of malware samples and IoCs.

How to Use Abuse.ch for Threat Research

Visit https://abuse.ch.

Choose a relevant threat feed (e.g., URLhaus for malicious URLs).

Search for specific IoCs (domains, hashes, IPs).

Download IoC lists and integrate them into security tools (e.g., SIEM, IDS/IPS).

Use Case: Investigating an unknown IP found in firewall logs.

Investigating Phishing Emails Using PhishTool

What is PhishTool?

PhishTool is a forensic analysis platform designed to investigate phishing emails. It helps SOC analysts and threat hunters by extracting:

Email headers.

Embedded malicious URLs.

Phishing indicators.

How to Analyze Phishing Emails with PhishTool

Visit https://phishtool.com.

Upload a phishing email (EML format) or paste raw email headers.

Analyze the extracted data:

Sender information: Verify if the email is spoofed.

Embedded URLs: Check for malicious redirects.

Attachments: Inspect for malware payloads.

Cross-check results with threat intelligence platforms (e.g., VirusTotal, Abuse.ch).

Use Case: Validating a suspected phishing email received by an employee.

Using Cisco's Talos Intelligence Platform for Intel Gathering

What is Cisco Talos?

Cisco Talos Intelligence is a threat intelligence research team that provides:

Global threat visibility.

Malware analysis and indicators.

IP and domain reputation services.

How to Use Talos for Threat Intelligence

Visit https://talosintelligence.com/.

Use the IP & Domain Reputation Center to:

Search for malicious domains or IPs.

View historical threat data.

Assess email security risk (SPF, DKIM, DMARC status).

Check Talos Blog & Threat Advisories for updates on emerging cyber threats.

Integrate Talos threat feeds into security tools for automated monitoring.

Use Case: Checking if an IP address flagged in firewall logs is associated with malicious activity.

Summary

This documentation serves as a practical guide for cybersecurity professionals to leverage threat intelligence platforms for enhanced security operations. These tools help detect, analyze, and respond to cyber threats effectively:

Platform and Use Case:

UrlScan.io:Scan & analyze suspicious URLs

Abuse.ch:Track malware, botnets, & C2 infrastructure

PhishTool:Investigate phishing emails

Cisco Talos->Gather domain/IP reputation data & cyber threat insights



