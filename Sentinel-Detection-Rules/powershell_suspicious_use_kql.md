
## 🔐 Use Case 1 – Sentinel Detection Rule: Suspicious PowerShell Activity

### 📌 Objective
Detect potentially malicious use of PowerShell (e.g., obfuscated commands, encoded payloads) within a cloud or endpoint environment monitored by Microsoft Sentinel.

### 🧠 Mapped to MITRE ATT&CK
- **Technique ID**: T1059.001
- **Name**: PowerShell
- **Tactic**: Execution

### 🔎 KQL Rule Snippet
```kql
DeviceProcessEvents
| where FileName =~ "powershell.exe"
| where ProcessCommandLine has_any ("-EncodedCommand", "Invoke-Expression", "IEX", "DownloadString", ".Invoke")
| extend Command = tostring(ProcessCommandLine)
| project Timestamp, DeviceName, InitiatingProcessAccountName, Command
```

### ✅ What This Rule Does
- Looks for PowerShell executions on a device
- Flags suspicious indicators common in malware or red team simulation
- Can be enhanced with user risk, allowlists, time-of-day logic

### 💡 Sample Actions
- Escalate if invoked by non-admin outside working hours
- Correlate with other signals (e.g., Defender alert or lateral movement)
- Create automated incident with playbook trigger in Sentinel

---
