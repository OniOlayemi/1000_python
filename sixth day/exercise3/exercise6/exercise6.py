import copy

filename = 'exercise6.txt'
file_list = []
file_dict = {}
column = []
dd = open(filename, 'r')
data = dd.read()
data = data.replace('\n', ",!,").split(',')

print(data)

for d in range(len(data)):
    if d < 3:
        column.append(data[d])
    else:
        if data[d] == '!':
            counter = 0
            if file_dict == {}:
                continue
            else:
                file_list.append(other_dict)
                #counter = 0
            continue
        else:
            file_dict[column[counter]] = data[d]
            counter += 1
            if counter % 3 == 0:
                other_dict = copy.deepcopy(file_dict)




print(file_list)
answer = {}
for data in file_list:
    answer[data["fname"],data["lname"]] = data
print(answer[('Eric', 'Idle')]['born']) # 29 March 1943
print(answer)
