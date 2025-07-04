
## ✉️ Use Case 2 – Phishing Triage: Header & Payload Analysis

### 📌 Objective
Demonstrate structured phishing triage process using:
- Header inspection
- IOC enrichment
- Payload evaluation

### 📥 Scenario Details
- Spoofed email from `hr@companycareers.xyz`
- Subject: “URGENT: Updated Salary Review”
- Attachment: `SalaryAdjustments.xlsm`
- URL in body: `http://company-secure-login.com`

### 🔍 Analysis Steps
1. **Header Review**
   - SPF/DKIM/DMARC fail
   - IP from non-authorized server
   - `Reply-To` mismatch
2. **Payload & Link Review**
   - `.xlsm` file flagged in VirusTotal (6/68 engines)
   - URL redirects to credential-harvesting page (via URLScan)

### 🧠 IOCs Extracted
- SHA256 hash of attachment
- IP address of malicious site
- Suspicious domain

### 🤖 Automation Plan (Python-based)
- Extract links & attachments
- Hash and check via VirusTotal API
- Log unknowns, alert on known-bads


---

## 🔧 Tools & Technologies Used
| Tool | Purpose |
|------|---------|
| Microsoft Sentinel | SIEM + cloud-native detection |
| KQL | Query language for log analysis |
| MITRE ATT&CK | Threat modeling & mapping |
| VirusTotal | File and URL reputation checks |
| MXToolbox | Header and DNS inspection |
| URLScan.io | Website rendering and IOC checking |
| Python (proposed) | Scripting for automation |

---
