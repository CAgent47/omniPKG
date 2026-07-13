#!/bin/bash
set -euo pipefail
python3 core/createJson.py

eval $(python3 core/updatePKG.py)

if ! command -v jq &> /dev/null; then 
    eval $(python3 core/installPKG.py) jq
fi

Packages=($(python3 core/detectPKG.py))

for PKG in "${Packages[@]}"; do
    if ! command -v "$PKG" &> /dev/null; then
        echo "[ + ]: Installing $PKG" 
        eval python3 core/installPKG.py "$PKG"
    else
        echo "[ - ]: $PKG Installed On your System"
    fi
done

# Created By CAgent_47