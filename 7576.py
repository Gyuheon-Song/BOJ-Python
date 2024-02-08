import sys
input = sys.stdin.readline
from collections import deque
box = []
Q = deque()
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
L = 0
m, n = map(int, input(). split())
for _ in range(n) :
    box.append(list(map(int, input(). split())))

for i in range(n) :
    for j in range(m) :
        if box[i][j] == 1 :
            Q.append([i, j])

def BFS(box) :
    global L
    while Q :
        r, c = Q.popleft()
        for k in range(4) :
            nr = r + dr[k]
            nc = c + dc[k]
            if nr >= 0 and nc >= 0 and nr < n and nc < m and box[nr][nc] == 0 :
                box[nr][nc] += box[r][c] + 1
                Q.append([nr, nc])
    

BFS(box)
ans = 0
for i in box :
    for j in i :
        if j == 0 :
            print(-1)
            exit()
    ans = max(ans, max(i))
print(ans-1)

    



