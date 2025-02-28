# 🔒 Burp Suite Security Testing Project

## Overview
This repository contains **Burp Suite security testing scripts and automation tools** to analyze and improve web application security. It includes custom extensions, payload generators, proxy log parsers, and a sample vulnerability report.

## 🚀 Features
- **Passive Scanner Extension**: Detects sensitive data exposure (API keys, tokens, secrets).
- **Intruder Payload Generator**: Creates brute-force/fuzzing payloads for security testing.
- **Proxy Log Parser**: Extracts URLs and parameters from Burp Suite proxy logs.
- **Vulnerability Report**: Real-world findings from a security assessment.

## 🛠 Tools & Technologies
- **Burp Suite**: Web security testing framework.
- **Python**: Used for scripting and automation.
- **Regular Expressions (Regex)**: Pattern-matching in HTTP responses.
- **JSON Parsing**: Analyzing Burp Suite logs.

## 📜 Scripts
| Script | Description |
|--------|------------|
| `burp_extension.py` | Custom Burp Suite BApp extension for passive scanning. |
| `payload_generator.py` | Generates attack payloads for Burp Intruder. |
| `proxy_log_parser.py` | Extracts URLs & parameters from Burp Proxy logs. |

## 🔧 Installation & Usage
### **1️⃣ Install Burp Suite Community/Professional**
Download Burp Suite from [PortSwigger](https://portswigger.net/burp).

### **2️⃣ Install Dependencies**
Ensure Python 3 is installed and install necessary libraries:
```bash
pip install requests

