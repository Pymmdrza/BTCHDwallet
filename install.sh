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

pip3 install requests-random-user-agent
command_success "[ERROR] Failed to install requests-random-user-agent"



while true; do
    python3 singleWallet.py
    echo "Restarting script..."
    sleep 3
done
