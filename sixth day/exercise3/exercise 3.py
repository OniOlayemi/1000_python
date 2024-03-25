filename = 'exercise3.txt'

listed = []
listed_dict = {}
with open(filename, 'r') as dd:
    for line in dd:
        word = line.rstrip().split()
        print(word)
        listed.extend(word)

for i in listed:
    if i.lower() in listed_dict:
        listed_dict[i.lower()] += 1
    else:
        listed_dict[i.lower()] = 1

print(listed_dict)
sort_listed = sorted(listed_dict)
for sorts in sort_listed:
    print(sorts, listed_dict[sorts])