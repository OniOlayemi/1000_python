import random

first = random.randrange(0, 10)
second = random.randrange(0, 10)
third = random.randrange(0, 10)
forth = random.randrange(0, 10)


comp = str(first) + str(second) + str(third) +str(forth)

print("INSTRUCTION \ninput the guess of four number if you get the number and position right you will get a '*' but if "
      "you get the number right but not the position you'd get a '+'")
print(comp)
users = input("input a guess of four numbers: ")

if len(users) > 4:
    exit("input 4 numbers")

result = ""
for i in range(0, 4):
    if comp[i] == users[i]:
        result += '*'
        continue

    elif users[i] not in users[:i]:
        if users[i] in comp:
            result += "+"

print(result)