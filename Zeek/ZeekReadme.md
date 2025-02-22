# Zeek Network Security Monitor  

[![Zeek](https://img.shields.io/badge/Zeek-Network%20Monitoring-orange)](https://zeek.org/)  
[![License](https://img.shields.io/badge/License-BSD--3--Clause-blue)](https://opensource.org/licenses/BSD-3-Clause)  
[![GitHub Release](https://img.shields.io/github/v/release/zeek/zeek?color=green)](https://github.com/zeek/zeek/releases)  

## 📌 Introduction  

[Zeek](https://zeek.org/) (formerly Bro) is an advanced **open-source network security monitoring** tool designed for **passive network analysis, anomaly detection, and log generation**. It is widely used in **security operations centers (SOC)** and by **threat hunters** to monitor and analyze network traffic at scale.

Unlike traditional IDS systems like **Snort** or **Suricata**, Zeek is a **network traffic analyzer** that enables deep packet inspection and provides **rich logs** for security investigations.

---

## 🚀 Features  

✅ **Deep Packet Inspection (DPI)** for application-layer analysis  
✅ **Network Traffic Logging** (HTTP, DNS, SSL, SSH, etc.)  
✅ **Customizable Event Scripting** with Zeek's powerful scripting language  
✅ **Anomaly Detection & Threat Hunting**  
✅ **Integration with ELK, Splunk, SIEMs** for log analysis  
✅ **Scalability** - Can handle high-volume traffic in enterprise environments  

---

## 📥 Installation Guide  

### 🏗️ Prerequisites  
Ensure your system meets the following requirements:  

- **Linux** (Ubuntu/Debian, CentOS, Fedora) or **macOS**  
- **GCC 8+**, **CMake 3.12+**, **Python 3.6+**  
- **Libpcap, OpenSSL**  
- **Bash & Make**  
- **Root/Sudo Access**  

### 🔧 Installing Zeek  

#### **1️⃣ Using Precompiled Packages (Recommended)**  
For **Ubuntu/Debian**:  
```bash
sudo apt update
sudo apt install zeek -y
```
For **CentOS/Fedora**:  
```bash
sudo yum install epel-release -y
sudo yum install zeek -y
```

#### **2️⃣ Installing from Source**  
```bash
git clone --recursive https://github.com/zeek/zeek.git
cd zeek
./configure
make -j$(nproc)
sudo make install
```
Verify installation:  
```bash
zeek -v
```

---

## 🎯 Basic Usage  

### ✅ **Start Capturing Live Traffic**  
```bash
sudo zeek -i eth0
```
_(Replace `eth0` with your network interface.)_  

### ✅ **Analyze a PCAP File**  
```bash
zeek -r sample.pcap
```
Generates log files like:  
```bash
conn.log  # Connection logs
http.log  # HTTP traffic logs
dns.log   # DNS queries
ssl.log   # SSL/TLS activity
weird.log # Anomalous traffic
```

### ✅ **Viewing Logs**  
```bash
cat conn.log | less
```
or convert logs to JSON format:  
```bash
zeek-cut < conn.log | jq .
```

---

## ⚙️ Configuration & Management  

Zeek uses `zeekctl` for centralized configuration.  

### **1️⃣ Edit `node.cfg` for Multi-Node Deployment**  
```ini
[logger]
type=logger
host=localhost

[manager]
type=manager
host=localhost

[worker-1]
type=worker
host=localhost
interface=eth0
```

### **2️⃣ Start/Stop Zeek**  
```bash
sudo zeekctl deploy
sudo zeekctl start
sudo zeekctl stop
```

---

## 🔥 Zeek Scripting  

Zeek uses a **powerful scripting language** for custom detections.  

### **Basic Example: Detecting Large Downloads**  
Create `large_download.zeek`:  
```zeek
event http_reply(c: connection, msg: http_msg) {
    if ( msg$status_code == 200 && msg$body_length > 10000000 ) {
        print fmt("Large download detected: %s -> %s", c$id$orig_h, c$id$resp_h);
    }
}
```
Run the script:  
```bash
zeek -i eth0 large_download.zeek
```

### **Using Zeek Package Manager (zkg)**  
Install community plugins:  
```bash
zkg install zeek/spicy
```
List installed packages:  
```bash
zkg list
```

---

## 📊 Integration with ELK Stack (Elasticsearch, Logstash, Kibana)  

### **1️⃣ Install Filebeat for Log Shipping**  
```bash
sudo apt install filebeat -y
```

### **2️⃣ Configure Filebeat to Process Zeek Logs**  
Edit `/etc/filebeat/filebeat.yml`:  
```yaml
filebeat.inputs:
  - type: log
    paths:
      - "/usr/local/zeek/logs/current/*.log"
    fields:
      log_type: zeek
```
Start Filebeat:  
```bash
sudo systemctl start filebeat
```

---

## 🐳 Running Zeek in Docker  

Use the official **Zeek Docker image** for containerized deployments.  

### **1️⃣ Pull the Zeek Image**  
```bash
docker pull zeekurity/zeek
```

### **2️⃣ Run Zeek on an Interface**  
```bash
docker run --net=host --rm -it zeekurity/zeek zeek -i eth0
```

### **3️⃣ Analyze a PCAP File**  
```bash
docker run --rm -v $(pwd):/pcap zeekurity/zeek zeek -r /pcap/sample.pcap
```

---

## 🌩️ Deploying Zeek on Cloud (AWS, Azure, GCP)  

### **AWS Deployment**  
1️⃣ Create an **EC2 Instance** (Ubuntu 20.04)  
2️⃣ Attach a network interface for packet capture  
3️⃣ Install Zeek  
```bash
sudo apt install zeek -y
```
4️⃣ Run on the correct interface  
```bash
sudo zeek -i ens5
```

---

## 🛡️ Real-World Security Use Cases  

### **1️⃣ Detecting Malware C2 Communication**  
Monitor **suspicious DNS queries** to known bad domains.  
```bash
cat dns.log | grep -i "malicious.com"
```

### **2️⃣ Detecting SSH Brute-Force Attacks**  
Analyze SSH connection failures.  
```bash
cat ssh.log | grep -i "authentication failed"
```

### **3️⃣ Identifying Expired or Weak SSL Certificates**  
Check SSL certificate expiry in `ssl.log`.  
```bash
cat ssl.log | awk '{print $3, $4, $5}'
```

---

## 📈 Performance Tuning  

### **1️⃣ Optimize Log Storage**  
```bash
sudo sed -i 's/#CompressLogs=yes/CompressLogs=no/' /usr/local/zeek/etc/zeekctl.cfg
```

### **2️⃣ Increase Open File Limits**  
```bash
ulimit -n 100000
```

### **3️⃣ Run Zeek with Multiple Workers**  
```bash
zeek -i eth0 -C -w 4
```

---

## 📚 Additional Resources  
- [Zeek Official Documentation](https://docs.zeek.org/en/current/)  
- [Zeek GitHub Repository](https://github.com/zeek/zeek)  
- [Zeek Scripts Repository](https://github.com/zeek/scripts)  

---
