import sys
import heapq
input = sys.stdin.readline
n = int(input())
m = int(input())
adjlst = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cost = [sys.maxsize] * (n+1)   # 비용리스트를 충분히 큰 값으로 설정
hq = []

for _ in range(m) :
    u, v, c = map(int, input(). split())
    adjlst[u].append((v, c))

depart, arrive = map(int, input(). split())

heapq.heappush(hq, (0, depart))   # 최소 힙에서 최소비용 정렬을 위해 시작점의 비용을 0으로 하여 힙에 푸쉬
cost[depart] = 0    # 출발지점의 비용은 0

while len(hq) > 0 :
    now = heapq.heappop(hq)
    now_node = now[1]
    if visited[now_node] == True :     # 이미 방문한 노드이면 와일문 한번 돌림
        continue
    visited[now_node] = True
    for temp in adjlst[now_node] :     
        next_node = temp[0]            # 인접리스트의 원소의 인덱스 0이 다음 노드
        pay = temp[1]                  # 인접리스트의 원소의 인덱스 1이 해당 노드까지의 간선의 비용
        if cost[next_node] > cost[now_node] + pay :      # 비용리스트에서 해당 노드까지의 원래 비용보다, 가장 최근의 연산의 노드까지의 비용에 최근비용을 합한게 적다면
            cost[next_node] = cost[now_node] + pay       # 해당 노드까지의 비용을 최솟값으로 초기화
            heapq.heappush(hq, (cost[next_node], next_node))   # 최소힙에 비용순으로 정렬되도록 다음 노드의 간선정보 입력

print(cost[arrive])   