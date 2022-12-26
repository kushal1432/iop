import pyqrcode
from pyqrcode import QRCode

# String which represent the QR code

s = "https://docs.google.com/document/d/1FKivgfQ0ED62TsDDoOACf138g_F1ztk21Osxs1MCdnM/edit"

# Generate QR code
url = pyqrcode.create(s)


# Create and save the png file naming "myqr.png"

url.svg("myyoutube.svg", scale=8)