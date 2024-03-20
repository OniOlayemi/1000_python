import random

valuer = [None, 0, "", False, [], (), {}, '0', True]

for v in valuer:
    if v:
        print("True value:", v)
    else:
        print("False value: ", v)

vlu = 0
for n in valuer:
    vlu = 10 if vlu > 10 else vlu + 1
    print(vlu)

a = 'you are doing well'
b = "no gree for anybody"

print(a > b)

a = 'you' 'are' "doing" "well"

print(a)

n = 'The big dog jumped over the lazy fox'

print(n.rindex("o"))
print(len(n))
print(n.index('o'))
print(n.find('edd'))
print(n.rfind('o'))
print(n.find('o'))
print(n.__getitem__(8), 'must be integer') #more like a slice .slice or []

if 'wo' in n:
    print("found it")

else:
    print("go fishing")

if 'big' in n:
    print("found it")

sib = 'dog'
if sib in n:
    loc = n.index(sib)
    print(sib, ' is located at index ', loc)

for i in range(32, 126):
    print(i, chr(i), end=" * ")

txt = "Hello world"

for t in txt:
    if t == " ":
        continue
    elif t == "r":
        break
    print(t)

total = 0

while True:
    print(total)
    total += random.randrange(20)

    if total > 1000000:
        break

    elif total % 17 == 1:
        break

    elif total ** 2 % 23 == 7:
        break

print('done')

