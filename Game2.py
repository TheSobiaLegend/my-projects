import random

def gamewin(comp,you):
    if comp==you:
        return None
    if comp=='r':
        if you=='p':
            return True
        elif you=='s':
            return False
    elif comp=='p':
        if you=='r':
            return False
        elif you=='s':
            return True
    elif comp=='s':
        if you=='r':
            return True
        elif you=='p':
            return False

print("Comp turn: Chose Rock(r), Paper(p) or Scissor(s)? ")
compchose=random.randint(1,3)
if compchose==1:
    comp='r'
elif compchose==2:
    comp='p'
elif compchose==3:
    comp='s'

you=input("Your turn: Chose Rock(r), Paper(p) or Scissor(s)? ")

print(f'Comp chose {comp}')
print(f'You chose {you}')

g=gamewin(comp,you)
if g==None:
    print("Game Tie!")
elif g==True:
    print("You Win!")
elif g==False:
    print("You Lose!")
