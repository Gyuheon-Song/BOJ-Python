import sys
input = sys.stdin.readline

n, m, b = map(int, input(). split())
arr = [list(map(int, input(). split())) for _ in range(n)]
min_time = sys.maxsize
height = 0

for i in range(257) :
    dig = 0
    stack = 0
    for j in range(n) :
        for k in range(m) :
            if arr[j][k] >= i :
                dig += arr[j][k] - i
            else :
                stack += i -arr[j][k]

    if stack > dig + b :
        continue
    time = stack + (dig * 2)
    if time <= min_time :
        min_time = time
        height = i

print(min_time, height) 