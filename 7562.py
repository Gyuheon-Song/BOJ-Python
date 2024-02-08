from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
dr = [-2, -1, 1, 2, 2, 1, -1, -2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]

def BFS(start, end, board) :
    global L
    Q = deque()
    Q.append(start)
    board[start[0]][start[1]] = 1
    L = 0
    while Q :
        l = len(Q)
        for _ in range(l) :
            r, c = Q.popleft()
            if r == end[0] and c == end[1] :
                return L
            for k in range(8) :
                nr = r + dr[k]
                nc = c + dc[k]
                if nr >= 0 and nc >= 0 and nr < size and nc < size and board[nr][nc] == 0 :
                    Q.append([nr, nc])
                    board[nr][nc] = 1
        L += 1

for i in range(n) :
    size = int(input())
    start = list(map(int, input(). split()))
    end = list(map(int, input(). split()))
    board = [[0]*(size) for _ in range(size)]
    BFS(start, end, board)
    print(L)
