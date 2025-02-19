# 🛡️ Threat Intelligence & Investigation Tools  

This repository contains my documentation on **Threat Intelligence basics, classifications, and hands-on investigations** using popular cybersecurity tools.  

---

## 📌 Understanding the Basics of Threat Intelligence & Its Classifications  

Threat Intelligence (TI) is the process of collecting, analyzing, and applying knowledge about cyber threats to enhance security defenses.  

### 🔍 Threat Intelligence Classifications  
1️⃣ **Strategic Threat Intelligence** – High-level insights for executives on attack motives & trends.  
2️⃣ **Tactical Threat Intelligence** – Focuses on attacker **TTPs (Tactics, Techniques, and Procedures)**.  
3️⃣ **Operational Threat Intelligence** – Real-time intelligence about **ongoing threats & incidents**.  
4️⃣ **Technical Threat Intelligence** – Specific indicators like **malicious IPs, hashes, domains**.  

---

## 🕵️ Using UrlScan.io to Scan for Malicious URLs  

### 🔹 What is UrlScan.io?  
[UrlScan.io](https://urlscan.io/) is an online service for **analyzing URLs and webpages** to detect malicious activity.  

### 🛠️ Steps to Scan a URL  
1. Visit [UrlScan.io](https://urlscan.io/).  
2. Enter the **suspicious URL** in the search box.  
3. Click **"Public Scan"** (or **"Private Scan"** for confidential analysis).  
4. Analyze:  
   - **Screenshot** (checks for phishing).  
   - **Outbound requests** (identifies C2 servers).  
   - **Injected scripts** (detects malware payloads).  

### 📌 Example Use Case  
A phishing email contains a **fake PayPal login link**. Scanning it with **UrlScan.io** reveals it’s **hosted on a suspicious server** and contains **keylogging scripts**.  

---

## 🦠 Using Abuse.ch to Track Malware & Botnet Indicators  

### 🔹 What is Abuse.ch?  
[Abuse.ch](https://abuse.ch/) provides **threat intelligence feeds** for tracking malware, botnets, and malicious URLs.  

### 📌 Key Intelligence Feeds  
- **ThreatFox** – IOC database (IPs, domains, hashes).  
- **URLhaus** – Tracks **malware distribution URLs**.  
- **Feodo Tracker** – Monitors **botnet C2 servers**.  

### 🛠️ Steps to Use Abuse.ch  
1. Visit [ThreatFox](https://threatfox.abuse.ch/).  
2. Search for **file hashes, IPs, or domains**.  
3. **Analyze the results** for known threats.  

### 📌 Example Use Case  
You find a **file attachment** in an email. Searching its **SHA256 hash** on **ThreatFox** shows it’s linked to the **Emotet banking trojan**.  

---

## 📧 Investigating Phishing Emails Using PhishTool  

### 🔹 What is PhishTool?  
[PhishTool](https://phishtool.com/) is an advanced phishing analysis platform that extracts email metadata, validates SPF/DKIM, and detects malicious links.  

### 🛠️ Steps to Investigate a Phishing Email  
1. Open **PhishTool** and upload the **phishing email**.  
2. **Analyze metadata**, including:  
   - Sender domain & SPF/DKIM records.  
   - Malicious links & redirections.  
   - Attachment hashes (checks for malware).  
3. Cross-check with **Abuse.ch** or **Cisco Talos**.  

### 📌 Example Use Case  
A "PayPal security alert" email asks for login details. **PhishTool reveals domain spoofing and hidden tracking pixels**, confirming it's phishing.  

---

## 🔎 Using Cisco Talos Intelligence for Threat Intel Gathering  

### 🔹 What is Cisco Talos?  
[Cisco Talos](https://talosintelligence.com/) is a **threat intelligence platform** providing data on malware, DNS reputation, and attack campaigns.  

### 🛠️ Steps to Use Cisco Talos  
1. Go to [Talos Intelligence](https://talosintelligence.com/).  
2. Enter an **IP, domain, or file hash** in the search bar.  
3. **Review the reputation score**:  
   - ✅ **Good** – Likely safe.  
   - ⚠️ **Neutral** – Needs investigation.  
   - ❌ **Malicious** – Associated with cyber threats.  
4. Analyze **historical activity, geolocation, and attack sources**.  

### 📌 Example Use Case  
A **server logs repeated login attempts** from an unknown IP. **Cisco Talos identifies it as a botnet IP**, allowing proactive blocking.  

---

## 🔥 Conclusion & Next Steps  

✔️ Threat Intelligence helps in **proactive cybersecurity defense**.  
✔️ Using **UrlScan.io, Abuse.ch, PhishTool, and Cisco Talos**, we can:  
   ✅ Detect phishing attacks & malware campaigns.  
   ✅ Track botnet activity & malicious indicators.  
   ✅ Strengthen **SOC & Incident Response** workflows.  

---

🚀 **Keep Learning, Keep Hunting!** 🛡️
