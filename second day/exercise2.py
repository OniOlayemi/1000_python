import random

debug = 'off'
move = "inactive"

print("    ------------   ")
print("--- Instructions ---")
print("    ------------   ")
print("1. Guess the computer generated number (BETWEEN 1 - 20); the game ends after a right guess")
print("2. Or press 'x' to exit game, or 's' to reveal hidden value or 'd' for debug mode, or 'm' to move value or"
      " press 'n' to move to the next game")
print("\n\n")

while True:

    comp = random.randrange(1, 21)
    if debug == "on":
        print(comp)

    if move == "active":
        comp += round(random.randrange(-2, 2))

    users = input("input an instruction with a character:  ")

    if users.lower() == "x":
        exit("You wanted to quit")

    elif users.lower() == "s":
        print(comp)

    elif users.lower() == "d":
        if debug == "on":
            debug = 'off'
        else: debug = "on"

    elif users.lower() == "m":
        if move == "active":
            move == "inactive"
        else:
            move = 'active'

    elif users.lower() == 'n':
        continue

    else:
        try:
            d = int(users)
            if d != comp:
                print("try again")
            else:
                print("you won!!!")
                exit("You won")

        except ValueError:
            exit("use predefined number")


#I know I should use function but honestly, I am feeling lazy at the moment and I am still working on loops


