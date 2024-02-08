from collections import deque
import sys

board = []
visited = []
n, m = map(int, input(). split())
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
    
def BFS(r, c, board) :
    Q = deque()
    Q.append([r, c])
    
    while Q :
        r, c = Q.popleft()
        for k in range(4) :
            nr = r + dr[k]
            nc = c + dc[k]
            if nr >= 0 and nc >= 0 and nr < n and nc < m and visited[nr][nc] == -1 and board[nr][nc] == 1 :
                board[nr][nc] = board[r][c] + 1 
                visited[nr][nc] = 1
                Q.append([nr, nc])   

for _ in range(n) :
    row = list(map(int, input(). split()))
    board.append(row)
    visited.append([-1]*(m))

for i in range(n) :
    for j in range(m) :
        if board[i][j] == 2 :
            a, b = i, j
            break      

board[a][b] = 0
visited[a][b] = 1
BFS(a, b, board)

for i in range(n) :
    for j in range(m) :
        if board[i][j] == 1 and visited[i][j] == -1 :
            board[i][j] = -1

for item in board :
    print(*item)
