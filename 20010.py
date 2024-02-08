import sys
import heapq
from collections import deque
input = sys.stdin.readline


def Find(x) :   # 파인드
    if x == uflst[x] :
        return x
    else :
        uflst[x] = Find(uflst[x])
        return uflst[x]
    

def Union(a, b) :   # 유니온
    a = Find(a)
    b = Find(b)

    if a != b :
        uflst[max(a, b)] = min(a, b)


def BFS(start, dist) :    # 한 마을과 다른 마을간의 최장거리를 찾는 BFS
    visited = [False]*n
    q = deque()
    q.append((start, dist))
    visited[start] = True
    maxdist = 0

    while q :
        now, nowdist = q.popleft()
        maxdist = max(maxdist, nowdist)

        for next, d in adjlst[now] :
            if not visited[next] :
                visited[next] = True
                q.append((next, nowdist+d))
    
    return maxdist


n, k = map(int, input(). split())
edge = []
uflst = [i for i in range(n)]
adjlst = [[] for _ in range(n)]

for _ in range(k) :
    a, b, c = map(int, input(). split())
    heapq.heappush(edge, (c, a, b))
    
mincost = 0

while edge :
    tmp, a, b = heapq.heappop(edge)
    if Find(a) != Find(b) :  # 최소비용으로 연결된 상황에서의 마을과 마을간의 최대이용비용을 위한 엣지 선별
        Union(a, b)
        adjlst[a].append((b, tmp))   # 인접리스트에 저장
        adjlst[b].append((a, tmp))
        mincost += tmp

ans = 0
for i in range(n) :
    ans = max(ans, BFS(i, 0))

print(mincost)
print(ans)
