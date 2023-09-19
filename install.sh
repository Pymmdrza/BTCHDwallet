#!/bin/bash

command_success() {
  if [[ $? -ne 0 ]]; then
    echo "Error: $1"
    exit 1
  fi
}

pip3 install hdwallet
command_success "[ERROR] Failed to install hdwallet"

pip3 install colorthon
command_success "[ERROR] Failed to install colorthon"

pip3 install requests
command_success "[ERROR] Failed to install requests"

while true; do
    python3 BTCHDW.py
    echo "Restarting script..."
    sleep 3
done
