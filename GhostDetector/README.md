# 👻 GhostDetector
> A network and file system monitoring tool to detect Telegram API connections and track file modifications in real-time 📡🔍

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Windows](https://img.shields.io/badge/Platform-Windows-blue.svg)](https://www.microsoft.com/windows)

---

## 🎬 Video Tutorial
<div align="center">
  <a href="https://youtu.be/Y5bDoBET1RM?si=Com5OCmUZrZ1K-iD">
    <br>
    <img src="https://img.shields.io/badge/▶️_Watch_Tutorial-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch Tutorial">
  </a>
  <br>
  <i>👆 Click to watch the full video on YouTube</i>
</div>

---

🎓 This project is part of my YouTube tutorial series on cybersecurity tools and monitoring techniques. I wanted to create something educational that helps people understand network traffic analysis and file system monitoring. The level will increase day by day and I'm pretty sure that it'll be really valuable for everyone! So yeah, feel free to watch this tutorial 🚀

---

🔗 Project
This script builds upon techniques from my previous tutorial! If you haven't watched it yet, <a href="https://github.com/Hghost0x00/GhostLogger">check out GhostLogger 👻</a>

📺 Previous Tutorial: GhostLogger - Keylogger with Telegram Exfiltration
🎯 What it does: Uses Telegram Bot API to exfiltrate keystroke data
💡 Why it matters: GhostDetector can actually detect when GhostLogger communicates with Telegram! 🔍

This creates a full offensive/defensive learning cycle - build the malware, then build the detection tool! 🛡️

---

## ✨ Features

- 🌐 **Telegram API Detection**: Monitors outbound HTTPS traffic to detect connections to Telegram API servers
- 📁 **File Modification Tracking**: Scans and monitors all `.txt` files on the system for changes
- 🔀 **Multi-threaded Operation**: Run both monitoring modules simultaneously
- ⚡ **Real-time Alerts**: Instant notifications when activity is detected

---

## 📋 Requirements

- 💻 Windows OS (requires WinDivert)
- 🐍 Python 3.7 or higher
- 👑 Administrator privileges (required for packet capture)
- 📦 Python packages:
  ```
  pydivert, colorama
  ```

---

## 🚀 Installation

### 1️⃣ Clone the Repository 📥
```bash
git clone https://github.com/Hghost0x00/Ghost.git
cd GhostDetector
```

### 2️⃣ Install Dependencies 💾
```bash
pip install pydivert colorama
```

### 3️⃣ Install WinDivert Driver 🔧
1. Download from [WinDivert official site](https://www.reqrypt.org/windivert.html) 📥
2. Extract the archive and run the installer 🛠️
3. Follow the installation instructions for your system ✅

---

## 🎮 Usage

### Starting GhostDetector ▶️

⚠️ **Important**: Run as Administrator!

```bash
python ghostdetector.py
```

### Menu Options 🎯

```
[1] Start Telegram Detection       - Monitor network traffic for Telegram API 🌐
[2] Start File Creation Analysis   - Track .txt file modifications 📝
[3] Start Both                     - Run both modules concurrently 🔀
[0] Exit                          - Close the application 🚪
```

### How It Works 🔍

#### 📡 Telegram Detection Module
- Captures outbound TCP traffic on port 443 (HTTPS) 🔐
- Filters packets destined for known Telegram API IP addresses 🎯
- Alerts when Telegram API communication is detected ⚡

#### 📂 File Analysis Module
- Enumerates all `.txt` files starting from C:\ drive 🗂️
- Monitors file sizes at 0.5-second intervals ⏱️
- Logs any detected size changes indicating file modification 📊

---

## ⚠️ Important Notes

- 👑 **Administrator Rights Required**: The packet capture functionality requires elevated privileges
- ⚡ **Performance Impact**: Scanning entire file systems can be resource-intensive on systems with many files
- 📚 **Educational Purpose**: This tool is for educational and legitimate security research purposes only

---

## 📝 License

This project is provided as-is for personal use. Feel free to modify and distribute! ✨

---

## ⚖️ Legal Disclaimer

This tool is provided for **educational purposes** and **legitimate security testing** only. Users are responsible for complying with all applicable laws and regulations. Unauthorized monitoring of network traffic or file systems may be illegal in your jurisdiction. Always ensure you have proper authorization before using this tool. 🔒

---

## 👤 Author

**Hghost010** 🧑‍💻
- GitHub: [@Hghost0x00](https://github.com/Hghost0x00)

---

## 🌟 Show Your Support

Give a ⭐️ if this project helped you!

---

<div align="center">

**Made with 👻 by Hghost010**

*Detect like a ghost, monitor like a pro.* 🔮

</div>
