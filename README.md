# qr-code-generator
The python3 module makes qr generation as easy as possible.

## How to generate the QR Code
1. `pip3 install -r requirements.txt`
2. `python3 qr_code_generator.py`

The script will prompt the link request question. The user has then to paste the link into the terminal.

The picture will be generated as `qrcode.png` and saved in the same directory as the script.

## How does a QR Code work
Each QR Code consists of the following zones:
1. Quiet zone
2. Finder pattern
3. Alignment pattern
4. Timing pattern
5. Version of information
6. Data cells