import qrcode

#criar um codigo QR
qr = qrcode.QRCode(version=1, box_size=10, border=5)

#adicionar dados ao codigo QR
data = 'https://1drv.ms/f/s!AsEryP8vmImRkpNnJN-iZ0NscP1lLA?e=eZynSq'
qr.add_data(data)
qr.make(fit=True)

#criar imagem do codigo QR
img = qr.make_image(fill_color='Pink', back_color='pink')

# salvar imagem em um arquivo
img.save('qr_code.png')