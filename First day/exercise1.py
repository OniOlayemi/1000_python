import random

a = random.randrange(1, 20)

try:
    b = int(input("guess a number between 1 to 21: "))
except ValueError:
    exit("input a number")
    #print("input a number")
except NameError:
    exit("input a number")
    #print("input a number")

if b < a:
    print("your guess is smaller")

elif b > a:
    print("Your guess is bigger")

else:
    print("Hit!!! you made the right choice")