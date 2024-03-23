try:
    users = int(input("insert a number and I will tell you if it is prime or not:  "))

except ValueError:
    exit("insert a number")

if users == 2 or users == 5 or users == 7 or users == 3:
    print('True')

elif users % 2 != 0 and users % 3 != 0 and users % 5 != 0 and users % 7 != 0:
    print('True')
else:
    print("False")
