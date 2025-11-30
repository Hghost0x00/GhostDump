# 👻 GhostLogger
> A keylogger using Telegram to exfiltrate the dumped keystrokes 📡

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Telegram Bot API](https://img.shields.io/badge/Telegram%20Bot%20API-Latest-blue.svg)](https://core.telegram.org/bots/api)

---

## 🎬 Video Tutorial

<div align="center">
  <a href="https://www.youtube.com/watch?v=_PysGRksbGQ">
    <br>
    <img src="https://img.shields.io/badge/▶️_Watch_Episode_1-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch Episode 1">
  </a>
  <br>
  <i>👆 Building GhostLogger - The Original Tutorial</i>
</div>

<div align="center">
  <a href="https://www.youtube.com/watch?v=4fvQoriTH7c&t=319s">
    <br>
    <img src="https://img.shields.io/badge/▶️_Watch_Episode_2-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch Episode 2">
  </a>
  <br>
  <i>👆 GhostLogger 2.0 - Upgrade, Test & Compile</i>
</div>


---

🎓 This project is part of my first YouTube tutorial. I tried to make something as simple as possible to help anyone diving into the malware development world. The level will increase day by day and I'm pretty sure that it'll be really valuable for everyone, even me, because it forces me to think about how I can create this or that for a tutorial. So yeah, feel free to watch this tutorial 🚀

---

## 📋 Requirements
- 🐍 Python 3.7 or higher
- 📦 Python packages:
  ```
  python-telegram-bot, keyboard
  ```

---

## 🚀 Installation

### 1️⃣ Clone the Repository 📥
```bash
git clone https://github.com/Hghost0x00/GhostLogger.git
cd GhostLogger
```

### 2️⃣ Install Dependencies 💾
```bash
pip install python-telegram-bot keyboard
```

### 3️⃣ Get Your Telegram Bot Token 🤖
1. Open Telegram and message [@BotFather](https://t.me/botfather) 💬
2. Send `/newbot` and follow the prompts ✅
3. Choose a name (e.g., "GhostDump Bot") 📝
4. Copy the token you receive 🔑

### 4️⃣ Configure Your Bot ⚙️
Update the `TOKEN` variable in the code:
```python
TOKEN = "telegram_bot_token"
```

---

## 🎮 Usage

### Starting the KeyLogger ▶️
```bash
python ghostlogger.py
```

⌨️ Type some words or whatever using your keyboard. You'll see that every single keystroke is written to the test.txt file. Moreover, start the Telegram bot and see that you've dumped the test.txt file! 📄✨

---

## 📦 Compiling with PyInstaller

### Install PyInstaller 🔧
```bash
pip install pyinstaller
```

### Compile to Executable 🛠️

#### Basic Compilation 🔨
```bash
pyinstaller --onefile ghostlogger.py
```

#### Advanced Compilation (No Console Window) 🥷
```bash
pyinstaller --onefile --noconsole --icon=ghost.ico ghostlogger.py
```

#### Recommended Options ⭐
```bash
pyinstaller --onefile --noconsole --name GhostLogger --clean ghostlogger.py
```

### PyInstaller Options Explained 📖
- `--onefile`: Creates a single executable file 📄
- `--noconsole`: Runs without showing a console window (stealth mode) 🤫
- `--icon=ghost.ico`: Adds a custom icon to the executable 🎨
- `--name GhostLogger`: Specifies the name of the output executable 🏷️
- `--clean`: Cleans PyInstaller cache before building 🧹

### Find Your Executable 📂
After compilation, your executable will be located in the `dist/` folder:
```
GhostLogger/
├── dist/
│   └── GhostLogger.exe 💻
├── build/
└── ghostlogger.spec
```

---

## 📝 License
This project is provided as-is for personal use. Feel free to modify and distribute! ✨

---

## 👤 Author
**Hghost010** 🧑‍💻

---

## 🌟 Show Your Support
Give a ⭐️ if this project helped you!

---

<div align="center">

**Made with 👻 by Hghost010**

*Backup like a ghost, restore like a pro.* 🔮

</div>
