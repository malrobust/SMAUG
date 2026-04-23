# Sifra | Autonomous Security Researcher 🛡️

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Ollama](https://img.shields.io/badge/Powered%20by-Ollama-orange.svg)](https://ollama.ai/)

**Sifra** (Hebrew for *Cipher*) is a high-performance, autonomous AI agent designed for security research, vulnerability assessment, and systemic analysis. Powered by local LLMs via Ollama, Sifra enables security professionals to automate complex workflows without leaking sensitive data to external APIs.

---

## 🌟 Features

- **Autonomous ReAct Engine**: Employs a sophisticated Reasoning-Action loop to solve complex tasks.
- **Security-First Planning**: Automatically decomposes high-level objectives into executable security modules.
- **Voice-Enabled Interface**: Optional voice command and response system for hands-free operation.
- **Local-First Architecture**: Your data stays on your machine. Leveraging Ollama for private, local LLM execution.
- **Modular Toolset**: Expandable tools for web crawling, network scanning, and vulnerability discovery.
- **Rich Terminal UI**: A premium console experience with live status updates and markdown rendering.

## 🚀 Quick Start

### Prerequisites

- [Python 3.10+](https://www.python.org/downloads/)
- [Ollama](https://ollama.ai/) (Running locally)
- [Optional] `pyaudio` (For voice support)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/sifra.git
   cd sifra
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the agent**:
   ```bash
   cp config.yaml.example config.yaml
   # Edit config.yaml with your preferred model and safety scope
   ```

4. **Launch Sifra**:
   ```bash
   python3 main.py
   ```

## 🛠️ Configuration

Edit `config.yaml` to define your operational boundaries:

```yaml
security:
  scope:
    - "localhost"
    - "testphp.vulnweb.com"
  blocked_commands:
    - "rm -rf /"
```

## ⚠️ Disclaimer

Sifra is intended for **authorized security testing and educational purposes only**. The user is solely responsible for compliance with local and international laws. Unauthorized access to computer systems is illegal.

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for details.

## 📄 License

Sifra is released under the [MIT License](LICENSE).
