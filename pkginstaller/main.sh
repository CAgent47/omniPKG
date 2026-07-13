#!/bin/bash
set -euo pipefail

# Colors for better output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Function to print colored messages
print_error() {
    echo -e "${RED}[ ERROR ]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[ SUCCESS ]${NC} $1"
}

print_info() {
    echo -e "${YELLOW}[ INFO ]${NC} $1"
}

# Function to check if Python files exist
check_python_files() {
    local missing_files=()
    
    for file in "core/createJson.py" "core/installPKG.py" "core/updatePKG.py" "core/detectPKG.py"; do
        if [[ ! -f "$file" ]]; then
            missing_files+=("$file")
        fi
    done
    
    if [[ ${#missing_files[@]} -gt 0 ]]; then
        print_error "Missing Python core files: ${missing_files[*]}"
        return 1
    fi
    
    return 0
}

# Function to clone the repository
clone_repository() {
    print_info "Cloning omniPKG repository..."
    
    # Check if git is installed
    if ! command -v git &> /dev/null; then
        print_error "Git is not installed. Please install git first."
        exit 1
    fi
    
    # Backup existing files if any
    if [[ -d "core" ]]; then
        print_info "Backing up existing core directory..."
        mv core core_backup_$(date +%s)
    fi
    
    # Clone the repository
    if git clone https://github.com/CAgent47/omniPKG.git temp_repo; then
        # Copy core files from cloned repo
        if [[ -d "temp_repo/core" ]]; then
            cp -r temp_repo/core .
            cp -r temp_repo/packages.json . 2>/dev/null || true
            cp -r temp_repo/distroPKG.json . 2>/dev/null || true
            print_success "Core files downloaded successfully!"
            rm -rf temp_repo
            return 0
        else
            print_error "Failed to find core directory in cloned repository"
            rm -rf temp_repo
            return 1
        fi
    else
        print_error "Failed to clone repository. Please check your internet connection."
        return 1
    fi
}

# Main execution
main() {
    print_info "Starting OmniPKG Package Installer v1.5"
    print_info "Author: CAgent_47"
    echo "=========================================="
    
    # Check for Python core files
    if ! check_python_files; then
        print_info "Core Python files are missing!"
        echo ""
        print_info "The following files are required:"
        echo "  - core/createJson.py"
        echo "  - core/installPKG.py"
        echo "  - core/updatePKG.py"
        echo "  - core/detectPKG.py"
        echo ""
        print_info "You can download them from: https://github.com/CAgent47/omniPKG.git"
        
        read -p "Do you want to download them now? (y/n): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            if clone_repository; then
                print_success "Core files downloaded. Continuing..."
            else
                print_error "Failed to download core files. Exiting."
                exit 1
            fi
        else
            print_error "Cannot continue without core files. Exiting."
            exit 1
        fi
    fi
    
    # Check if Python is installed
    if ! command -v python3 &> /dev/null; then
        print_error "Python 3 is not installed. Please install Python 3 first."
        exit 1
    fi
    
    # Execute the main installation process
    print_info "Creating package mappings..."
    python3 core/createJson.py
    
    print_info "Updating package manager..."
    eval $(python3 core/updatePKG.py)
    
    # Check and install jq if needed
    if ! command -v jq &> /dev/null; then 
        print_info "Installing jq..."
        eval $(python3 core/installPKG.py) jq
    fi
    
    print_info "Detecting packages to install..."
    Packages=($(python3 core/detectPKG.py))
    
    # Install packages
    echo "=========================================="
    print_info "Starting package installation..."
    echo ""
    
    for PKG in "${Packages[@]}"; do
        if ! command -v "$PKG" &> /dev/null; then
            echo "[ + ]: Installing $PKG" 
            eval python3 core/installPKG.py "$PKG"
        else
            echo "[ - ]: $PKG Already installed on your system"
        fi
    done
    
    echo "=========================================="
    print_success "Installation completed successfully!"
    echo ""
    echo "Created By CAgent_47"
    echo "GitHub: https://github.com/CAgent47"
    echo "LinkedIn: https://linkedin.com/in/mohammad-shaygan-2a96a8387"
    echo "X: https://x.com/CAgent_47"
}

# Trap errors
trap 'print_error "An error occurred. Exiting..." && exit 1' ERR

# Run main function
main

exit 0
