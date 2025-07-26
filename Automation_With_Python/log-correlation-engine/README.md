##  Log Correlation Engine

Correlates logs from authentication and process creation events to detect suspicious activity, like lateral movement or privilege escalation.

##  Use Case

Detect scenarios where a user logs in and executes a suspicious binary like `mimikatz.exe` within 5 minutes.

##  Inputs

- `auth_logs.json`: login activity
- `process_logs.json`: process creation logs
- `correlation_rules.yaml`: rules to apply

##  Output

- `output/correlations.json`: list of flagged events

## How to Run

```bash
pip install -r requirements.txt
python correlate.py
