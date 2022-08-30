# install all the libraries needed
#? pip install qrcode image
# create a function that collects a text and converts it to a qrcode
# save the qrcode as an image
# run the function

import qrcode

def generate_qrcode(text):
  qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=3
  )

  qr.add_data(text)
  qr.make(fit=True)
  img = qr.make_image(fill_color="black", back_color="white")
  img.save("D:/qrimg.png")

url = input("Enter your URL: ")
generate_qrcode(url)