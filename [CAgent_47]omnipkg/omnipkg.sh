#!/bin/bash
set -euo pipefail

clear

installer() {
    local pkg="$1"
    if ! command -v "$pkg" &> /dev/null; then
        echo -e "${BGreen}[ Install ]${RESET} Installing $pkg ..."
        SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
        install_cmd=$(python3 "$SCRIPT_DIR/core/installPKG.py" "$pkg")
        
        if eval "$install_cmd"; then
            echo -e "${BGreen}[ Successfuly ]${RESET} $pkg installed successfully!"
        else
            echo -e "${BRed}[ ERROR ]${RESET} Failed to install $pkg please visit packages.json and find your Package manager for edit packages name"
        fi
    else
        echo -e "${Yellow}[ WARNING ]${RESET} $pkg is already installed in your system."
    fi
}
# Colors
# shellcheck disable=SC2034
RED=$(tput setaf 1)
GREEN=$(tput setaf 2)
YELLOW=$(tput setaf 3)
BLUE=$(tput setaf 4)
CYAN=$(tput setaf 6)
# shellcheck disable=SC2034
BOLD=$(tput bold)
RESET=$(tput sgr0)
# shellcheck disable=SC2034
BPurple='\033[1;35m'
# shellcheck disable=SC2034
BGreen='\033[1;32m'
# shellcheck disable=SC2034
Yellow='\033[0;33m'
BRed='\033[1;31m'
echo "${CYAN}============================================"
echo "  ██████╗ ███╗   ███╗███╗   ██╗██╗██████╗ ██╗  ██╗ ██████╗ "
echo "  ██╔═══██╗████╗ ████║████╗  ██║██║██╔══██╗██║ ██╔╝██╔════╝ "
echo "  ██║   ██║██╔████╔██║██╔██╗ ██║██║██████╔╝█████╔╝ ██║  ███╗"
echo "  ██║   ██║██║╚██╔╝██║██║╚██╗██║██║██╔═══╝ ██╔═██╗ ██║   ██║"
echo "  ╚██████╔╝██║ ╚═╝ ██║██║ ╚████║██║██║     ██║  ██╗╚██████╔╝"
echo "   ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝ "
echo "============================================"
echo "${GREEN}          Universal Package Bootstrapper     ${RESET}"
echo "${YELLOW}                  v1.7                       ${RESET}"
echo "============================================"
echo "  ${BLUE}🐧  Author   :${RESET} CAgent_47"
echo "  ${BLUE}📦  License  :${RESET} MIT                          "
echo "  ${BLUE}🌐  GitHub   :${RESET} github.com/CAgent47"
echo "============================================"
echo ""
echo "  ${GREEN}[ INFO ]${RESET} Starting OmniPKG Package Installer..."
echo "  ${GREEN}[ INFO ]${RESET} Detecting your system and package manager..."
echo "${RESET}"

sleep 4


echo "============================================"
echo "${GREEN}[ INFO ]${RESET} checking json files...."
python3 core/createJson.py

echo "============================================"
echo -e "${BPurple}[ UPDATE ]${RESET} Updating your system....."
# shellcheck disable=SC2046
eval $(python3 core/updatePKG.py)

echo "============================================"
echo -e "${BGreen}[ Install ]${RESET} Checking Jq...."
installer jq
# shellcheck disable=SC2034
# shellcheck disable=SC2091

echo "============================================"
echo -e "${BGreen}[ Install ]${RESET} Detecting Packages"


# shellcheck disable=SC2091
mapfile -t Packages < <(python3 core/detectPKG.py)
echo " "
echo -e "${Yellow}[ WARNING ]${RESET} The following packages are being installed..."

for showPKG in "${Packages[@]}"; do
    echo "$showPKG"
done

echo " "
echo "do you want to install these packages? (y / n)"
# shellcheck disable=SC2162
# shellcheck disable=SC2034

read InstallREQ

if [[ "$InstallREQ" == "y" ]] || [[ "$InstallREQ" == "Y" ]]; then
    echo -e "${BGreen}[ OK ]${RESET} Installing Packages Please Wait a minutes..."
    for package in "${Packages[@]}"; do
        installer "$package"
    done
    # shellcheck disable=SC2046
    eval $(python3 core/cleanPKG.py)
else
    echo "OK Edit your Packages In The packages.json In core folder"
fi
