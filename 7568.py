n = int(input())
lst = []
for _ in range(n) :
    h, m = map(int, input(). split())
    lst.append([h, m])

for i in lst :
    rank = 1
    for j in lst :
        if i[0] < j[0] and i[1] < j[1] :
            rank += 1
    print(rank, end = " ")
