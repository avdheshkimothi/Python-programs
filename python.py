import qrcode
i=input("enter the url or text  you want to convert into qr code :")
QR=qrcode.make(i)
QR.save("your qr.png")
print("qr has been successfully created and saved in your current directory as 'your qr.png'")
