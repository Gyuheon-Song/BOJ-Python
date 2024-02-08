from collections import deque
import sys
input = sys.stdin.readline
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
t = int(input())

def BFS(r, c, farm) :
    Q = deque()
    Q.append([r, c])
    farm[r][c] = 0
    while Q :
        l = len(Q)
        for _ in range(l) :
            r, c = Q.popleft()
            for k in range(4) :
                nr = r + dr[k]
                nc = c + dc[k]
                if nr >= 0 and nc >= 0 and nr < n and nc < m and farm[nr][nc] == 1 :
                    Q.append([nr, nc])
                    farm[nr][nc] = 0

for _ in range(t) :
    m, n, k = map(int, input(). split())
    farm = [[0]*(m) for _ in range(n)]
    cnt = 0
    for _ in range(k) :
        b, a = map(int, input(). split())
        farm[a][b] = 1
    for i in range(n) :
        for j in range(m) :
            if farm[i][j] == 1 :
                cnt += 1
                BFS(i, j, farm)
    print(cnt)


        



