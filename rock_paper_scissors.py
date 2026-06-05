from random import randint
#1=rock 
#2=paper
#3=scissiors
USER_SCORE=0
COMPUTER_SCORE=0
while True:
    user_input=input("enter rock , paper , or scissors :").lower()
    
    if user_input=="rock": 
       user_choice=1
    elif user_input=="paper":
       user_choice=2
    elif user_input=="scissors" :
       user_choice=3
    else:
       print("enter a valid input")
       exit()
#1=rock 
#2=paper
#3=scissiors
    computer_choice=randint(1,3)
    print(computer_choice)
    if computer_choice==1:
        if user_choice==1:
           print("match tied \n user= rock \n computer=rock")
        elif user_choice==2:
           print("you won  \n user= paper \n computer=rock")
           USER_SCORE+=1
        else:
           print("computer won \n user=scissors \n computer=rock")
           COMPUTER_SCORE+=1
    if computer_choice==2:
        if user_choice==1:
           print("computer won \n user=rock \n computer= paper")
           COMPUTER_SCORE+=1
        elif user_choice==2:
           print("match tied  \n user= paper \n computer=paper")
        else:
           print("you  won \n user=scissors \n computer=paper")
           USER_SCORE+=1
    if computer_choice==3:
        if user_choice==1:
           print("you  won \n user= rock \n computer=scissors")
           USER_SCORE+=1
        elif user_choice==2:
           print("computer won \n user= paper \n computer=scissors")
           COMPUTER_SCORE+=1
        else:
           print("match tied \n user=scissiors \n computer=scissors")
    again=int(input("do you want to play one more time press 1 for yes 0 for no   :"))
    if again==0:
    
     print("game ended>>>>")
     print("YOUR SCORE IS :  ",USER_SCORE)
     print("COMPUTER SCORE IS :",COMPUTER_SCORE)
     break
