n = int(input())
cnt = 0
while n % 5 != 0 and n >= 0:
    n -= 3
    cnt += 1

if n < 0 :
    print(-1)
else :
    print(cnt + n//5)