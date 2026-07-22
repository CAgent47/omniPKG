<div align="center">

# 🐧 OmniPKG (V1.7) — Universal Package Bootstrapper

**One script. Any Debian-based distro. Zero manual package hunting.**

![Version](https://img.shields.io/badge/version-v1.7-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Shell](https://img.shields.io/badge/shell-bash-1f425f)
![Python](https://img.shields.io/badge/python-3-yellow)
![Platform](https://img.shields.io/badge/platform-Linux-orange)

</div>

---

## 📖 About

**OmniPKG** is a smart, interactive package bootstrapper for Debian-based Linux distributions. Instead of manually installing dependencies one by one, OmniPKG detects your system, checks a simple JSON config for the packages you need, and installs everything for you — with colorful, readable output at every step.

Built for people who are tired of typing `sudo apt install` fifteen times in a row.

---

## ✨ Features

- 🔍 **Auto-detection** of installed vs missing packages before touching anything
- 📦 **JSON-driven configuration** — edit `core/packages.json` to control exactly what gets installed
- 🎨 **Colorful, human-friendly terminal output** (success / warning / error states clearly marked)
- ✅ **Interactive confirmation** before any install runs — nothing happens silently
- 🧹 **Automatic cleanup** after installation (cache/temp files removed via `cleanPKG.py`)
- 🔄 **Self-updating system check** — runs a full system update before installing anything
- 🛡️ **Safe by design** — uses `set -euo pipefail`, checks before installing, never force-installs blindly

---

## ⚙️ How It Works

```
┌──────────────────────┐
│   omnipkg.sh start   │
└──────────┬───────────┘
           │
           ▼
   core/createJson.py      → ensures packages.json exists
           │
           ▼
   core/updatePKG.py       → runs system update (apt update && full-upgrade)
           │
           ▼
   installer() → jq        → ensures jq is available (auto-installed if missing)
           │
           ▼
   core/detectPKG.py       → reads packages.json, returns the package list
           │
           ▼
   [ Confirmation prompt ] → y/n before continuing
           │
           ▼
   installer() per package → installs each missing package individually
           │
           ▼
   core/cleanPKG.py        → cleans up after installation
```

---

## 🚀 Installation & Usage

```bash
git clone https://github.com/CAgent47/OmniPKG.git
cd OmniPKG
chmod +x omnipkg.sh
./omnipkg.sh
```

That's it. The script will:
1. Show the banner and detect your system
2. Make sure `packages.json` exists (creates a default one if it's missing)
3. Update your system
4. Show you exactly which packages it's about to install
5. Ask for confirmation (`y`/`n`)
6. Install everything, then clean up

---

## 📂 Project Structure

```
OmniPKG/
├── omnipkg.sh              # main entry point
├── core/
│   ├── packages.json       # your customizable package list
│   ├── createJson.py       # creates packages.json if missing
│   ├── updatePKG.py        # generates the system-update command
│   ├── installPKG.py       # generates the correct install command per distro
│   ├── detectPKG.py        # reads and returns the package list
│   └── cleanPKG.py         # generates the post-install cleanup command
└── README.md
```

---

## 🛠️ Requirements

| Requirement | Notes |
|---|---|
| Bash | any modern version |
| Python 3 | used by the `core/` scripts |
| `jq` | auto-installed by the script if missing |
| A Debian-based distro | Debian, Ubuntu, Pop!_OS, and derivatives |

---

## 📝 Customizing Packages

Open `core/packages.json` and edit the package list to whatever you need:

```json
{
    "Packages": [
        "curl",
        "git",
        "btop"
    ]
}
```

Save it, run `./omnipkg.sh` again — done.

---

## 🤝 Contributing

Issues and pull requests are welcome. If a package fails to install on your distro, check `core/packages.json` and make sure the package name matches your distro's package manager naming convention.

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for details.

---

<div align="center">

**Author:** CAgent_47
![GitHub](https://github.com/CAgent47) · ![LinkedIn](https://www.linkedin.com/in/mohammad-shaygan-2a96a8387) · ![X](https://x.com/CAgent_47)

</div>