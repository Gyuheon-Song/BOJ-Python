import sys
from collections import deque
import heapq
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


def BFS(k) :    # k 학생에 대해 각 학생들과의 연락하는 최대비용을 찾는 BFS
    q = deque()
    visited = [False]*(n+1)  # 방문배열 
    q.append((k, 0))   # k 학생과 자기자신과 연락비용은 0
    visited[k] = True  # 방문표지

    while q :    
        now, ccost = q.popleft()    # 현재 탐색중 학생과 현재까지의 최대연락비용을 의미한다

        for next, ncost in adjlst[now] :  # 다음학생과, 그 간선의 연락비용에 대해
            if not visited[next] :   # 아직 탐색하지 않았다면
                visited[next] = True   
                distance[k][next] = max(ccost, ncost)   # 최고비용배열에 이전 간선의 비용과 방금 탐색 비용중 큰 값을 저장
                q.append((next, distance[k][next]))     # 최신화해나가고 있는 k부터 각 학생까지의 경로상 최대비용을 다시 넘겨주며 진행


n, m = map(int, input(). split())
edge = []
uflst = [i for i in range(n+1)]   # 유니온 파인드 리스트
adjlst = [[] for _ in range(n+1)]    # 간선정보를 저장할 인접리스트(BFS용)
distance = [[0]*(n+1) for _ in range(n+1)]   # i행 j열은 i학생의 연락이 j학생에게 까지 가는 경로에서의 가장 높은 비용을 저장

for _ in range(m) :
    a, b, c = map(int, input(). split())
    heapq.heappush(edge, (c, a, b))   # 우선순위큐에 가중치를 기준으로 하여 간선정보 저장

total = 0   # MST의 총비용
while edge :
    cost, s, e = heapq.heappop(edge)

    if Find(s) != Find(e) :   # 서로 부모노드가 다르면
        Union(s, e)   # 두 학생을 연결
        adjlst[s].append((e, cost))
        adjlst[e].append((s, cost))
        total += cost   # 총비용 더해나가자

for i in range(1, n+1) :   # 각 학생들에 대해 다른 각 학생에 대하여 연락하는 경로의 최댓값들을 찾아놓자
    BFS(i)

q = int(input())
for _ in range(q) :
    x, y = map(int, input(). split())
    print(total-distance[x][y])   # 총 비용에서 두 팀장간의 연락경로 중 가장 비싼 간선을 끊어주면 된다