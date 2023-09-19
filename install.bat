@Echo off
title MMDRZA.COM - BTC & ETH HD Address
pip install colorthon
pip install hdwallet
Pushd "%~dp0"
:loop
python BTCHDW.py
goto loop
