#its a beginner python program for generating a strong password 

#made  using random module loops , list , and string concept.
import random
length=int(input("ENTER THE LENGTH OF PASSWORD :"))
if(length<=0):
	print("invalid input ")
	exit(1)
print("type the serial no. to modify password")
k=int(input(" ENTER YOUR PREFRENCE                                          \n  1.password containing  number and letter(uppercase and lowercase) only   \n 2.password containing numbers letter(upppercase and lowercase) punchuation symbol etc.\n 3. password containing  letter only \n 4.password containing  numbers only :\n"))
if k==1:
   list1=list()
   for i in range(length):
     passchar=chr(random.choice(list(range(65,90))+list(range(97,122))+list(range(48,57)))) #digits and letters
     list1.append(passchar)
   password=''.join(list1)
   print("YOUR PASSWORD IS  : \n ",password)
   
elif k==2:
   list1=list()               #all
   for i in range(length):
     passchar=chr(random.randint(33,126)) 
     list1.append(passchar)
   password=''.join(list1)
   print("YOUR PASSWORD IS  : \n ",password)
   
elif k==3:
   list1=list()
   for i in range(length):
     passchar=chr(random.choice(list(range(65,90))+list(range(97,122)))) #characters only
     list1.append(passchar)
   password=''.join(list1)
   print("YOUR PASSWORD IS  : \n ",password)
elif k==4:
   list1=list()
   for i in range(length):
     passchar=chr(random.randint(48,57)) #numbers
     list1.append(passchar)
   password=''.join(list1)
   print("YOUR PASSWORD IS  : \n ",password)
else :
   print("invalid input")
