import sys
from collections import deque
input = sys.stdin.readline

def BFS(start, end) :
    global ans
    ans = 0
    visited = [False] * (n+1)
    queue = deque()
    queue.append((start, 0))
    visited[start] = True

    while queue :
        now, dist = queue.popleft()
        if now == end :
            ans = dist
            return
        for next, d in adjlst[now] :
            if not visited[next] :
                visited[next] = True
                queue.append((next, dist+d))
            
            
n, m = map(int, input(). split())
adjlst = [[] for _ in range(n+1)]

for _ in range(n-1) :
    a, b, c = map(int, input(). split())
    adjlst[a].append((b, c))
    adjlst[b].append((a, c))

for _ in range(m) :
    node1, node2 = map(int, input(). split())
    BFS(node1, node2)
    print(ans)


