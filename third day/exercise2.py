"""
Given a list of numbers, numbers = [1203, 1256, 312456, 98],
count how many times each digit appears? The output will look like this:
0 1
1 3
2 3
3 2
4 1
5 2
6 2
7 0
8 1
9 1
"""


list = [1203, 1256, 312456, 98]
comp = ''
relist = []
for i in list:
    c = str(i)
    for d in c:
        comp += d
#print(comp)

comp = sorted(comp) #I had to sort to get the desired output

for i in comp:
    counter = 0
    if i in relist:
        continue
    else:
        relist.append(i)
        for a in range(len(comp)):
            if comp[a] == i:
                counter += 1

    print(i, counter)





