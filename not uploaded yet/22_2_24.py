planets = ['Mecury', 'Gold', 'platinum', 'silver', 'bronze', 'brass']

for i, planet in enumerate(planets):
    print(i, planet)

t = 1,2,3,4,5
print(type(t))


numbers = [1203, 1256, 312456, 98]

count = [0] * 10 # same as [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for num in numbers:
    for char in str(num):
        count[int(char)] += 1

for d in range(0, 10):
    print("{} {}".format(d, count[d]))

import dis

#dis.dis(for i, planet in enumerate(planets)
 #   p#, planet))

table2 = [[i * j
          for i in range(1, 11)]#how did they know there would be a square bracket there.
           for j in range(1, 11)
 ]
print(table2)


l1 = ['a', 'b', 'c', 'd']
l2 = ['e', 'f', 'g', 'h']

combo = []

for s in l1:
    for s2 in l2:
        combo.append(s + s2)

print(combo)

combo2 = [s + s2
          for s in l1
          for s2 in l2
]

print(combo2)
from math import factorial
y=0
size = 10
def pscl(x,y):
    return factorial(y)//factorial(x) * factorial(y - x)

pascal = [[pscl(y, x)for x in range(y+1) for x in range(size + 1)]]
print(pascal)
n = int(input("a number"))
#print(n)

is_prime = True
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        is_prime = False
        break

print(is_prime)

