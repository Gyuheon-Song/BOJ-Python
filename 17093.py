import sys
import math
input = sys.stdin.readline

n, m = map(int, input().strip(). split())

def Distance(x1, y1, x2, y2) :
    return math.pow(abs(x2-x1), 2) + math.pow(abs(y2-y1), 2)

P = []
ans = 0

for _ in range(n) :
    P.append(list(map(int, input().strip(). split())))

for _ in range(m) :
    x, y = map(int, input().strip(). split())
    for p in P :
        ans = max(ans, Distance(p[0], p[1], x, y))

print(int(ans))

