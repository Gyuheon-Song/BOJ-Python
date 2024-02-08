import sys
input = sys.stdin.readline

n, m = map(int, input(). split())
adjlst =[[] for _ in range(n+1)]
visited = [False] * (n+1)
dist = 0
ans = 10e9

def DFS(startnode, endnode, distance) :
    global dist, ans
    if startnode == endnode :
        ans = min(ans, distance)
        return
    else :
        for node, d in adjlst[startnode] :
            if not visited[node] :
                visited[node] = True
                DFS(node, endnode, distance+d)
                visited[node] = False

                
            
for _ in range(n-1) :
    a, b, c = map(int, input(). split())
    adjlst[a].append((b, c))
    adjlst[b].append((a, c))

for _ in range(m) :
    node1, node2 = map(int, input(). split())
    ans = 10e9
    DFS(node1, node2, 0)
    print(ans)

