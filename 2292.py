n = int(input())

k = 6
i = 1
cnt = 1
sum = 1
if n > 1 :
    while sum < n :
        sum += k
        k += 6
        cnt += 1

print(cnt)