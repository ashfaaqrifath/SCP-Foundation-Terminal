<h1 align="center">
  <img width="600" src="scp.png" alt="scp"><br>
</h1>

# SCP Foundation Terminal

> **"Secure. Contain. Protect."**

A Python-based terminal program that scrapes the [SCP Wiki](https://scp-wiki.wikidot.com) to retrieve, display, and save information about SCP objects — wrapped in an immersive, foundation-themed terminal experience with user authentication, activity logging, and security features.

> **Current Version:** v2.1.5

---

## ✨ Features

- 🔍 **SCP Lookup** — Retrieve detailed info on any SCP object directly from the SCP Wiki
- 💾 **Save to File** — Save SCP object data as `.txt` files in the `SCP object files/` folder
- 🔊 **Text-to-Speech** — Read out SCP entries using the speech engine
- 👤 **User Registration & Login** — Register accounts with password authentication
- 🔒 **Emergency Lockout** — Terminal lockout system for security
- 🕶️ **Incognito Mode** — Browse without logging activity
- 📋 **Activity Logging** — All terminal actions logged to `Activity Logs/`
- 🖥️ **Terminal Override** — Admin-level override system
- 🎨 **Colored Output** — Styled terminal UI with color formatting
- 🔐 **Security Features** — Multiple layers of access control

---

## 📁 Project Structure

```
SCP-Foundation-Terminal/
├── Activity Logs/          # Auto-generated session activity logs
├── SCP object files/       # Saved SCP data in .txt format
├── Users/                  # Registered user data
├── scp_terminal.py         # Main terminal entry point
├── scp001.py               # SCP-001 special handler
├── chronicle_engine.py     # Core data retrieval & scraping engine
├── register.py             # User registration module
├── lockout.py              # Emergency lockout handler
├── speech_engine.py        # Text-to-speech module
├── requirements.txt        # Python dependencies
├── scp.png                 # SCP Foundation logo
└── LICENSE
```

---

## ⚙️ Requirements

Python 3.x + the following packages:

```bash
pip install requests bs4 pyttsx3 colorama
```

> `shutil`, `random`, and `datetime` are Python standard library modules — no install needed.

Or install everything at once using the requirements file:

```bash
pip install -r requirements.txt
```

---

## 🚀 Setup & Usage

1. Clone the repo:
   ```bash
   git clone https://github.com/ashfaaqrifath/SCP-Foundation-Terminal.git
   cd SCP-Foundation-Terminal
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Register a new user:
   ```bash
   python register.py
   ```

4. Launch the terminal:
   ```bash
   python scp_terminal.py
   ```

5. Log in and start looking up SCP objects!

---

## 🗂️ How It Works

| File | Role |
|------|------|
| `scp_terminal.py` | Main terminal UI — handles login, commands, and navigation |
| `chronicle_engine.py` | Scrapes SCP Wiki using `requests` + `BeautifulSoup` |
| `register.py` | Handles new user account creation |
| `lockout.py` | Triggers emergency terminal lockout |
| `speech_engine.py` | Reads SCP content aloud using `pyttsx3` |
| `scp001.py` | Special handling for the classified SCP-001 entry |

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Web Scraping:** `requests`, `BeautifulSoup4`
- **TTS:** `pyttsx3`
- **Terminal Styling:** `colorama`
- **Data Source:** [scp-wiki.wikidot.com](https://scp-wiki.wikidot.com)

---

## 🔗 Links

- 🌐 [Portfolio](https://ashfaaqrifath.github.io/)
- 💼 [LinkedIn](https://www.linkedin.com/in/ashfaaqrifath/)
- 🐦 [Twitter](https://twitter.com/ashfaaqrifth)
- 📖 [SCP Wiki](https://scp-wiki.wikidot.com)

---

## 📄 License

MIT — © 2023 Ashfaaq Rifath
