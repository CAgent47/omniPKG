# OmniPKG (V1.5)

**A universal, distro-agnostic package bootstrapper for Linux.**

OmniPKG detects your system's package manager automatically and installs a predefined list of essential packages — no more writing separate install scripts for apt, dnf, pacman, and everything else.



![Version](https://img.shields.io/badge/version-1.5-blue)




![Shell](https://img.shields.io/badge/shell-bash-green)




![Python](https://img.shields.io/badge/python-3-yellow)




![License](https://img.shields.io/badge/license-MIT-lightgrey)



---

## ✨ Features

- **Automatic package manager detection** — supports `apt`, `dnf`, `pacman`, `yum`, `zypper`, `apk`, `xbps-install`, `eopkg`, `emerge`, `nix`, `guix`, `pkg`, `brew`, `flatpak`, `snap`, `winget`, `choco`, `scoop`, `pkgin`, `opkg`, `swupd`, `urpmi`, and `tdnf`.
- **Zero manual configuration** — generates its own config files on first run if they're missing.
- **Idempotent installs** — skips packages that are already installed.
- **Auto-installs `jq`** if it's missing, since it's required for parsing.
- **Simple, readable output** — clear `[ + ]` / `[ - ]` status per package.

## 📁 Project Structure

```
pkginstaller/
├── main.sh              # Entry point — run this
└── core/
    ├── createJson.py    # Generates config JSON files if they don't exist
    ├── detectPKG.py     # Detects the system's package manager and lists its target packages
    ├── installPKG.py    # Builds the install command for a given package
    ├── updatePKG.py     # Builds the update/upgrade command for the detected package manager
    ├── distroPKG.json   # Update & install syntax for every supported package manager
    └── packages.json    # List of packages to install + project metadata
```

## 🚀 Usage

Clone the repo and run the script:

```
git clone https://github.com/CAgent47/OmniPKG.git
cd OmniPKG/pkginstaller
chmod +x main.sh
./main.sh
```

That's it. OmniPKG will:

1. Generate the required JSON config files if they're missing.
2. Update your package manager's repositories.
3. Install `jq` if it isn't already present.
4. Loop through the package list in `packages.json` and install anything missing.

## ⚙️ Configuration

Want to customize which packages get installed? Just edit `core/packages.json`:

```
{
  "Packages": [
    "curl",
    "git",
    "wget"
  ]
}
```

Need to add support for a package manager, or tweak its install/update syntax? Edit `core/distroPKG.json` — each entry just needs an `install` and `update` command.

## 🗺️ Supported Package Managers

| Manager | Distro / Platform |
|---|---|
| `apt` | Debian, Ubuntu, Mint |
| `dnf` | Fedora, RHEL 8+ |
| `yum` | CentOS, older RHEL |
| `pacman` | Arch, Manjaro, EndeavourOS |
| `zypper` | openSUSE |
| `apk` | Alpine |
| `xbps-install` | Void Linux |
| `eopkg` | Solus |
| `emerge` | Gentoo |
| `urpmi` | Mageia |
| `swupd` | Clear Linux |
| `tdnf` | Photon OS |
| `nix` / `guix` | NixOS / Guix System |
| `pkg` / `pkgin` | FreeBSD, NetBSD |
| `opkg` | Embedded / OpenWrt |
| `flatpak` / `snap` | Cross-distro sandboxed apps |
| `brew` | Linuxbrew / macOS |
| `winget` / `choco` / `scoop` | Windows |

## 🧩 Requirements

- Bash
- Python 3
- `sudo` privileges (for most package managers)

## 🤝 Contributing

Pull requests are welcome! If your package manager isn't listed, feel free to open an issue or PR with its `install`/`update` syntax.

## 📄 License

MIT License

## 👤 Author

**CAgent_47** (Mohammad Shaygan)

- GitHub: [github.com/CAgent47](https://github.com/CAgent47)
- LinkedIn: [linkedin.com/in/mohammad-shaygan-2a96a8387](https://linkedin.com/in/mohammad-shaygan-2a96a8387)
- X: [x.com/CAgent_47](https://x.com/CAgent_47)