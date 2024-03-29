
dna = 'ACCGXXCXXGTTACTGGGCXTTGT'
sequences = dna.split('X')
sequences.sort(key=len, reverse=True)

print(sequences)
sequences = list( filter(lambda x: len(x) > 0, sequences) )
print(sequences)


winning = 'IneedtodowhatIgotta'
winning_list = []
winning_list.extend(winning)
print(winning_list)
winning_l = sorted(winning)
print(winning_l)
winning_li = [x for x in winning]
print(winning_li)

filename = 'exercise4.txt'

with open(filename, 'r') as fh:
    for line in fh:
        print(line)

fh = open(filename, 'r')
print(fh)
data = fh.read()
print(data)
fh.close()
print(fh)

import sys

def process(filename):
    with open(filename, 'r') as fh:
        for line in fh:
            line = line.rstrip('\n')
            if len(line) > 0:
                if line[0] == '#':
                    return

            if len(line) > 1:
                if line[0:2] == '//':
                    return

            print(line)

#process(sys.argv[0])

listed = [1,2,3,4,5,6,7,8,9]
print(list(enumerate(listed)))
new = 23

with open(filename, 'r') as th:
    for line in th:
        line = line.rstrip('\n')
        print(line)

with open(filename, 'r') as fh:
    line_str = fh.read()
print('---')
print(line_str, end= '-_-')


with open(filename, 'w') as fh:
    line = "it's gonna be alright."
    fh.write(line)

with open(filename, 'r') as fh:
    print(" ")
    print(fh.read())

filename = 'colors.txt'

with open(filename, 'r') as cl:
    users = input('pick a color with a number between (1 to 8) or color name: ')
    for lines in cl:
        if lines[0] == users:
            print(lines)
        if users.lower() == lines[2:].lower():
            print(lines)
