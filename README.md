<p align="center">
  <img src="smaug_logo.png" width="400" alt="SMAUG Logo">
</p>

# <h1 align="center">🛡️ SMAUG: Autonomous Security platform</h1>

<p align="center">
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-orange.svg" alt="License: MIT"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10+-orange.svg" alt="Python Version"></a>
  <a href="https://ollama.ai/"><img src="https://img.shields.io/badge/AI-Ollama%20%2F%20Gemma%2030B-orange" alt="Powered by Ollama"></a>
  <a href="https://github.com/malrobust/SMAUG/actions/workflows/ci.yml"><img src="https://github.com/malrobust/SMAUG/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://github.com/malrobust/SMAUG/stargazers"><img src="https://img.shields.io/github/stars/malrobust/SMAUG?style=social" alt="GitHub Stars"></a>
</p>

**Smaug** is a terminal-based autonomous security researcher. It uses Local LLMs to reason through security objectives and orchestrate specialized tools to identify and report vulnerabilities.

## 🏛️ Core Architecture

Smaug operates on a **Reasoning-Action-Observation** loop (ReAct), powered by the **Livion Engine**.

```mermaid
graph TD
    User([User Objective]) --> Loop{Reasoning Loop}
    Loop --> |Think| Thought[Conceptual Strategy]
    Loop --> |Action| Tool[Tool Execution]
    Loop --> |Memory| Mem[ChromaDB Vector Store]
    Tool --> Observation[Security Findings]
    Observation --> Loop
    Loop --> |Complete| Final[Security Report]
```

## ⚡ Integrated Capabilities

| Category | Capability | Tools |
| :--- | :--- | :--- |
| **Intelligence** | Subdomain & Tech Discovery | Amass, HTTPX, WhatWeb |
| **Scanning** | Port & Vulnerability Analysis | Nmap, Nuclei, FFUF |
| **Exploitation** | Managed Vulnerability Checks | SQLMap, Dalfox |
| **Memory** | Semantic Search Persistence | ChromaDB |
| **Execution** | System & Shell Control | Subprocess, File I/O |

## 🚀 Installation & Setup

### Prerequisites
- Python 3.10+
- [Ollama](https://ollama.ai/)

### Setup
```bash
git clone https://github.com/malrobust/SMAUG.git
cd SMAUG
pip install -r requirements.txt
python3 smaug_setup.py
```

### Usage
```bash
python3 main.py
```
**Example Objective**: `smaug > audit testphp.vulnweb.com for SQL vulnerabilities and generate a report`

## 🛠️ Operational Scope
Security boundaries are enforced in `config.yaml`:
```yaml
security:
  scope:
    - "testphp.vulnweb.com"
  blocked_commands:
    - "rm -rf /"
```

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.

---
**Disclaimer**: Smaug is for authorized security research only. Unauthorized testing is illegal.
