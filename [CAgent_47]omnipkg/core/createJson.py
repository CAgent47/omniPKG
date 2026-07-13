import os
import json

pkg_List = {
    "Author INFO":{
        "project": "Linux Package installer",
        "author": "CAgent_47",
        "GitHub": "github.com/CAgent47",
        "LinkedIn": "linkedin.com/in/mohammad-shaygan-2a96a8387",
        "X": "x.com/CAgent_47"
    },
    "apt": [
            "python3-full",
            "curl",
            "git",
            "openssh-client",
            "dos2unix",
            "ipython3",
            "libnotify-bin",
            "unrar",
            "wget",
            "python3-pip",
            "lolcat",
            "fortune",
            "cowsay",
            "btop"
        ],
    "dnf": [
            "python3",
            "curl",
            "git",
            "openssh-clients",
            "dos2unix",
            "ipython",
            "libnotify",
            "unrar",
            "wget",
            "python3-pip",
            "lolcat",
            "fortune",
            "cowsay",
            "btop"
        ],
    "pacman": [
            "python",
            "curl",
            "git",
            "openssh",
            "dos2unix",
            "ipython",
            "libnotify",
            "unrar",
            "wget",
            "python-pip",
            "lolcat",
            "fortune",
            "cowsay",
            "btop"
        ],
    "yum": [
            "python3",
            "curl",
            "git",
            "openssh-clients",
            "dos2unix",
            "ipython",
            "libnotify",
            "unrar",
            "wget",
            "python3-pip",
            "lolcat",
            "fortune",
            "cowsay",
            "btop"
        ],
    "zypper": [
            "python3-full",
            "curl",
            "git",
            "openssh",
            "dos2unix",
            "ipython",
            "libnotify",
            "unrar",
            "wget",
            "python3-pip",
            "lolcat",
            "fortune",
            "cowsay",
            "btop"
        ],
    "apk": [
            "python3",
            "curl",
            "git",
            "openssh-client",
            "dos2unix",
            "ipython",
            "libnotify",
            "unrar",
            "wget",
            "py3-pip",
            "lolcat",
            "fortune",
            "cowsay",
            "btop"
        ],
    "xbps-install": [
            "python3",
            "curl",
            "git",
            "openssh",
            "dos2unix",
            "ipython",
            "libnotify",
            "unrar",
            "wget",
            "python3-pip",
            "lolcat",
            "fortune",
            "cowsay",
            "btop"
        ],
    "eopkg": [
            "python3",
            "curl",
            "git",
            "openssh",
            "dos2unix",
            "ipython",
            "libnotify",
            "unrar",
            "wget",
            "python3-pip",
            "lolcat",
            "fortune",
            "cowsay",
            "btop"
        ],
    "emerge": [
            "dev-lang/python",
            "net-misc/curl",
            "dev-vcs/git",
            "net-misc/openssh",
            "app-text/dos2unix",
            "dev-python/ipython",
            "dev-libs/libnotify",
            "app-arch/unrar",
            "net-misc/wget",
            "dev-python/pip",
            "games-misc/lolcat",
            "games-misc/fortune",
            "games-misc/cowsay",
            "sys-process/btop"
        ],
    "nix": [
            "python3",
            "curl",
            "git",
            "openssh",
            "dos2unix",
            "ipython",
            "libnotify",
            "unrar",
            "wget",
            "python3-pip",
            "lolcat",
            "fortune",
            "cowsay",
            "btop"
        ],
    "guix": [
            "python",
            "curl",
            "git",
            "openssh",
            "dos2unix",
            "ipython",
            "libnotify",
            "unrar",
            "wget",
            "python-pip",
            "lolcat",
            "fortune",
            "cowsay",
            "btop"
        ],
    "pkg": [
            "python3",
            "curl",
            "git",
            "openssh",
            "dos2unix",
            "ipython",
            "libnotify",
            "unrar",
            "wget",
            "py3-pip",
            "lolcat",
            "fortune",
            "cowsay",
            "btop"
        ],
    "brew": [
            "python",
            "curl",
            "git",
            "openssh",
            "dos2unix",
            "ipython",
            "libnotify",
            "unrar",
            "wget",
            "pip",
            "lolcat",
            "fortune",
            "cowsay",
            "btop"
        ],
    "flatpak": [
            "org.python.Python",
            "org.curl.Curl",
            "org.git.Git",
            "org.openssh.OpenSSH",
            "org.dos2unix.Dos2unix",
            "org.ipython.IPython",
            "org.libnotify.Libnotify",
            "org.unrar.Unrar",
            "org.wget.Wget",
            "org.python.pip",
            "org.lolcat.Lolcat",
            "org.fortune.Fortune",
            "org.cowsay.Cowsay",
            "org.btop.Btop"
        ],
    "snap": [
            "python3",
            "curl",
            "git",
            "openssh",
            "dos2unix",
            "ipython",
            "libnotify",
            "unrar",
            "wget",
            "pip",
            "lolcat",
            "fortune",
            "cowsay",
            "btop"
        ],
    "winget": [
            "Python.Python",
            "curl.curl",
            "Git.Git",
            "OpenSSH.OpenSSH",
            "dos2unix.dos2unix",
            "ipython.ipython",
            "libnotify.libnotify",
            "unrar.unrar",
            "wget.wget",
            "pip.pip",
            "lolcat.lolcat",
            "fortune.fortune",
            "cowsay.cowsay",
            "btop.btop"
        ],
    "choco": [
            "python",
            "curl",
            "git",
            "openssh",
            "dos2unix",
            "ipython",
            "libnotify",
            "unrar",
            "wget",
            "pip",
            "lolcat",
            "fortune",
            "cowsay",
            "btop"
        ],
    "scoop": [
            "python",
            "curl",
            "git",
            "openssh",
            "dos2unix",
            "ipython",
            "libnotify",
            "unrar",
            "wget",
            "pip",
            "lolcat",
            "fortune",
            "cowsay",
            "btop"
        ]
}

