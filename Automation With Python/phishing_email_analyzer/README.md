#  Phishing Email Analyzer

##  Description

This tool analyzes suspected phishing emails from a CSV file and assigns a **severity score** based on:
- Known phishing keywords
- Suspicious or obfuscated domains
- Spoofed sender patterns (like fake Microsoft/Google addresses)

##  Files

| File | Description |
|------|-------------|
| `phishing_analyzer.py` | Core script to scan emails |
| `suspected_emails.csv` | Input: list of suspected emails |
| `email_analysis_report.csv` | Output: structured report |
| `README.md` | Project overview |

##  How to Run

```bash
python3 phishing_analyzer.py
```

## Scoring Logic
**Indicator**  	**Score**
Keyword match	    +2
Suspicious domain	+3
Spoofed sender	    +3

**Final Score**	 **Severity**
8+	             High
4–7	             Medium
< 4	             Low

## Skills Demonstrated
Email analysis using Python

IOC-based phishing detection

Regex, CSV handling, and scoring logic


