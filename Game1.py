import random

def game(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='s':
            return True
        elif you=='g':
            return False
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True

print("Comp turn: Enter snake(s), water(w) or gun(g)?")
randno=random.randint(1,3)

if randno==1:
    comp='s'
elif randno==2:
    comp='w'
elif randno==3:
    comp='g'

you=input("Your turn: Enter snake(s), water(w) or gun(g)?")
a=game(comp,you)
print(f'Comp chose: {comp}')
print(f'You chose: {you}')

if a==None:
    print("The game is tie!")
elif a==True:
    print("You win.")
elif a==False:
    print("You lose.")
