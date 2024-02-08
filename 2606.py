import sys
input = sys.stdin.readline
v = int(input())
e = int(input())
graph = [[] for _ in range(v+1)]
chk = [0]*(v+1)
cnt = 0
for _ in range(e) :
    a, b = map(int, input(). split())
    graph[a].append(b)
    graph[b].append(a)

def DFS(r) :
    global cnt
    chk[r] = 1
    for dr in graph[r] :
        if chk[dr] == 0 :
            cnt += 1
            DFS(dr)
DFS(1)

print(cnt)
    

