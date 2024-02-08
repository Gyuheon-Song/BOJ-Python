a, b = map(int, input(). split())
k = int(b ** 0.5)
lst = [False] * (k+1)
cnt = 0
ans = []

for i in range(2, k+1) :
    if lst[i] == False :
        for j in range(i+i, k+1, i) :
            lst[j] = True

for i in range(2, k+1) :
    if lst[i] == False :
        ans.append(i)

for num in ans :
    i = 2
    while num ** i <= b :
        if a <= num**i <= b :
            cnt += 1
        i += 1

print(cnt)
