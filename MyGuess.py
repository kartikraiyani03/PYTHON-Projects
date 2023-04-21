import random

num = random.randint(1,100)
you = None

while(num != you):
    you = int(input("Enter the Number : "))
    if(num == you):
         print("You Win")
         
    elif(num >= you):
        print("Highe Number Please...\n")  
        
    else:
        print("Lower Number Please...\n")
        



