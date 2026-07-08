#!/bin/bash
set -eou pipefail
command -v apt >/dev/null || {
    echo "apt not found"
    exit 1
}
conf=${1:-config.json}

if ! command -v jq &> /dev/null; then
    sudo apt install -y jq
fi
if jq -e '.update' "$conf" > /dev/null; then
    sudo apt update
    sudo apt full-upgrade -y
fi

applyPKG() {
    local pkg="$1"
    if dpkg -s "$pkg" &> /dev/null; then
        echo "[ - ] '$pkg' Installed in your System"
    else
        echo "[ + ] Installing '$pkg' ..."
        if ! sudo apt install -y "$pkg"; then
            echo "[ERROR]: failed to install $pkg"
            exit 1
        fi
    fi
}

if [[ ! -f "$conf" ]]; then

    if [[ ! -f "create.py" ]]; then
        echo "[ Python Error ]: Conf Create File Not Exists Please Goto https://github.com/CAgent47/GraphicCardDriver-installer-for-Debian13 and Download '*.py' file Please"
        exit 1
    fi
    
    echo "[FiX]: File $conf Not Found Creating File." >&2
    if ! command -v python3 &> /dev/null; then
        sudo apt install -y python3-full
    fi
    python3 create.py
fi

mapfile -t packages < <(jq -r '.Packages[]' "$conf")

for basic in "${packages[@]}"; do
    applyPKG "$basic"
done
# Created By CAgent_47
