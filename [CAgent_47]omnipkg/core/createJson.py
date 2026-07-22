import omnimadule
pkg_managers_json = {
    "apt": {
        "update": "sudo apt update && sudo apt full-upgrade -y",
        "install": "sudo apt install -y",
        "clean": "sudo apt autoremove -y && sudo apt clean"
    },
    "dnf": {
        "update": "sudo dnf check-update && sudo dnf upgrade -y",
        "install": "sudo dnf install -y",
        "clean": "sudo dnf autoremove -y && sudo dnf clean all"
    },
    "pacman": {
        "update": "sudo pacman -Syu --noconfirm",
        "install": "sudo pacman -S --noconfirm",
        "clean": "sudo pacman -Rns $(pacman -Qdtq) --noconfirm 2>/dev/null || true && sudo pacman -Scc --noconfirm"
    },
    "yum": {
        "update": "sudo yum check-update && sudo yum update -y",
        "install": "sudo yum install -y",
        "clean": "sudo yum autoremove -y && sudo yum clean all"
    },
    "zypper": {
        "update": "sudo zypper refresh && sudo zypper update -y",
        "install": "sudo zypper install -y",
        "clean": "sudo zypper clean && sudo zypper packages --unneeded | awk 'NR>3 {print $5}' | xargs sudo zypper rm -y 2>/dev/null || true"
    },
    "apk": {
        "update": "sudo apk update && sudo apk upgrade",
        "install": "sudo apk add",
        "clean": "sudo apk cache clean && sudo apk del $(apk info --installed --orphaned) 2>/dev/null || true"
    },
    "xbps-install": {
        "update": "sudo xbps-install -S && sudo xbps-install -Su",
        "install": "sudo xbps-install -y",
        "clean": "sudo xbps-remove -Oo && sudo xbps-remove -y $(xbps-query --list-orphans) 2>/dev/null || true"
    },
    "eopkg": {
        "update": "sudo eopkg update-repo && sudo eopkg upgrade -y",
        "install": "sudo eopkg install -y",
        "clean": "sudo eopkg remove --orphans -y && sudo eopkg clean"
    },
    "emerge": {
        "update": "sudo emerge --sync && sudo emerge -avuDN @world",
        "install": "sudo emerge",
        "clean": "sudo emerge --depclean && sudo emerge --prune"
    },
    "nix": {
        "update": "nix-channel --update && nix-env -u",
        "install": "nix-env -iA nixpkgs.",
        "clean": "nix-collect-garbage -d && nix-store --optimise"
    },
    "guix": {
        "update": "guix pull && guix package -u",
        "install": "guix install",
        "clean": "guix gc && guix package --delete-generations"
    },
    "pkg": {
        "update": "sudo pkg update && sudo pkg upgrade -y",
        "install": "sudo pkg install -y",
        "clean": "sudo pkg autoremove -y && sudo pkg clean -y"
    },
    "brew": {
        "update": "brew update && brew upgrade",
        "install": "brew install",
        "clean": "brew cleanup --prune=all && brew autoremove"
    },
    "flatpak": {
        "update": "flatpak update -y",
        "install": "flatpak install -y",
        "clean": "flatpak uninstall --unused -y && flatpak repair"
    },
    "snap": {
        "update": "sudo snap refresh",
        "install": "sudo snap install",
        "clean": "sudo snap remove --revision $(snap list --all | awk 'NR>1 {print $1}' | xargs -I {} snap changes {} | grep -E 'Remove.*Done' | awk '{print $2}' | head -1) 2>/dev/null || true && sudo snap set system refresh.retain=2"
    },
    "winget": {
        "update": "winget upgrade --all",
        "install": "winget install",
        "clean": "winget uninstall --all --force 2>/dev/null || true && winget settings --enable clean"
    },
    "choco": {
        "update": "choco upgrade all -y",
        "install": "choco install -y",
        "clean": "choco cleanup -y && choco cache remove -y"
    },
    "scoop": {
        "update": "scoop update *",
        "install": "scoop install",
        "clean": "scoop cleanup --cache --all && scoop cache rm --all"
    },
    "pkgin": {
        "update": "sudo pkgin update && sudo pkgin upgrade",
        "install": "sudo pkgin install",
        "clean": "sudo pkgin autoremove && sudo pkgin clean"
    },
    "opkg": {
        "update": "opkg update && opkg upgrade",
        "install": "opkg install",
        "clean": "opkg remove --autoremove && opkg clean"
    },
    "swupd": {
        "update": "sudo swupd update",
        "install": "sudo swupd bundle-add",
        "clean": "sudo swupd clean --all && sudo swupd bundle-remove --orphans"
    },
    "urpmi": {
        "update": "sudo urpmi.update -a && sudo urpmi --auto-update",
        "install": "sudo urpmi",
        "clean": "sudo urpmi --clean && sudo urpme --orphans -a"
    },
    "tdnf": {
        "update": "sudo tdnf check-update && sudo tdnf upgrade -y",
        "install": "sudo tdnf install -y",
        "clean": "sudo tdnf autoremove -y && sudo tdnf clean all"
    }
}

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
pkg_file = 'core/distroPKG.json'
pkg_configuration = "core/packages.json"

omnimadule.createJsonFileIFNotExists(pkg_configuration, pkg_configuration, pkg_List)
omnimadule.createJsonFileIFNotExists(pkg_file, pkg_file, pkg_managers_json)