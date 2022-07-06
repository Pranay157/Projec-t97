import random
number=random.randint(1,9)
chances=0
while chances < 5:
    guess=int(input("Enter the numbers "))
    if guess== number:
     print("Congratulation YOU WON !!!")
     break
    elif guess<number:
     print("The number is too small" ,guess)
    else :
     print("The number is too Big" ,guess)
    chances+=1
if not chances<5 :
    print("You are the loser") 

