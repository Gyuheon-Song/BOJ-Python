from collections import deque
n = int(input())
apart = []
lst = []
group = 0
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
for _ in range(n) :
    apart.append(list(map(int, input())))

def BFS(r, c, apart) :
    Q = deque()
    Q.append([r, c])
    apart[r][c] = 0
    cnt = 1
    while Q :
        l = len(Q)
        for _ in range(l) :
            r, c = Q.popleft()
            for k in range(4) :
                nr = r + dr[k]
                nc = c + dc[k]
                if nr >= 0 and nc >= 0 and nr < n and nc < n and apart[nr][nc] == 1 :
                    Q.append([nr, nc])
                    apart[nr][nc] = 0
                    cnt += 1
    lst.append(cnt)

for i in range(n) :
    for j in range(n) :
        if apart[i][j] == 1 :
            group += 1
            BFS(i, j, apart)

print(group)
lst.sort()
for item in lst :
    print(item)

            
