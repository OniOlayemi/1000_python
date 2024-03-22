list = [ 'grape banana mango', 'nut peach orange', 'apple nut banana apple mango']
new_list = []
sort_list = []

for i in list:
    voom = i.split(" ")
    for v in voom:
        if v not in new_list:
            new_list.append(v)
print(new_list)


