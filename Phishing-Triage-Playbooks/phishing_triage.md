# ✉️ Phishing Triage Sample – Basic Email Header & Payload Analysis

## 📥 Sample Email Indicators
- **From**: hr@companycareers.xyz (spoofed)
- **Subject**: URGENT: Updated Salary Review
- **Attachment**: `SalaryAdjustments.xlsm`
- **Link**: `http://company-secure-login.com`

## 🔍 Step 1: Header Review
- Check `Return-Path`, `Reply-To`, and SPF/DKIM/DMARC results
- Header anomaly: `Received:` header from public mail server (likely spoofed)

## 🛠 Tools Used
- [MXToolbox](https://mxtoolbox.com)
- [Google Admin Toolbox – Messageheader](https://toolbox.googleapps.com/apps/messageheader/)

## 🔬 Step 2: Payload Analysis
- Attachment contains macro-enabled Excel file
- Hash submitted to VirusTotal → Detection: 6/68 engines
- Link redirects to credential-harvesting page (confirmed via URLScan)

## 🧠 IOC Extraction
- SHA256 of file: `f3b3d7e0a913...`
- URL: `company-secure-login.com`
- IP: `185.199.110.153`

## ⚠️ Suggested Automation
Using Python + VirusTotal API:
- Auto extract links and attachments
- Hash & scan via API
- Flag known bad and log unknown for human review

---

