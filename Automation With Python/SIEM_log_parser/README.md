#  SIEM Log Parser for Alert Triage

##  Description

This script parses raw SIEM log exports (e.g. Splunk, Sentinel) from a `.txt` file, extracts key metadata, and identifies suspicious events based on IOC keywords. The result is a structured `.csv` of filtered alerts ready for analyst triage.

##  Use Case

- SOC analyst needs to extract all `powershell`, `wget`, or `curl` commands from SIEM logs.
- Triage team wants to visualize alerts in a clean table.
- Threat detection team wants to feed parsed results to another tool (Excel, SIEM, Jupyter).

##  Files

| File | Description |
|------|-------------|
| `siem_parser.py` | Main script for parsing logs |
| `raw_logs.txt` | Raw SIEM logs (input) |
| `parsed_alerts.csv` | Structured suspicious alerts (output) |
| `README.md` | Project overview |

##  How to Run

```bash
python3 siem_parser.py
