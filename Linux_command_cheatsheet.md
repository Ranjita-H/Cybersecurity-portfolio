# Zeek & Linux Command Reference Guide

This section provides a **comprehensive reference guide** for essential **Zeek and Linux commands** used in network security monitoring, log analysis, and system administration.

---

## 🗂 Categories Overview

| Category         | Command Purpose and Usage |
|-----------------|--------------------------|
| **Basics**      | Commonly used shell commands |
| **Read File**   | Commands to read and view file contents |
| **Find & Filter** | Filtering, sorting, and extracting data from logs/files |
| **Advanced**    | Advanced text processing techniques |
| **Special**     | Zeek-specific commands for analyzing network logs |

---

## 📌 Command Reference Table

### 🔹 **Basics**
| Command | Description |
|---------|-------------|
| `history` | View command history |
| `!10` | Execute the 10th command in history |
| `!!` | Execute the previous command |

---

### 📄 **Read File**
| Command | Description |
|---------|-------------|
| `cat sample.txt` | Read the content of `sample.txt` |
| `head sample.txt` | View the first 10 lines of the file |
| `tail sample.txt` | View the last 10 lines of the file |

---

### 🔎 **Find & Filter**
| Command | Description |
|---------|-------------|
| `cat test.txt \| cut -f 1` | Cut the 1st field |
| `cat test.txt \| cut -c1` | Cut the 1st column |
| `cat test.txt \| grep 'keyword'` | Filter specific keywords |
| `cat test.txt \| sort` | Sort output alphabetically |
| `cat test.txt \| sort -n` | Sort output numerically |
| `cat test.txt \| uniq` | Eliminate duplicate lines |
| `cat test.txt \| wc -l` | Count number of lines |
| `cat test.txt \| nl` | Show line numbers |

---

### ⚡ **Advanced**
| Command | Description |
|---------|-------------|
| `cat test.txt \| sed -n '11p'` | Print line 11 |
| `cat test.txt \| sed -n '10,15p'` | Print lines between 10-15 |
| `cat test.txt \| awk 'NR < 11 {print $0}'` | Print lines below 11 |
| `cat test.txt \| awk 'NR == 11 {print $0}'` | Print line 11 |

---

### 🌐 **Special (Zeek Log Analysis)**
| Command | Description |
|---------|-------------|
| `cat signatures.log \| zeek-cut uid src_addr dst_addr` | Extract specific fields from Zeek logs |

---

## 📊 **Use Cases & Practical Examples**
| Use Case | Description |
|---------|-------------|
| `sort \| uniq` | Remove duplicate values |
| `sort \| uniq -c` | Remove duplicates and count occurrences |
| `sort -nr` | Sort values numerically and recursively |
| `rev` | Reverse string characters |
| `cut -f 1` | Extract field 1 |
| `cut -d '.' -f 1-2` | Extract first two fields separated by `.` |
| `grep -v 'test'` | Display lines that do not contain "test" |
| `grep -v -e 'test1' -e 'test2'` | Exclude lines containing "test1" or "test2" |
| `file filename` | View file type and details |
| `grep -rin Testvalue1 * \| column -t \| less -S` | Search for "Testvalue1" and format output with column alignment |

---

