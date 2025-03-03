# TShark Command-Line Packet Analysis

TShark is a powerful command-line tool for packet analysis, ideal for data carving, automation, and in-depth investigations. This documentation provides essential commands and usage examples to enhance your network traffic analysis.

---

## 📌 Overview
TShark, the command-line version of Wireshark, allows users to:
- Capture and analyze network traffic
- Filter packets efficiently using predefined syntax or Berkeley Packet Filters (BPF)
- Automate tasks and integrate with other tools

---

## 🛠 Commonly Used Tools
| Tool | Purpose |
|------|---------|
| `capinfos` | Provides details about a capture file |
| `grep` | Searches plain-text data |
| `cut` | Extracts sections of lines |
| `uniq` | Filters repeated lines/values |
| `nl` | Displays line numbers |
| `sed` | Stream editor for text manipulation |
| `awk` | Scripting language for pattern search & processing |

---

## ⚙️ Basic Commands

| Command | Purpose |
|---------|---------|
| `tshark -h` | Display help page |
| `tshark -v` | Show version info |
| `tshark -D` | List available interfaces |
| `tshark -i <interface>` | Capture live traffic on the specified interface |
| `tshark` | Sniff traffic like tcpdump |

---

## 🎯 Sniffing & Reading Capture Files

| Command | Purpose |
|---------|---------|
| `tshark -r <file.pcap>` | Read a capture file |
| `tshark -c <num>` | Stop after capturing a specified number of packets |
| `tshark -w <file.pcap>` | Save captured traffic to a file |
| `tshark -V` | Show detailed packet information |
| `tshark -q` | Suppress output (silent mode) |
| `tshark -x` | Display packet bytes in hex & ASCII |

---

## ⏳ Capture Conditions

| Command | Purpose |
|---------|---------|
| `tshark -w test.pcap -a duration:10` | Capture for 10 seconds and save to file |
| `tshark -w test.pcap -a filesize:100` | Stop capture after 100KB file size |
| `tshark -w test.pcap -a files:3` | Stop after creating 3 files |
| `tshark -w test.pcap -b duration:10` | Infinite loop, new file every 10 sec |
| `tshark -w test.pcap -b filesize:100` | New file every 100KB |
| `tshark -w test.pcap -b filesize:100 -b files:3` | Rotate files after 3 captures |

---

## 🛑 Packet Filtering
TShark provides two types of filtering:
1. **Capture Filters (`-f`)** - Applied before capturing traffic
2. **Display Filters (`-Y`)** - Applied after capture to refine output

### Capture Filters

| Command | Purpose |
|---------|---------|
| `tshark -f "host 10.10.10.10"` | Capture traffic to/from specific host |
| `tshark -f "net 192.168.1.0/24"` | Capture traffic from a subnet |
| `tshark -f "port 80"` | Capture traffic on a specific port |
| `tshark -f "tcp"` | Capture only TCP traffic |

### Display Filters

| Command | Purpose |
|---------|---------|
| `tshark -Y "ip.addr == 10.10.10.10"` | Filter packets with specific IP |
| `tshark -Y "tcp.port == 80"` | Show traffic on port 80 |
| `tshark -Y "http"` | Display HTTP packets only |
| `tshark -Y "dns.qry.type == 1"` | Show only DNS A record queries |

---

## 🔍 Example Use Cases
### Capture and Save Traffic for 30 Seconds
```bash
tshark -i eth0 -w capture.pcap -a duration:30
```
### Filter Traffic for Specific IP and Save
```bash
tshark -i eth0 -f "host 192.168.1.1" -w filtered_capture.pcap
```
### Read and Display Only TCP Packets
```bash
tshark -r capture.pcap -Y "tcp"
```
### Monitor HTTP Traffic in Real-Time
```bash
tshark -i eth0 -Y "http"
```

---

## 📖 Additional Resources
- [Wireshark Display Filter Reference](https://www.wireshark.org/docs/dfref/)
- [TShark Manual](https://www.wireshark.org/docs/man-pages/tshark.html)

