import random
chance = 3
x = random.randrange(1,5)
print('Choose a number between 1-5:')
while chance :
    p = input(' ')
    n = int(p)
    if n < x:
        print('\nNumber you chose is less')
        chance -= 1
    elif n > x:
        print('\nNumber you chose is greater')
        chance -= 1
    elif n == x :
        print('\nCorrect Guess!!')
        break
    elif chance == 0 :
        print('Better luck next time!!')
        break
        
    
