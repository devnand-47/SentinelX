# SentinelX
🛡️ Active Defense System for Discord. Automatically detects and neutralizes "Nuking" attempts and Raids using behavioral analysis
<div align="center">

  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=000000,300000,ff0000&height=220&section=header&text=SentinelX&fontSize=80&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=Enterprise%20Grade%20Discord%20Security%20%7C%20Anti-Nuke%20System&descAlignY=60&descSize=20" width="100%"/>

  <p>
    <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/Discord.py-2.0+-5865F2?style=for-the-badge&logo=discord&logoColor=white" />
    <img src="https://img.shields.io/badge/Security-High-red?style=for-the-badge&logo=kalilinux&logoColor=white" />
    <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
  </p>

</div>

---

### 🛡️ About The Project
**SentinelX** is an advanced, asynchronous Discord security bot designed to protect communities from "Nuking" attempts, Raids, and malicious admins.
⚠️ Disclaimer
This tool is for defensive purposes only. It is designed to protect communities. The developer (Dev_Nand) is not responsible for misuse of the source code.

Unlike standard bots, SentinelX uses **heuristic monitoring** of the Audit Log. If an administrator begins banning members too quickly (e.g., 5 bans in 10 seconds), the bot instantly identifies this as a "Nuke Attempt" and strips their permissions.

* **⚡ Zero-Latency Defense:** Monitors audit logs in real-time.
* **🧠 Smart Thresholds:** Distinguishes between manual moderation and scripted attacks.
* **🔒 Panic Mode:** Automatically locks down the server when a threat is detected.

---

### 🚀 Key Capabilities

| Feature | Description | Status |
| :--- | :--- | :--- |
| **💀 Anti-Nuke (Ban)** | Detects mass bans and instantly bans the attacker. | ✅ Active |
| **👢 Anti-Nuke (Kick)** | Detects mass kicking of members. | ✅ Active |
| **🚫 Auto-Moderation** | Filters malicious links, IP loggers, and spam. | 🚧 Beta |
| **📝 Security Logging** | detailed logs of all mod actions to a secure channel. | ✅ Active |
| **🔐 Whitelist System** | Trusted users can bypass checks (Owner only). | ✅ Active |

---

### ⚙️ Installation & Deployment


SentinelX/
├── cogs/
│   └── antinuke.py      # Core logic for mass-ban detection
├── main.py              # Bot entry point and intent handling
├── requirements.txt     # Python dependencies
└── .env                 # Secrets

#### 1. Clone the Repository
```bash
git clone https://github.com/devnand-47/SentinelX.git
cd SentinelX
python main.py

⚠️ Disclaimer
This tool is for defensive purposes only. It is designed to protect communities. The developer (Dev_Nand) is not responsible for misuse of the source code.

