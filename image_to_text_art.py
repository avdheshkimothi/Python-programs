from PIL import Image
img=Image.open(input("image:")).convert("L")
w=100
h=int(img.height/img.width *w*0.45)
img=img.resize((w,h))
chars="@#*+=-:. "
for y in range(h):
    for x in range(w):
        p=img.getpixel((x,y))
        print(chars[p* len(chars)//256],end="")
    print()