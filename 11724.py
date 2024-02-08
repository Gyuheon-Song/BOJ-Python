from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input(). split())
graph = [[] for _ in range(n+1)]
chk = [False] * (n+1)
ans = 0

def BFS(start) :
    Q = deque([start])
    while Q :
        for _ in range(len(Q)) :
            x = Q.popleft()
            for nx in graph[x] :
                if chk[nx] == False :
                    Q.append(nx)
                    chk[nx] = True
        
for _ in range(m) :
    a, b = map(int, input(). split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1) :
    if chk[i] == False :
        ans += 1
        BFS(i)    

print(ans)

