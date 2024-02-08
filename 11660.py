import sys
input = sys.stdin.readline
n, m = map(int, input(). split())
lst = [[0]*(n+1)]
for i in range(1, n+1) :
    lst.append([0]+list(map(int, input(). split())))

sumlst = [[0]*(n+1) for _ in range(n+1)]


for i in range(1, n+1) :
    for j in range(1, n+1) :
        sumlst[i][j] = sumlst[i][j-1] + sumlst[i-1][j] - sumlst[i-1][j-1] + lst[i][j]
        

for _ in range(m) :
    r1, c1, r2, c2 = map(int, input(). split())
    ans = sumlst[r2][c2] - sumlst[r2][c1-1] -sumlst[r1-1][c2] + sumlst[r1-1][c1-1]
    print(ans)

