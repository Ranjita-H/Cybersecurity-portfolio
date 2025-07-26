import json
import yaml
import os

DATA_DIR = "data"
OUTPUT_FILE = "output/correlations.json"
RULES_FILE = "rules/correlation_rules.yaml"

def load_logs():
    logs = {}
    for filename in os.listdir(DATA_DIR):
        if filename.endswith(".json"):
            with open(os.path.join(DATA_DIR, filename)) as f:
                logs[filename] = json.load(f)
    return logs

def load_rules():
    with open(RULES_FILE) as f:
        return yaml.safe_load(f)

def correlate(logs, rules):
    results = []
    for rule in rules:
        r_type = rule['type']
        description = rule['description']
        if r_type == 'lateral_movement':
            for auth in logs.get("auth_logs.json", []):
                if auth['status'] == "failed":
                    for proc in logs.get("process_logs.json", []):
                        if proc['user'] == auth['user'] and proc['timestamp'] > auth['timestamp']:
                            results.append({
                                "type": r_type,
                                "description": description,
                                "details": {
                                    "auth_event": auth,
                                    "process_event": proc
                                }
                            })
        elif r_type == 'data_exfiltration':
            for fw in logs.get("firewall_logs.json", []):
                if fw['action'] == "allow" and fw['destination_ip'] not in rule.get("internal_ips", []):
                    results.append({
                        "type": r_type,
                        "description": description,
                        "details": fw
                    })
        # Add more rules here...
    return results

def save_results(results):
    os.makedirs("output", exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(results, f, indent=4)

if __name__ == "__main__":
    logs = load_logs()
    rules = load_rules()
    correlated_events = correlate(logs, rules)
    save_results(correlated_events)
    print(f"[+] Correlation complete. {len(correlated_events)} suspicious events saved to {OUTPUT_FILE}")
