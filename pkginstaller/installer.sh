#!/bin/bash


# Install Default Packages
sudo apt update && sudo apt full-upgrade -y

# jq Exists?
if ! command -v jq  &> /dev/null; then # if not exists..
    echo "Installing Jq For Read Json..."
    sleep 2
    sudo apt install -y jq
fi


# Variables
pack="config.json"
Packages=($(jq -r '.Packages[]' "$pack"))

echo "Installing packages Please Wite......."
# Read Json And Install PKG
for pkg in "${Packages[@]}"; do
    if ! command -v $pkg &> /dev/null; then
        echo -e "\e[96mInstalling $pkg......\e[0m"
        sleep 2
        sudo apt install -y "$pkg"
    fi
done

if ! command fastfetch &> /dev/null; then
    sudo apt install fastfetch -y
fi

# Restart System
read -p "The package installation was successful. Do you want to restart? (y/n): " restart
if [[ "$restart" == "y" ]] || [[ "$restart" == "Y" ]]; then 
    echo "5 seconds until restart to cancel (CTRL + C)! "
    for reboot_Sys in {5..1}; do
        echo "$reboot_Sys"
        sleep 1
    done
    reboot || sudo systemctl reboot
else
    echo "Restart later and let it settle."
    echo "Created By CAgent_47"
fi

# Created By CAgent_47
