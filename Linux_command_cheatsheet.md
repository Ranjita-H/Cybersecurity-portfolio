# 🖥️ Linux Command Cheat Sheet  

This is a **quick reference guide** for essential Linux commands, categorized for easy lookup. Useful for **log analysis, filtering, and automation** in cybersecurity and system administration.  

## 📌 Table of Contents  
- [🔰 Basics](#-basics)  
- [📖 Reading Files](#-reading-files)  
- [🔍 Find & Filter](#-find--filter)  
- [⚙️ Advanced Commands](#-advanced-commands)  
- [🚀 Special Use Cases](#-special-use-cases)  

---

## 🔰 Basics  

| **Command** | **Description** |  
|------------|---------------|  
| history | View command history |  
| !10 | Execute the 10th command in history |  
| !! | Execute the previous command |  

---

## 📖 Reading Files  

| **Command** | **Description** |  
|------------|---------------|  
| cat sample.txt | Read the entire file |  
| head sample.txt | Read the first 10 lines |  
| tail sample.txt | Read the last 10 lines |  

---

## 🔍 Find & Filter  

| **Command** | **Description** |  
|------------|---------------|  
| cat test.txt | cut -f 1 | Cut the 1st field |  
| cat test.txt | cut -c1 | Cut the 1st column |  
| cat test.txt | grep 'keywords' | Filter specific keywords |  
| cat test.txt | sort | Sort output alphabetically |  
| cat test.txt | sort -n | Sort output numerically |  
| cat test.txt | uniq | Remove duplicate lines |  
| cat test.txt | wc -l | Count line numbers |  
| cat test.txt | nl | Show line numbers |  

---

## ⚙️ Advanced Commands  

| **Command** | **Description** |  
|------------|---------------|  
| cat test.txt | sed -n '11p' | Print line 11 |  
| cat test.txt | sed -n '10,15p' | Print lines between 10-15 |  
| cat test.txt | awk 'NR < 11 {print $0}' | Print lines below 11 |  
| cat test.txt | awk 'NR == 11 {print $0}' | Print line 11 |  

---

## 🚀 Special Use Cases  

| **Command** | **Description** |  
|------------|---------------|  
| cat signatures.log | zeek-cut uid src_addr dst_addr | Filter specific fields in Zeek logs |  
| sort | uniq | Remove duplicate values |  
| sort | uniq -c | Remove duplicates & count occurrences |  
| sort -nr | Sort values numerically |  
| rev | Reverse string characters |  
| cut -f 1 | Cut the first field |  
| cut -d '.' -f 1-2 | Split string at . and keep first 2 fields |  
| grep -v 'test' | Display lines that don't match "test" |  
| grep -v -e 'test1' -e 'test2' | Display lines that don't match "test1" or "test2" |  
| file | View file type & metadata |  
| grep -rin Testvalue1 * | column -t | less -S | Search recursively, format output in columns & view with less |  



