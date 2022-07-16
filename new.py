import random
while True:
    print( '1.Roll The dice 2.Exit')
    usr=int(input('What do you want to do?'))
    if usr ==1:
        number=random.randint(1,6)
        print (number)
        
    else:
        break