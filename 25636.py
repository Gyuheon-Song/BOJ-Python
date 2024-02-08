import sys
import heapq
input = sys.stdin.readline

def Dijkstra(start) :  # 다익스트라

    d[start] = 0  # 소방서가 위치한 곳의 거리를 0으로 설정하고 각 교차로 까지의 최단거리를 구한다
    water[start] = a[start]  # 소방서에서 물을 일단 충전하고 출발한다

    while Q :
        distance, cur = heapq.heappop(Q)   # 현재 교차로까지의 최단거리와 현재 교차로를 최소힙에서 뽑아온다
        
        if distance > d[cur] :  # 현재 교차로까지의 최단거리가 최적의 경우가 아닐 때 굳이 밑의 조건문을 돌리지 않는다
            continue

        for next, dist in adjlst[cur] :  # 다음노드와 현재노드에서 다음노드까지 잇는 엣지의 가중치
            if distance + dist < d[next] :  # 방금 탐색한 엣지의 가중치를 더한 것이 기존의 최소거리보다 작다면 최신화
                water[next] = water[cur] + a[next] # 최단거리가 탐색된 것이므로 해당 경로를 무조건 타야 하므로 
                                                    # 물은 무조건 충전을 하고 간다
                d[next] = distance + dist   # 최단거리 최신화
                heapq.heappush(Q, (d[next], next))   # 최소힙에 넣어준다

            if distance + dist == d[next] :   # 만약 기존의 최단거리와 동일한 거리의 경로라면 물을 더 많이 충전할 수 있는지만 판단
                if water[cur] + a[next] > water[next] :   # 동일한 최단거리를 가지는 기존 경로의 물 충전량보다 방금 탐색한 경로의 물 충전량이 많다면
                    water[next] = water[cur] + a[next]    # 최대 물 충전량만 최신화
                    
                   
n = int(input())
a = [0] + list(map(int, input(). split()))   # 각 교차로에서 충전할 수 있는 물의 양을 저장한 리스트
m = int(input())  # 간선의 개수
adjlst = [[] for _ in range(n+1)]   # 인접리스트
water = [0] * (n+1)    # 인덱스번호에 해당하는 교차로까지가는 경로상에서 충전할 수 있는 최대 물 양을 저장하는 리스트
d = [float('inf')]*(n+1)    # 최단거리 리스트

for _ in range(m) :    # 양방향 간선정보를 인접리스트에 저장
    u, v, w = map(int, input(). split())
    adjlst[u].append((v, w))
    adjlst[v].append((u, w))

s, t = map(int, input(). split())    # 소방서가 위치한 곳과 화재가 난 교차로의 번호

Q = [(0, s)]    # 최소힙에 먼저 초기거리(0)와 출발위치(소방서의 위치)를 저장

Dijkstra(s)   # 다익스트라

# 최단거리가 초기화된 적이 없다면 경로가 존재하지 않으므로 -1출력
# 최단거리 존재할 시 최단거리와 해당 교차로까지의 경로상에서 최대 충전가능한 물의 양 출력
print(d[t], water[t]) if d[t] != float('inf') else print(-1)