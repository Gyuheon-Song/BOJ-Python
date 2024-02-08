n = int(input())

lst = [0] * (6)
if n >= 6 :
    lst = lst + [0]*(n-5)

lst[0] = -1
lst[1] = -1
lst[2] = 1
lst[3] = -1
lst[4] = 2
lst[5] = 1

for i in range(6, n+1) :
    if lst[i-2] != -1 and lst[i-5] != -1 :
        lst[i] = min(lst[i-2]+1, lst[i-5]+1)
    elif lst[i-2] == -1 :
        lst[i] = lst[i-5] + 1
    elif lst[i-5] == -1 :
        lst[i] = lst[i-2] + 1

print(lst[n])