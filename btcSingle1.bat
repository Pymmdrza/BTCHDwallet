@Echo off
title MMDRZA.COM - BTC CHECK ADDR1 PRO/btc.py
Pushd "%~dp0"
:loop
pip install colorama
pip install bs4
pip install BeautifulSoup
python btc.py
goto loop
