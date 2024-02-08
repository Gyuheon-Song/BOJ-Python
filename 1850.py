import sys
input = sys.stdin.readline
n, m = map(int, input(). split())

if n > m :
    a, b = n, m
else :
    a, b = m, n

def Euclid(x, y) :
    r = x % y
    while r != 0 :
        x, y = y, r
        return Euclid(x, y)

    return y

ans = "1"* Euclid(a, b)

print("".join(ans))

