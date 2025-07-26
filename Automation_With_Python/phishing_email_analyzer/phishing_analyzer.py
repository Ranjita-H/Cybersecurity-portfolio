"""
Phishing Email Analyzer
Author: Ranjita Hukkeri
Description:
Scans a CSV of suspected emails and flags indicators of phishing.
Generates an analysis report with severity score and explanation.
"""

import csv
import re

INPUT_FILE = "suspected_emails.csv"
OUTPUT_FILE = "email_analysis_report.csv"

PHISHING_KEYWORDS = [
    "verify your account", "reset password", "suspended", "click here", "urgent action",
    "login immediately", "unauthorized access", "you have won", "update billing",
    "credential", "OTP", "bank", "limited time", "security alert"
]

SUSPICIOUS_DOMAINS = [
    "bit.ly", "tinyurl", ".xyz", ".top", ".click", "goog1e", "paypal-secure", "login-microsoft"
]

def score_email(subject, body, sender):
    score = 0
    reasons = []

    full_text = f"{subject} {body}".lower()

    # Keyword matches
    for keyword in PHISHING_KEYWORDS:
        if keyword in full_text:
            score += 2
            reasons.append(f"Keyword match: '{keyword}'")

    # Suspicious domains
    for domain in SUSPICIOUS_DOMAINS:
        if domain in full_text:
            score += 3
            reasons.append(f"Suspicious domain: '{domain}'")

    # Spoofed sender checks
    if "@" in sender:
        domain = sender.split("@")[1]
        if re.match(r"(support|admin|security)[\.\-_]?(google|microsoft|paypal)\.com", domain, re.IGNORECASE):
            score += 3
            reasons.append(f"Spoofed trusted sender domain: '{domain}'")

    severity = "Low"
    if score >= 8:
        severity = "High"
    elif score >= 4:
        severity = "Medium"

    return score, severity, "; ".join(reasons)

def main():
    results = []

    with open(INPUT_FILE, "r") as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            subject = row.get("Subject", "")
            body = row.get("Body", "")
            sender = row.get("From", "")
            score, severity, explanation = score_email(subject, body, sender)

            results.append({
                "Subject": subject,
                "From": sender,
                "Score": score,
                "Severity": severity,
                "Indicators": explanation
            })

    with open(OUTPUT_FILE, "w", newline="") as outfile:
        fieldnames = ["Subject", "From", "Score", "Severity", "Indicators"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in results:
            writer.writerow(row)

    print(f"[+] Analysis complete. Report saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
