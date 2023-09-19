@Echo off
title MMDRZA.COM - BTC & ETH HD Address
Pushd "%~dp0"
:loop
pip install colorthon
pip install hdwallet
python singleWallet.py
goto loop
