letter = "ACCGXXCXXGTTACTGGGCXTTGT"

sort_out = letter[0] + letter[2] + letter[letter.index('T')] + letter[letter.index('G')]

print(sort_out)

to_list = letter.split("X")
sort_list = sorted(to_list, key = len, reverse=True)
sort_list = [x for x in sort_list if len(x) > 0 ]

print(sort_list)