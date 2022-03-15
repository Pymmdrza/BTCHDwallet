## Bitcoin address and Private key search and generator with check balance without apikey 
### first install this package :


`pip install hdwallet`


`pip install bs4`



![Screenshot BTCGenerator](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/m57ksuqqf94s22ki2e0b.png)
----
#### after install package's use this source  :

```
import time

from hdwallet import HDWallet
from hdwallet.symbols import ETH as SYMBOL
import random
from bs4 import BeautifulSoup
import requests

mmdrza = '''
=========================[MMDZA.CoM]==============================
|            _ __ ___  _ __ ___   __| |_ __ ______ _             | 
|           | '_ ` _ \| '_ ` _ \ / _` | '__|_  / _` |            |
|           | | | | | | | | | | | (_| | |   / / (_| |            |
|           |_| |_| |_|_| |_| |_|\__,_|_|  /___\__,_|            |
=========================[MMDZA.CoM]==============================
= Athur : MMDRZA
= Email : x4@Mmdrza.Com
= Web : https://Mmdrza.Com
= Dev.to/mmdrza
= Github.Com/Pymmdrza
=========================[MMDZA.CoM]==============================
|| Donate =    Bitcoin 16p9y6EstGYcnofGNvUJMEGKiAWhAr1uR8       ||
=========================[MMDZA.CoM]==============================
        '''

print(mmdrza)
print('===[Follow My Web Site Mmdrza.Com and Enjoy All Source Python]===')
time.sleep(5)
z = 1
# =========================[MMDZA.CoM]==============================


while True:
    c1 = str(random.choice('0123456789abcdefABCDEF'))
    c2 = str(random.choice('0123456789abcdefABCDEF'))
    c3 = str(random.choice('0123456789abcdefABCDEF'))
    c4 = str(random.choice('0123456789abcdefABCDEF'))
    c5 = str(random.choice('0123456789abcdefABCDEF'))
    c6 = str(random.choice('0123456789abcdefABCDEF'))
    c7 = str(random.choice('0123456789abcdefABCDEF'))
    c8 = str(random.choice('0123456789abcdefABCDEF'))
    c9 = str(random.choice('0123456789abcdefABCDEF'))
    c10 = str(random.choice('0123456789abcdefABCDEF'))
    c11 = str(random.choice('0123456789abcdefABCDEF'))
    c12 = str(random.choice('0123456789abcdefABCDEF'))
    c13 = str(random.choice('0123456789abcdefABCDEF'))
    c14 = str(random.choice('0123456789abcdefABCDEF'))
    c15 = str(random.choice('0123456789abcdefABCDEF'))
    c16 = str(random.choice('0123456789abcdefABCDEF'))
    c17 = str(random.choice('0123456789abcdefABCDEF'))
    c18 = str(random.choice('0123456789abcdefABCDEF'))
    c19 = str(random.choice('0123456789abcdefABCDEF'))
    c20 = str(random.choice('0123456789abcdefABCDEF'))
    c21 = str(random.choice('0123456789abcdefABCDEF'))
    c22 = str(random.choice('0123456789abcdefABCDEF'))
    c23 = str(random.choice('0123456789abcdefABCDEF'))
    c24 = str(random.choice('0123456789abcdefABCDEF'))
    c25 = str(random.choice('0123456789abcdefABCDEF'))
    c26 = str(random.choice('0123456789abcdefABCDEF'))
    c27 = str(random.choice('0123456789abcdefABCDEF'))
    c28 = str(random.choice('0123456789abcdefABCDEF'))
    c29 = str(random.choice('0123456789abcdefABCDEF'))
    c30 = str(random.choice('0123456789abcdefABCDEF'))
    c31 = str(random.choice('0123456789abcdefABCDEF'))
    c32 = str(random.choice('0123456789abcdefABCDEF'))
    c33 = str(random.choice('0123456789abcdefABCDEF'))
    c34 = str(random.choice('0123456789abcdefABCDEF'))
    c35 = str(random.choice('0123456789abcdefABCDEF'))
    c36 = str(random.choice('0123456789abcdefABCDEF'))
    c37 = str(random.choice('0123456789abcdefABCDEF'))
    c38 = str(random.choice('0123456789abcdefABCDEF'))
    c39 = str(random.choice('0123456789abcdefABCDEF'))
    c40 = str(random.choice('0123456789abcdefABCDEF'))
    c41 = str(random.choice('0123456789abcdefABCDEF'))
    c42 = str(random.choice('0123456789abcdefABCDEF'))
    c43 = str(random.choice('0123456789abcdefABCDEF'))
    c44 = str(random.choice('0123456789abcdefABCDEF'))
    c45 = str(random.choice('0123456789abcdefABCDEF'))
    c46 = str(random.choice('0123456789abcdefABCDEF'))
    c47 = str(random.choice('0123456789abcdefABCDEF'))
    c48 = str(random.choice('0123456789abcdefABCDEF'))
    c49 = str(random.choice('0123456789abcdefABCDEF'))
    c50 = str(random.choice('0123456789abcdefABCDEF'))
    c51 = str(random.choice('0123456789abcdefABCDEF'))
    c52 = str(random.choice('0123456789abcdefABCDEF'))
    c53 = str(random.choice('0123456789abcdefABCDEF'))
    c54 = str(random.choice('0123456789abcdefABCDEF'))
    c55 = str(random.choice('0123456789abcdefABCDEF'))
    c56 = str(random.choice('0123456789abcdefABCDEF'))
    c57 = str(random.choice('0123456789abcdefABCDEF'))
    c58 = str(random.choice('0123456789abcdefABCDEF'))
    c59 = str(random.choice('0123456789abcdefABCDEF'))
    c60 = str(random.choice('0123456789abcdefABCDEF'))
    c61 = str(random.choice('0123456789abcdefABCDEF'))
    c62 = str(random.choice('0123456789abcdefABCDEF'))
    c63 = str(random.choice('0123456789abcdefABCDEF'))
    c64 = str(random.choice('0123456789abcdefABCDEF'))
    magic = (
            c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9 + c10 + c11 + c12 + c13 + c14 + c15 + c16 + c17 + c18 + c19 + c20 + c21 + c22 + c23 + c24 + c25 + c26 + c27 + c28 + c29 + c30 + c31 + c32 + c33 + c34 + c35 + c36 + c37 + c38 + c39 + c40 + c41 + c42 + c43 + c44 + c45 + c46 + c47 + c48 + c49 + c50 + c51 + c52 + c53 + c54 + c55 + c56 + c57 + c58 + c59 + c60 + c61 + c62 + c63 + c64)
    PRIVATE_KEY = str(magic)
    # =========================[MMDZA.CoM]==============================
    hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
    hdwallet.from_private_key(private_key=PRIVATE_KEY)
    privatekey = hdwallet.private_key()
    btcaddr1 = hdwallet.p2sh_address()
    # =========================[MMDZA.CoM]==============================
    URL = ('https://bitcoin.atomicwallet.io/address/' + btcaddr1)
    markup = "<h1></h1>"
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537'}
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    small = soup.find("small", {"class": 'text-muted'}).get_text()
    rnd = str(small)[:2]
    # =========================[MMDZA.CoM]==============================
    print(str(z), 'ADD=', str(btcaddr1), str(rnd), '[ MMDRZA.CoM ]')
    z += 1
    # =========================[MMDZA.CoM]==============================
    if int(rnd) > 0:
        print('=======================[ M M D R Z A . C o M ]=======================')
        print('Save information pivatekey and balance on the btcWallet.txt ')
        print('=======================[ M M D R Z A . C o M ]=======================')
        f = open("btcWallet.txt", "a")
        f.write(privatekey + '\n')
        f.write(btcaddr1 + '  BAL= ' + rnd + '\n')
        f.write('=======================[ M M D R Z A . C o M ]=======================')
        f.write('Donate (BTC) = 16p9y6EstGYcnofGNvUJMEGKiAWhAr1uR8')
        f.write('=======================[ M M D R Z A . C o M ]=======================')
        f.close()
        # =========================[MMDZA.CoM]==============================
        continue

# =========================[M M D Z A . C o M]==============================
# Programmer M M D R Z A
# Web Mmdrza.Com
# Dev.to/Mmdrza
# Github.Com/Pymmdrza
# Donat = Bitcoin 16p9y6EstGYcnofGNvUJMEGKiAWhAr1uR8
# =========================[M M D Z A . C o M]==============================


```


#### Visit Another Source : [MMDRZA.COM](https://mmdrza.com)

```
# =========================[M M D Z A . C o M]==============================
# Programmer M M D R Z A
# Web Mmdrza.Com
# Dev.to/Mmdrza
# Github.Com/Pymmdrza
# Donat = Bitcoin 16p9y6EstGYcnofGNvUJMEGKiAWhAr1uR8
# =========================[M M D Z A . C o M]==============================

```
