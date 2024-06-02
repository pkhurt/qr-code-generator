import qrcode

link = input("Bitte geben Sie den Link ein, für den der QR-Code erstellt werden soll: ")

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

print("QR-Code wurde erstellt und als 'qrcode.png' gespeichert.")
