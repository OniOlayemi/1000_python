print('___convertion___')

a = input("input a number: ")
print(a.isdecimal())
print(a.isnumeric())

if a.isdecimal():
    a = int(a)
    print(type(a))


b = 0.4
c = 0.2

d = b + c

print(d)
d = int(d)
print(d)

print('___Numbers___')
a = 0xA
b = 0b111
c = 0o21
d = 234

print('a is: ', a, 'b is: ',b, 'c is: ',c, 'd is: ',d, 'Total is: ', a+b+c+d)

print("___Random___ \n\n")

import random

a = random.random()
print(random.random())
print(a)

random.seed(4)
print(random.random())
print(random.random())

random.seed(0)
print(random.random())
print(random.random())

random.seed(4)
print(random.random())
print(random.random())

random.seed(0)
print(random.random())
print(random.random())

print('__Random_choice__')

stringing = 'abcdefghijklmnop'

print(random.choice(stringing))
print(random.choice(stringing))
print(random.choice(stringing))

fruits = ['apple', 'pear', 'guava', 'cashew', 'mango', 'pineapple']
print(random.choice(fruits))
print(random.choice(fruits))
print(random.choice(fruits))