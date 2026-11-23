#install pip segno package 
import segno

qrcode = segno.make_qr("www.x.com")
qrcode.save("basic_rqcode.png", scale = 3, dark = "darkblue")
