#!/bin/bash
# Install Default Packages
sudo apt update && sudo apt full-upgrade -y

# jq Exists?
if ! command -v jq  &> /dev/null; then # if not exists..
    echo "Installing Jq For Read Json..."
    sleep 2
    sudo apt install -y jq
fi


# json file connect and read packages list for install
pack="config.json"
Packages=($(jq -r '.Packages[]' "$pack"))

echo "Installing packages Please Wite......."
# Use json connection and install packages in list
for pkg in "${Packages[@]}"; do
    if ! dpkg -s "$pkg" >/dev/null 2>&1; then
        echo -e "\e[96mInstalling $pkg......\e[0m"
        sleep 2
        sudo apt install -y "$pkg"
    fi
done

# Restart System Request
read -p "The package installation was successful. Do you want to restart? (y/n): " restart
if [[ "$restart" == "y" ]] || [[ "$restart" == "Y" ]]; then 
    echo "5 seconds until restart to cancel (CTRL + C)! "
    for reboot_Sys in {5..1}; do
        echo "$reboot_Sys"
        sleep 1
    done
    # If Error for execution `sudo systemctl reboot` use reboot command
    # reboot
    sudo systemctl reboot
else
    echo "Restart later and let it settle."
    echo "Created By CAgent_47"
fi

# Created By CAgent_47
