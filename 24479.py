import sys
sys.setrecursionlimit(10**5)
n, m, r = map(int, input(). split())
edges = []
lst = [0]*(n+1)
for _ in range(m) :
    edges.append(list(map(int, input(). split())))

def DFS(v, graph, chk, n) :
    global cnt, lst
    chk[v] = 1
    cnt += 1
    lst[v] = cnt
    for nv in graph[v] :
        if chk[nv] == 0 :   
           DFS(nv, graph, chk, n)
    return    

def solution(n, edges) :
    global cnt, lst
    chk = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    for [a, b] in edges :
        graph[a].append(b)
        graph[b].append(a)
    cnt = 0
    graph = [sorted(item) for item in graph]
    DFS(r, graph, chk, n)
    return lst[1:]

ans = solution(n, edges)
print(*ans, sep = "\n")