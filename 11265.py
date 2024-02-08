import sys
input = sys.stdin.readline

n, m = map(int, input(). split())
adjmtrx = [[0 for _ in range(n+1)]]
for _ in range(n) :
    lst = [0] + list(map(int, input(). split()))
    adjmtrx.append(lst)

for k in range(1, n+1) :
    for i in range(1, n+1) :
        for j in range(1, n+1) :
            adjmtrx[i][j] = min(adjmtrx[i][j], adjmtrx[i][k]+adjmtrx[k][j])

for _ in range(m) :
    a, b, c = map(int, input(). split())
    if c >= adjmtrx[a][b] :
        print("Enjoy other party")
    else :
        print("Stay here")