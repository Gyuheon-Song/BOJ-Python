import sys
import math
input = sys.stdin.readline

n = int(input())

for _ in range(n) :
    x1, y1, r1, x2, y2, r2 = map(int, input(). split())
    d = math.sqrt(((x1-x2)**2) + ((y1-y2)**2))
    dr = r1 + r2

    if d == 0 :
        if r1 == r2 :
            print(-1)
        else :
            print(0)
    elif d == dr :
        print(1)
    elif d < dr :
        if d + min(r1, r2) < max(r1, r2) :
            print(0)
        elif d + min(r1, r2) == max(r1, r2) :
            print(1)
        else :
            print(2)
    else :
        print(0)
