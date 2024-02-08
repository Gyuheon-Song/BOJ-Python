from collections import deque
a, b = map(int, input(). split())
maze = []
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
for _ in range(a) :
    maze.append(list(map(int, input())))

def BFS(r, c, maze) :
    global L
    Q = deque()
    Q.append([r, c])
    L = 1
    while Q :
        l = len(Q)
        for i in range(l) :
            r, c = Q.popleft()
            if r == a-1 and c == b-1 :
                return L
            for k in range(4) :
                nr = r + dr[k]
                nc = c + dc[k]
                if nr >= 0 and nc >= 0 and nr < a and nc < b and maze[nr][nc] == 1:
                    Q.append([nr, nc])
                    maze[nr][nc] = 0
        L += 1

BFS(0,0,maze)
print(L)



