filename = "apache hit.txt"

hhh = open(filename, 'r')

data = hhh.readlines()
iplist = []

count = {}
print(data)

for line in data:
    space = line.index(" ")
    iplist.append(line[0:space])

for i in iplist:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

print(count)