pkg_configuration = "core/packages.json"
def createJsonFile(file, list):
    with open(file, "w") as savePackages:
        json.dump(list, savePackages, indent=4)
    print(" ")
    print("[ Python Message ]: The json file did not exist and was created. Edit the config.json file to edit the installable packages.")
    print(" ")

if not os.path.exists(pkg_configuration):
    createJsonFile(pkg_configuration, pkg_List)
else:
    print("[ Python Message ]: Success")


pkg_managers_json = {
    "apt": {
        "update": "sudo apt update && sudo apt full-upgrade -y",
        "install": "sudo apt install -y"
    },
    "dnf":{
        "update": "sudo dnf check-update && sudo dnf upgrade -y",
        "install": "sudo dnf install -y"
    },
    "pacman": {
        "update": "sudo pacman -Syu --noconfirm",
        "install": "sudo pacman -S --noconfirm"
    },
    "yum":{
        "update": "sudo yum check-update && sudo yum update -y",
        "install": "sudo yum install -y"
    },
    "zypper": {
        "update": "sudo zypper refresh && sudo zypper update -y",
        "install": "sudo zypper install -y"
    },
    "apk": {
        "update": "sudo apk update && sudo apk upgrade",
        "install": "sudo apk add"
    },
    "xbps-install":{
        "update": "sudo xbps-install -S && sudo xbps-install -Su",
        "install": "sudo xbps-install -y"
    },
    "eopkg": {
        "update": "sudo eopkg update-repo && sudo eopkg upgrade -y",
        "install": "sudo eopkg install -y"
    },
    "emerge": {
        "update": "sudo emerge --sync && sudo emerge -avuDN @world",
        "install": "sudo emerge"
    },
    "nix": {
        "update": "nix-channel --update && nix-env -u",
        "install": "nix-env -iA nixpkgs."
    },
    "guix": {
        "update": "guix pull && guix package -u",
        "install": "guix install"
    },
    "pkg": {
        "update": "sudo pkg update && sudo pkg upgrade -y",
        "install": "sudo pkg install -y"
    },
    "brew": {
        "update": "brew update && brew upgrade",
        "install": "brew install"
    },
    "flatpak": {
        "update": "flatpak update -y",
        "install": "flatpak install -y"
    },
    "snap": {
        "update": "sudo snap refresh",
        "install": "sudo snap install"
    },
    "winget": {
        "update": "winget upgrade --all",
        "install": "winget install"
    },
    "choco": {
        "update": "choco upgrade all -y",
        "install": "choco install -y"
    },
    "scoop": {
        "update": "scoop update *",
        "install": "scoop install"
    },
    "pkgin": {
        "update": "sudo pkgin update && sudo pkgin upgrade",
        "install": "sudo pkgin install"
    },
    "opkg": {
        "update": "opkg update && opkg upgrade",
        "install": "opkg install"
    },
    "swupd": {
        "update": "sudo swupd update",
        "install": "sudo swupd bundle-add"
    },
    "urpmi": {
        "update": "sudo urpmi.update -a && sudo urpmi --auto-update",
        "install": "sudo urpmi"
    },
        "tdnf": {
        "update": "sudo tdnf check-update && sudo tdnf upgrade -y",
        "install": "sudo tdnf install -y"
    }
}

pkg_file = 'core/distroPKG.json'
def createPKGJsonFile(file, list):
    with open(file, "w") as PKGM:
        json.dump(list, PKGM, indent=4)
    print(" ")
    print("[ Python Message ]: The distroPKG.json file did not exist and was created.")
    print(" ")

if not os.path.exists(pkg_file):
    createPKGJsonFile(pkg_file, pkg_managers_json)
else:
    print("[ Python Message ]: Success")