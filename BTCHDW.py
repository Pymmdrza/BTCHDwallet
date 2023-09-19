from colorthon import Colors
from hdwallet import HDWallet
from hdwallet.symbols import BTC, ETH
import random
import requests, os
import time, re, platform

mmdrza = '''

███╗   ███╗███╗   ███╗██████╗ ██████╗ ███████╗ █████╗     ██████╗ ██████╗ ███╗   ███╗
████╗ ████║████╗ ████║██╔══██╗██╔══██╗╚══███╔╝██╔══██╗   ██╔════╝██╔═══██╗████╗ ████║
██╔████╔██║██╔████╔██║██║  ██║██████╔╝  ███╔╝ ███████║   ██║     ██║   ██║██╔████╔██║
██║╚██╔╝██║██║╚██╔╝██║██║  ██║██╔══██╗ ███╔╝  ██╔══██║   ██║     ██║   ██║██║╚██╔╝██║
██║ ╚═╝ ██║██║ ╚═╝ ██║██████╔╝██║  ██║███████╗██║  ██║██╗╚██████╗╚██████╔╝██║ ╚═╝ ██║
╚═╝     ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝
                              -***-                                                          
= author : MMDRZA
= Email : Mmdrza@vk.com
= Web : https://Mmdrza.Com
= Medium : https://mdrza.medium.com
= Github.Com/Pymmdrza
= Donat = Bitcoin 1MMDRZA12xdBLD1P5AfEfvEMErp588vmF9
=========================[M M D Z A . C o M]==============================
        '''


# =========================[Terminal Clear]===============================
def getClear():
    if 'win' in platform.platform() or 'Windows' in platform.platform():
        os.system('cls')
    elif 'linux' in platform.platform() or 'Linux' in platform.platform():
        os.system('clear')
    elif 'darwin' in platform.platform():
        os.system('clear')
    elif 'mac' in platform.platform() or 'Mac' in platform.platform():
        os.system('clear')
    else:
        raise ValueError('Not Supported Platform: "%s"' % platform.platform())

# =========================[Check Balance Ethereum]=======================
def ethBal(addr: str) -> str:
    url = f"https://ethereum.atomicwallet.io/api/v2/address/{addr}"
    req = requests.get(url).json()
    ret = dict(req)['balance']
    return int(ret) / 1000000000000000000
# =========================[Check Balance Bitcoin]========================
def getBal(addr):
    rl = f"https://bitcoin.atomicwallet.io/api/v2/address/{addr}"
    req = requests.get(rl).json()
    ret = dict(req)['balance']
    return int(ret) / 10000000000

# =========================[Colors Terminal]==============================
green = Colors.GREEN
red = Colors.RED
white = Colors.WHITE
yellow = Colors.YELLOW
reset = Colors.RESET
# -------------------------------------------------------------------------
getClear()
# -------------------------------------------------------------------------
print(green, mmdrza, reset)
print('\n\nStart ...')
time.sleep(2)
# -------------------------------------------------------------------------
z = 1
ff = 0
while True:
# -------------------------------------------------------------------------
# Convert Private Key (HEX) to Base  Generated.
    PRIVATE_KEY = "".join(random.choice("0123456789abcdef") for _ in range(64))
    hd_btc: HDWallet = HDWallet(BTC)
    hd_eth: HDWallet = HDWallet(ETH)
    hd_btc.from_private_key(PRIVATE_KEY)
    hd_eth.from_private_key(PRIVATE_KEY)
# -------------------------------------------------------------------------
# Generated Ethereum Address From Private Key (HEX)
    ethaddr = hd_eth.p2pkh_address()
# Generated Bitcoin P2PKH Address From Private Key (HEX)
    btcaddr1 = hd_btc.p2pkh_address()
# Generated Bitcoin P2WPKH Address From Private Key (HEX)
    btcaddr2 = hd_btc.p2wpkh_address()
# Generated Bitcoin P2WPKH in P2SH Address From Private Key (HEX)
    btcaddr3 = hd_btc.p2wpkh_in_p2sh_address()
