import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
adjlst = [[] for _ in range(n+1)]
visit = [False] * (n+1)
ans = [0] * (n+1)

for _ in range(1, n) :
    u, v = map(int, input(). split())
    adjlst[u].append(v)
    adjlst[v].append(u)

def DFS(x) :
    visit[x] = True
    for i in adjlst[x] :
        if visit[i] == False :
            ans[i] = x        # 다음에 방문할 노드의 부모노드는 현재 부모노드이다
            DFS(i)

DFS(1)

for i in range(2, n+1) :
    print(ans[i])