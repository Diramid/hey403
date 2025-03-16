#!/bin/bash

# Author: Diramid <diramidteam@gmail.com>
# Version: v1.2.0
# Date: 2025-03-7
# Description: hey403 installation script
# Usage: ./install.sh

GREEN="\e[32m"
YELLOW="\e[33m"
NC="\e[0m"

if [[ $EUID -ne 0 ]]; then
  echo -e "${YELLOW}WARNING: You should run this script as the root user.${NC}"
  read -t 15 -r -p "Do you want to continue as root? (Y/n): " choice
  echo
  choice=${choice:-Y}

  if [[ ${choice} =~ ^[Yy]$ ]]; then
    echo -e "${GREEN}INFO: Running script with root privileges"
    sudo "${0}" "$0"
    exit 0
  else
    exit 1
  fi

fi

SCRIPT_NAME="hey403"
DEST="/usr/local/bin"

echo -e "${GREEN}INFO: Starting the hey403 installation process...${NC}"
echo -e "${GREEN}INFO: Moving files...${NC}"

sudo cp "${SCRIPT_NAME}" "${DEST}"

echo -e "${GREEN}INFO: Installation completed successfully!${NC}"
