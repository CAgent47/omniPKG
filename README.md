# OmniPKG(V1.5)

**A universal, distro-agnostic package bootstrapper for Linux.**

OmniPKG is a small tool that automatically detects which package manager your Linux system uses (`apt`, `dnf`, `pacman`, etc.) and installs a list of essential packages for you — automatically, without you needing to know the exact install command for your specific distro.

![Version](https://img.shields.io/badge/version-1.5-blue)
![Shell](https://img.shields.io/badge/shell-bash-green)
![Python](https://img.shields.io/badge/python-3-yellow)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## 🤔 What problem does this solve?

Every Linux distribution has its own package manager and its own syntax for installing software:

```
Ubuntu/Debian:   sudo apt install curl
Fedora:          sudo dnf install curl
Arch:            sudo pacman -S curl
Alpine:          sudo apk add curl
```

If you set up a lot of machines, or you're writing a setup script that needs to work across different distros, you either write a huge if/else chain yourself, or you use OmniPKG, which does that detection and translation for you.

## ✨ Features

- **Automatic package manager detection** — supports `apt`, `dnf`, `pacman`, `yum`, `zypper`, `apk`, `xbps-install`, `eopkg`, `emerge`, `nix`, `guix`, `pkg`, `brew`, `flatpak`, `snap`, `winget`, `choco`, `scoop`, `pkgin`, `opkg`, `swupd`, `urpmi`, and `tdnf`.
- **Self-healing / standalone mode** — if you only have `main.sh` and the `core/` folder is missing, the script offers to clone the rest of the project from GitHub automatically.
- **Zero manual configuration** — generates its own config files on first run if they're missing.
- **Idempotent installs** — skips packages that are already installed, so it's safe to run more than once.
- **Auto-installs `jq`** if it's missing, since the scripts need it to read the JSON config files.
- **Colored, readable output** — clear `[ INFO ]`, `[ SUCCESS ]`, and `[ ERROR ]` messages, plus a `[ + ]` / `[ - ]` line per package.
- **Safe error handling** — uses `set -euo pipefail` and a trap, so the script stops cleanly on the first real error instead of continuing in a broken state.

## 📁 Project Structure

```
pkginstaller/
├── main.sh              # Entry point — this is the file you actually run
└── core/
    ├── createJson.py    # Generates the config JSON files below if they don't exist yet
    ├── detectPKG.py     # Figures out your package manager and prints the packages it should install
    ├── installPKG.py    # Given one package name, prints the correct install command for your system
    ├── updatePKG.py     # Prints the correct "update repositories" command for your system
    ├── distroPKG.json   # A dictionary of install/update commands for every supported package manager
    └── packages.json    # The list of packages you want installed, plus project info
```

## 🧠 How it works

When you run `main.sh`, this happens step by step:

1. **It checks that the `core/` Python files exist.** If any are missing (e.g. you only downloaded `main.sh` by itself), it asks whether you want it to clone the full project from GitHub and pull in the missing `core/` folder automatically.
2. **`createJson.py` runs next.** It checks if `distroPKG.json` and `packages.json` exist. If either is missing, it creates them with default values, so the project works even on a fresh setup.
3. **`updatePKG.py` runs and prints an update command** (e.g. `sudo apt update && sudo apt full-upgrade -y`). `main.sh` captures that output with `eval` and actually runs it, refreshing your package manager's repository list.
4. **`jq` is checked.** If it's not installed, `installPKG.py` is used to install it, since the rest of the script relies on `jq`-style JSON parsing.
5. **`detectPKG.py` runs**, detects your package manager, and prints the list of packages from `packages.json` that should be installed. `main.sh` stores this list in a Bash array.
6. **The script loops over that array.** For each package: if it's already installed, it prints `[ - ]` and skips it. If it's missing, `installPKG.py` prints the correct install command for that one package, and `main.sh` runs it with `eval`.

In short: Python figures out *what* command to run for your specific system, and Bash actually runs it.

## 🚀 Usage

### Option 1 — Full clone (recommended)

```
git clone https://github.com/CAgent47/OmniPKG.git
cd OmniPKG/pkginstaller
chmod +x main.sh
./main.sh
```

### Option 2 — Standalone `main.sh`

If you only have `main.sh` on its own (no `core/` folder next to it), just run it anyway:

```
chmod +x main.sh
./main.sh
```

It will detect that `core/` is missing and ask:

```
[ ERROR ] Missing Python core files: core/createJson.py core/installPKG.py core/updatePKG.py core/detectPKG.py
[ INFO ] Core Python files are missing!

[ INFO ] The following files are required:
  - core/createJson.py
  - core/installPKG.py
  - core/updatePKG.py
  - core/detectPKG.py

[ INFO ] You can download them from: https://github.com/CAgent47/omniPKG.git
Do you want to download them now? (y/n):
```

Answer `y` and it clones the repo, copies `core/` into your current folder, and continues automatically.

You'll need `sudo` access for most package managers, since installing and updating system packages requires root privileges.

## 🖥️ Example Output

A typical run on a fresh Debian/Ubuntu machine looks like this:

```
[ INFO ] Starting OmniPKG Package Installer v1.5
[ INFO ] Author: CAgent_47
==========================================
[ INFO ] Creating package mappings...
[ INFO ] Updating package manager...
[ INFO ] Installing jq...
[ INFO ] Detecting packages to install...
==========================================
[ INFO ] Starting package installation...

[ + ]: Installing python3-full
[ - ]: curl Already installed on your system
[ - ]: git Already installed on your system
[ + ]: Installing ssh
[ + ]: Installing dos2unix
[ + ]: Installing ipython3
[ + ]: Installing libnotify-bin
[ + ]: Installing unrar
[ - ]: wget Already installed on your system
[ + ]: Installing python3-pip
[ + ]: Installing lolcat
[ + ]: Installing fortune
[ + ]: Installing cowsay
[ + ]: Installing btop
==========================================
[ SUCCESS ] Installation completed successfully!

Created By CAgent_47
GitHub: https://github.com/CAgent47
LinkedIn: https://linkedin.com/in/mohammad-shaygan-2a96a8387
X: https://x.com/CAgent_47
```

`[ INFO ]` lines show in yellow, `[ SUCCESS ]` in green, and `[ ERROR ]` in red in your actual terminal — this is just the plain-text version.

## ⚙️ Configuration

### Changing which packages get installed

Edit `core/packages.json` and change the `Packages` array:

```
{
  "Packages": [
    "curl",
    "git",
    "wget"
  ]
}
```

### Adding a new package manager

Edit `core/distroPKG.json`. Each entry needs an `install` and `update` command:

```
{
  "apt": {
    "update": "sudo apt update && sudo apt full-upgrade -y",
    "install": "sudo apt install -y"
  }
}
```

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
- `git` (only needed if using standalone mode to self-clone `core/`)
- `sudo` privileges (for most package managers)

## ❓ FAQ / Troubleshooting

**Why does it ask for my password?**
Installing or updating system packages requires root access, so most commands are run with `sudo`.

**What happens if I say "n" when it asks to download core files?**
The script exits safely without making any changes to your system.

**My package manager isn't in the list, what do I do?**
Open an issue or a PR on GitHub with the correct `install`/`update` syntax for it, and it can be added to `distroPKG.json`.

**Is it safe to run `main.sh` multiple times?**
Yes — it checks whether each package is already installed before trying to install it, so running it again just skips what you already have.

**What does `set -euo pipefail` and the `trap` at the end do?**
They make the script stop immediately and print a clean error message if any command fails, instead of silently continuing with a half-broken setup.

## 🤝 Contributing

Pull requests are welcome! If your package manager isn't listed, feel free to open an issue or PR with its `install`/`update` syntax.

## 📄 License

MIT License

## 👤 Author

**CAgent_47** (Mohammad Shaygan)

- GitHub: [github.com/CAgent47](https://github.com/CAgent47)
- LinkedIn: [linkedin.com/in/mohammad-shaygan-2a96a8387](https://linkedin.com/in/mohammad-shaygan-2a96a8387)
- X: [x.com/CAgent_47](https://x.com/CAgent_47)
