qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=8,border=10)
qr.make("https://www.youtube.com/watch?v=N-iO1tDmP1A&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl&index=6")
img=qr.make_image(fill_color="blue",back_color="white")
img.save("Youtube")