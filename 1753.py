import sys
import heapq 
input = sys.stdin.readline

V, E = map(int, input(). split())
k = int(input())
graph = [[] for _ in range(V+1)]    # 인접리스트 생성
visited = [False] * (V+1)    # 방문배열
d = [sys.maxsize] * (V+1)    # 충분히 큰 값으로 거리 리스트 초기화
hq = []
                  

for _ in range(E) :
    u, v, w = map(int, input(). split())
    graph[u].append((v, w))

heapq.heappush(hq, (0, k))     # 우선순위 큐에서의 최솟값 정렬을 위해 거리값이 필요하고
d[k] = 0                   # 시작점의 거리의 값이 0 이므로 (0, k) 를 넣어주게 된다
                           # 이후로는 거리리스트의 값을 (d[next], next node) 의 형식으로 넣는다
while len(hq) > 0 :
    current = heapq.heappop(hq)
    c_v = current[1]
    if visited[c_v] :      # 이미 방문한 적이 있는 노드이면 와일문을 한번 돌린다
        continue
    visited[c_v] = True    # 방문하게 된 노드를 True로 바꾸어 방문표시
    for tmp in graph[c_v] :
        next = tmp[0]
        value = tmp[1]
        if d[next] > d[c_v] + value :     # 목표노드의 거리리스트의 값보다 현재노드의 거리리스트의 값에 가중치를 더한
            d[next] = d[c_v] + value      # 값이 더 작을 때
            heapq.heappush(hq, (d[next], next))

for i in range(1, V+1) :
    if visited[i] :
        print(d[i])
    else :
        print("INF")



