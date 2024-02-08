import sys
input = sys.stdin.readline
from collections import deque

Q = deque()
dr = [-1, 0, 1, 0, 0, 0]
dc = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

m, n, h = map(int, input(). split())
box = [[] for _ in range(h)]

for q in range(h) :    
    for _ in range(n) :
        box[q].append(list(map(int, input(). split())))


def BFS() :
    while Q :
        z, r, c = Q.popleft()
        for k in range(6) :
            nr = r + dr[k]
            nc = c + dc[k]
            nz = z + dz[k]
            if 0 <= nr < n and 0 <= nc < m and 0 <= nz < h :
                if box[nz][nr][nc] == 0 :
                    box[nz][nr][nc] += box[z][r][c] + 1
                    Q.append([nz, nr, nc])

for i in range(h) :
    for j in range(n) :
        for p in range(m) :
            if box[i][j][p] == 1 :
                Q.append([i, j, p])
BFS()

ans = 0
for i in box :
    for j in i :
        for s in j :
            if s == 0 :
                print(-1)
                exit()
        ans = max(ans, max(j))
print(ans-1)


