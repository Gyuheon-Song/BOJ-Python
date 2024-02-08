import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

adjlst = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cost = [sys.maxsize] * (n+1)
hq = []
prev_node = [0] * (n+1)   # 최소비용의 간선으로 이어진 노드의 앞 노드를 저장하는리스트 생성

for _ in range(m) : 
    u, v, c = map(int, input(). split())
    adjlst[u].append((v, c))

depart, arrive = map(int, input(). split())

heapq.heappush(hq, (0, depart))
cost[depart] = 0

while hq :
    now = heapq.heappop(hq)
    now_node = now[1]
    if visited[now_node] == True :
        continue
    visited[now_node] = True
    for temp in adjlst[now_node] :
        next_node = temp[0]
        pay = temp[1]
        if cost[next_node] > cost[now_node] + pay :
            cost[next_node] = cost[now_node] + pay
            prev_node[next_node] = now_node      # 다음 노드까지의 현재노드에서부터의 비용이 최소일 때 앞전 노드로 초기화
            heapq.heappush(hq, (cost[next_node], next_node))

path = [arrive]    # 경로리스트에 도착노드를 넣어놓고 거슬러 올라간다
backtrack = arrive

while backtrack != depart :         # 경로의 역추적이 출발노드가 될 때까지 와일문 진행
    backtrack = prev_node[backtrack]    # 역추적 값을 이전노드 저장 리스트의 값으로 최신화
    path.append(backtrack)          # 도착지점으로부터 추적해나가며 최신화된 이전 노드들을 경로리스트에 append

path.reverse()               # 경로리스트는 도착지점부터 출발지점까지 역으로 추적되었기에 경로리스트를 출발노드부터 올바르게 정렬

print(cost[arrive])
print(len(path))
print(*path)

