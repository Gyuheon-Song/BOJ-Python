# 벨만-포드 알고리즘
import sys
input = sys.stdin.readline

n, m = map(int, input(). split())
distance = [sys.maxsize] * (n+1)
edge = []

for _ in range(m) :
    s, e, d = map(int, input(). split())
    edge.append((s, e, d))

distance[1] = 0     # 시작점 거리 1로 초기화

for _ in range(n-1) :          # node의 개수가 n개일때 n-1번의 edge안에서 최단거리를 무조건 구할 수 있기에
    for s, e, d in edge :      
        if distance[s] != sys.maxsize and distance[e] > distance[s] + d :
            distance[e] = distance[s] + d
    # 위의 과정에서 최단거리가 구해진다

negcycle = False

# 한번 더 엣지 탐색을 돌렸을때 업데이트가 발생하면 음수사이클 존재
for s, e, d in edge :      
        if distance[s] != sys.maxsize and distance[e] > distance[s] + d :
            negcycle = True
            break

if not negcycle :    # 음수사이클이 존재하지 않을 때
     for i in range(2, n+1) :
        if distance[i] != sys.maxsize :    # 도달할 수 있는 노드일때(업데이트가 발생한 노드일때)
            print(distance[i])
        else :                            # 도달할 수 없는 노드일때(업데이트가 발생하지 않은 노드일때)
            print(-1)
else :
    print(-1)