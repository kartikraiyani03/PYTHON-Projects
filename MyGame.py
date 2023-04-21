import random

def game(comp , you):
    if comp==you:
        return None
    
    elif comp == 'r':
        if you == 'p':
          return True
    elif you == 's':
        return False
    
    elif comp == 'p':
        if you == 'r':
          return False
    elif you == 's':
        return True
    
    elif comp == 's':
        if you == 'r':
          return True
    elif you == 'p':
        return False

num = random.randint(1,3)

if num==1:
    comp='r'
if num==2:
    comp='p'
if num==3:
    comp='s'
    
you = input("Ener Your Choice : Rock(r) Papepr(p) Seissor(s) : \n")
print("Your Choice",you,"")
print("Comp Choice",comp,"\n")

if(game(comp,you)):
     print("You Win\n")
elif(game(comp,you)==None):
    print("Tie\n")
else:
    print("You Loose\n")


