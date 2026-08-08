import time
text=input("ENTER TEXT : ")
result=""
print("\n Converting...\n")
for c in text:
    binary=format(ord(c),"08b")
    print(c,"->",binary)
    result+=binary+" "
    time.sleep(0.2)