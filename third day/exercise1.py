colors = ['blue','green','yellow','white']
users = input("insert a number to show a color: 1 = blue, 2 = green, 3 = yellow, 4 = white:  ")
try:
    users = int(users)
    print(colors[users])

except ValueError:
    if users.lower() == 'blue' or users.lower() == 'green' or users.lower() == 'yellow' or users.lower() == 'white':
        print(users.lower())
    else:
        exit('insert a number or code')

