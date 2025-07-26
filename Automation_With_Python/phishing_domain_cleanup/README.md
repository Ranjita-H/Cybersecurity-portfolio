# 🛡️ Phishing Domain Cleanup Tool

## 📌 Description

This Python script helps security analysts automatically clean up a trusted domain allow list by removing known phishing domains. It's designed for use in SOC environments where allowlists are used for email gateway filtering.

It uses:
- `trusted_domains.txt`: current allowlist in use
- `phishing_domains.txt`: list of domains flagged as phishing
- Generates: a cleaned allowlist, a log file, and a backup of the original

## 📁 Files

| File | Description |
|------|-------------|
| `phishing_cleaner.py` | Main script that performs the cleanup |
| `trusted_domains.txt` | Your allowlisted domains (input/output) |
| `phishing_domains.txt` | Known phishing domains to remove |
| `phishing_cleanup.log` | Log file showing all operations |
| `trusted_domains_backup.txt` | Automatically created backup of the original allowlist |

## ▶️ How to Use

1. Clone the repo or copy the files into your project.
2. Update the `trusted_domains.txt` and `phishing_domains.txt` with your actual data.
3. Run the script:

```bash
python3 phishing_cleaner.py
