import random
done = True
while done :
    x = input("\npress Y to roll or N to exit:")
    if x == 'Y' or x == 'y' :
        n = random.randrange(1,7)
        print('\n')
        print(n)
    elif x == 'N' or x == 'n':
        done = False

    else :
        print('Invalid Input\n')
