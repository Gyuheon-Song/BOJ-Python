def Star(n, row, col) :
    if n == 3 :
        for i in range(3) :
            result[row][col+i] = "*"
            result[row+2][col+i] = "*"
        result[row+1][col] = result[row+1][col+2] = "*"
    else :
        Star(n//3, row, col)
        Star(n//3, row, col+n//3)
        Star(n//3, row, col+2*(n//3))
        Star(n//3, row+n//3, col)
        Star(n//3, row+n//3, col+2*(n//3))
        Star(n//3, row+2*(n//3), col)
        Star(n//3, row+2*(n//3), col+n//3)
        Star(n//3, row+2*(n//3), col+2*(n//3))

n = int(input())
result = [[" "] * (n) for _ in range(n)]
Star(n, 0, 0)
for k in result :
    print("".join(k))