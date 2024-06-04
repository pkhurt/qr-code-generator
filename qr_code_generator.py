import qrcode

link = input("Please paste the url for which the qr-code shall be generated: ")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(link)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')

img.save("qrcode.png")

print("QR-Code generated and saved as 'qrcode.png'.")
