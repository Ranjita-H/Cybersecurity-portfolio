"""
SIEM Log Parser for Alert Triage
Author: Ranjita Hukkeri
Description:
Reads raw log lines from SIEM output, extracts critical fields,
filters irrelevant entries, and exports a structured CSV for triage.
"""

import csv
import re
from datetime import datetime

RAW_LOG_FILE = "raw_logs.txt"
CSV_OUTPUT = "parsed_alerts.csv"
IOC_KEYWORDS = ["powershell", "mimikatz", "curl", "wget", "base64", "C:\\Windows\\Temp"]

def extract_fields(log_line):
    """Extracts timestamp, host, and event details from a log line."""
    try:
        timestamp_match = re.search(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", log_line)
        timestamp = timestamp_match.group() if timestamp_match else "N/A"

        host_match = re.search(r"host=([\w\-.]+)", log_line)
        host = host_match.group(1) if host_match else "unknown"

        event_match = re.search(r"event=([^ ]+)", log_line)
        event = event_match.group(1) if event_match else "none"

        raw_message = log_line.strip()

        return {
            "timestamp": timestamp,
            "host": host,
            "event": event,
            "raw_log": raw_message
        }

    except Exception as e:
        print(f"[!] Error parsing line: {e}")
        return None

def is_suspicious(log):
    """Check if any IOC keyword is present in the raw log line."""
    return any(ioc.lower() in log.lower() for ioc in IOC_KEYWORDS)

def main():
    alerts = []

    with open(RAW_LOG_FILE, "r") as f:
        for line in f:
            if not line.strip():
                continue
            parsed = extract_fields(line)
            if parsed and is_suspicious(parsed["raw_log"]):
                alerts.append(parsed)

    if not alerts:
        print("[+] No suspicious events detected.")
        return

    with open(CSV_OUTPUT, "w", newline="") as csvfile:
        fieldnames = ["timestamp", "host", "event", "raw_log"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for alert in alerts:
            writer.writerow(alert)

    print(f"[+] Parsed {len(alerts)} suspicious logs to {CSV_OUTPUT}")

if __name__ == "__main__":
    main()
