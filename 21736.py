from collections import deque
import sys

n, m = map(int, input(). split())
campus = []
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
cnt = 0

for i in range(n) :
    campus.append(list(sys.stdin.readline().strip()))

def BFS(r, c, campus) :
    global cnt
    Q = deque()
    Q.append([r, c])
    campus[r][c] = "X"
    while Q :
        r, c = Q.popleft()
        for k in range(4) :
            nr = r + dr[k]
            nc = c + dc[k]
            if nr >= 0 and nc >= 0 and nr < n and nc < m and campus[nr][nc] != "X" :
                if campus[nr][nc] == "O" :
                    campus[nr][nc] = "X"
                    Q.append([nr, nc])
                elif campus[nr][nc] == "P" :
                    cnt += 1
                    campus[nr][nc] = "X"
                    Q.append([nr, nc])


for i in range(n) :
    for j in range(m) :
        if campus[i][j] == "I" :
            BFS(i, j, campus)

print("TT") if cnt == 0 else print(cnt)

