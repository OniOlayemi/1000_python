txt = []
value = []

filename = 'test the microphone.txt'

with open(filename, 'r') as f:
    for line in f:
        y, t = line.strip('\n').split(" = ")
        txt.append(y)
        value.append(t)
    print(value, txt )


people = {}

people['foo'] = 123
people['bar'] = 212
people['cue'] = [2, 4, 5]

for f in people:
    print(f, people[f])

for f in people.values():
    print(f)

for t in people.items():
    print(t[0], t[1])

print(people.get('foo'))
print(people.get('nnnn'))
print(people.get('cue'))

print(people.get('answer', 43))

us = [{'foo': 332, 'name': "yemi"}, {'true': "True", 'name':"who"}]

print(list(map(lambda p:p['name'], us)))


people = [{'name': 'foo', 'id': 21223}, {'name': 'bar', 'id': 22132}, {'name': 'esco', 'id': 32212}]

by_name = {}
by_id = {}

for p in people:
    by_name[p['name']] = p
    by_id[p['id']] = p
    print(by_id)
    print(by_name)
sorted_byname = sorted(by_name)
print(sorted_byname)

from collections import OrderedDict
from collections import namedtuple

point = namedtuple('point', 'x,y,z')
f1 = point(2,3,4)
f2 = point(4,3,2)

print(f1 + f2)

d = {}
d[1] = 'new'
d[2] = 'old'
d[3] = 'new-old'
d[4] = 'bk stuff'

print(d)
e = OrderedDict(d)
print(e)
e[5] = 'just bought it'
print(e)
f = sorted(d.keys(), lambda x: d[x])
print(f)