import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
from collections import deque

n, m, r = map(int, input(). split())
Q = deque()
graph = [[] for _ in range(n+1)]
chk1 = [0]*(n+1)
chk2 = [0]*(n+1)
dfsans = []
bfsans = []
for _ in range(m) :
    a, b = map(int, input(). split())
    graph[a].append(b)
    graph[b].append(a)
graph = [sorted(item) for item in graph]

def DFS(r) :
    chk1[r] = 1
    dfsans.append(r)
    for dr in graph[r] :
        if chk1[dr] == 0 :
            DFS(dr)

def BFS(r) :
    Q.append(r)
    chk2[r] = 1
    bfsans.append(r)
    while Q :
        x = Q.popleft()
        for i in graph[x] :
            if chk2[i] == 0 :
                Q.append(i)
                bfsans.append(i)
                chk2[i] = 1
DFS(r)
print(*dfsans)
BFS(r)
print(*bfsans)
                