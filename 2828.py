import sys
n, m = map(int, input(). strip(). split())
j = int(input())
l = 1
r = m
cnt = 0

for i in range(j) :
    pos = int(input())
    if l <= pos <= r :
        continue
    else :
        if pos < l :
            while pos < l :
                l -= 1
                r -= 1
                cnt += 1
        else :
            while pos > r :
                l += 1
                r += 1
                cnt += 1

print(cnt)