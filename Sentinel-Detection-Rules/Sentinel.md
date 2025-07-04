# 🛡️ Microsoft Sentinel Detection Rule – Suspicious PowerShell Usage

## 🔍 Purpose
Detect potentially malicious PowerShell activity that could indicate early-stage attack behavior such as privilege escalation, credential dumping, or lateral movement.

## 📌 Mapped to MITRE ATT&CK
- **Technique**: T1059.001 – PowerShell
- **Tactic**: Execution

## 🔎 KQL Detection Query
```kql
DeviceProcessEvents
| where FileName =~ "powershell.exe"
| where ProcessCommandLine has_any ("-EncodedCommand", "Invoke-Expression", "IEX", "DownloadString", ".Invoke")
| extend Command = tostring(ProcessCommandLine)
| project Timestamp, DeviceName, InitiatingProcessAccountName, Command
```

## ✅ Explanation
- Filters for PowerShell executions
- Flags obfuscated or suspicious commands often used in attacks
- Can be tuned with allowlist of approved scripts

## 🔧 Suggested Action
- Correlate with user context and device risk
- Trigger alert with Medium/High severity if run by a non-admin or outside working hours
- Review against allowlisted scripts or approved jobs

---


