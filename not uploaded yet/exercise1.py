text = '''
This is a very long text.
OK, maybe it's not that long after all
'''

rt = {}

for i in text.lower():
    if i == " " or i == "\n":
        continue
    elif i in rt:
        rt[i] += 1
    else:
        rt[i] = 1

for i in rt.keys():
    print(i, rt[i])

print("exercise 2")

words = ['Wombat', 'Rhino', 'Sloth', 'Tarantula', 'Sloth', 'Rhino', 'Sloth']
words_dict = {}
for word in words:
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1

for item in words_dict:
    print(item, ":", words_dict[item])