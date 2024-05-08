@echo off
REM Install the necessary packages
pip install hdwallet
pip install colorthon
pip install requests
pip install requests-random-user-agent


:loop_start
python singleWallet.py
echo Restarting script...
timeout /t 5 /nobreak
goto loop_start
