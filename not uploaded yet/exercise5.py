the_list = "ACTNGTGCTYGATRGTAGCYXGTN"
counter = {}

for A in the_list:
    if A in counter:
        counter[A] += 1
    else:
        counter[A] = 1

for a in counter.keys():
    f = counter[a]/len(the_list)*100
    print(f'{a} {counter[a]} - {f:.2f}"%')