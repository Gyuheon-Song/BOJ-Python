import sys
input = sys.stdin.readline
ans = 0
def Z(x, r, c) :
    global ans
    if r == row and c == col :
        print(ans)
        exit()
    if not (r <= row < r + x and c <= col < c + x) :
        ans += x**2
        return
    Z(x//2, r, c)
    Z(x//2, r, c + x//2)
    Z(x//2, r + x//2, c)
    Z(x//2, r + x//2, c + x//2)

n, row, col = map(int, input(). split())
Z(2**n, 0, 0)


