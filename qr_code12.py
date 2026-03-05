import qrcode
from PIL import Image
from qrcode.main import QRCode

qr=qrcode.QRCode(version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10, border=4,)
qr.add_data("https://www.youtube.com/watch?v=i8_QWXpwWgU&list=RDGMEMQ1dJ7wXfLlqCjwV0xfSNbAVMi8_QWXpwWgU&start_radio=1")
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="blue")
img.save("margaux_web.png")