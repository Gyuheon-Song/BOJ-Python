from collections import deque
import sys
input = sys.stdin.readline
n, m, r = map(int, input(). split())
edges = []
cnt = 1
chk = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for i in range(m) :
    a, b = list(map(int, input(). split()))
    graph[a].append(b)
    graph[b].append(a)
graph = [sorted(item) for item in graph]

def BFS(r, graph, chk) :
    global cnt
    Q = deque()
    Q.append(r)
    chk[r] = 1
    while Q :
        x = Q.popleft()
        for i in graph[x] :
            if chk[i] == 0 :
                Q.append(i)
                cnt += 1
                chk[i] = cnt

BFS(r, graph, chk)
for i in chk[1::] :
    print(i)
