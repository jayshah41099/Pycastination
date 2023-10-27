# requirement: pip install qrcode
#terminal command: python3 Qrcode_Generator.py "website_link"

import qrcode
from PIL import Image
import sys

Link = sys.argv[1]

#Generate QR Code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(Link)
qr.make(fit=True)

#Create an image from the QR code
image = qr.make_image(fill="black", back_color="white")

#save the image
Image.save("qr_code.png")