# Generated Bitcoin P2WSH in P2SH Address From Private Key (HEX)
    btcaddr4 = hd_btc.p2wsh_in_p2sh_address()
# Generated Bitcoin P2SH Address From Private Key (HEX)
    btcaddr5 = hd_btc.p2sh_address()
# -------------------------------------------------------------------------
# Check Balance Value Address From Atomic Wallet
    value5 = getBal(btcaddr5)
    value4 = getBal(btcaddr4)
    value3 = getBal(btcaddr3)
    value2 = getBal(btcaddr2)
    value1 = getBal(btcaddr1)
    val_et = ethBal(ethaddr)
# -------------------------------------------------------------------------
    getClear()
    promptPUB = '''
        *********************** Bitcoin HighSpeed Check Balance WithOut API ********************
        *                                                                                      *
        *    ** This Tools No Need API , Check Without API Balance Bitcoin Address             *
        *    ** Create And Programmer Mmdrza Official Web Site https://mmdrza.com              *
        *    ** ANY ADDRESS IF BALANCE high In 0 Save To This File (btcWin.txt)                *
        *                                                                                      *
        *********************** Enjoy Programming With M M D R Z A . C o M *********************
        ========================================================================================
            '''
    print(yellow, promptPUB, reset)
    print(f"        {red}{'=' * 24}[{reset}{white}Scan{reset}:{yellow} {z}{reset} {white}Found{reset}: {green}{ff}{reset}{red}]{'=' * 24}{reset}")
    print(f"        | BTC Address {red}(P2PKH) {reset} | BAL: {yellow}{value1}{reset} |{white} {btcaddr1}{reset}")
    print(f"        | BTC Address {red}(BECH32){reset} | BAL: {yellow}{value2}{reset} |{white} {btcaddr2}{reset}")
    print(f"        | BTC Address {red}(P2WPKH){reset} | BAL: {yellow}{value3}{reset} |{white} {btcaddr3}{reset}")
    print(f"        | BTC Address {red}(P2WSH) {reset} | BAL: {yellow}{value4}{reset} |{white} {btcaddr4}{reset}")
    print(f"        | BTC Address {red}(P2SH)  {reset} | BAL: {yellow}{value5}{reset} |{white} {btcaddr5}{reset}")
    print(f"        | ETH Address {red}(ETH)   {reset} | BAL: {yellow}{val_et}{reset} |{white} {ethaddr}{reset}")
    print(f"        | Private Key {red}(HEX)   {reset} | {red}{PRIVATE_KEY}{reset}")
    print(f"        {red}{'=' * 70}{reset}")
    z += 1
    # =========================[M M D Z A . C o M]==============================
    if value1 > 0:
        ff += 1
        open('btcWin.txt', 'a').write(f'{btcaddr1}\n{PRIVATE_KEY}\n')
    elif value2 > 0:
        ff += 1
        open('btcWin.txt', 'a').write(f'{btcaddr2}\n{PRIVATE_KEY}\n')
    elif value3 > 0:
        ff += 1
        open('btcWin.txt', 'a').write(f'{btcaddr3}\n{PRIVATE_KEY}\n')
    elif value4 > 0:
        ff += 1
        open('btcWin.txt', 'a').write(f'{btcaddr4}\n{PRIVATE_KEY}\n')
    elif value5 > 0:
        ff += 1
        open('btcWin.txt', 'a').write(f'{btcaddr5}\n{PRIVATE_KEY}\n')
    elif val_et > 0:
        ff += 1
        open('btcWin.txt', 'a').write(f'{ethaddr}\n{PRIVATE_KEY}\n')
    else:
        continue
# =========================[M M D Z A . C o M]==============================
# Programmer M M D R Z A
# Web Mmdrza.Com
# Github.Com/Pymmdrza
# Donat = Bitcoin 1MMDRZA12xdBLD1P5AfEfvEMErp588vmF9
# =========================[M M D Z A . C o M]==============================

