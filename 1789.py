s = int(input())

n = 1
k = 2
cnt = 1

while n <= s :
    n += k
    k += 1
    cnt += 1

print(cnt-1)
