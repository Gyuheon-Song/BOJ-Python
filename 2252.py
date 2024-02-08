import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input(). split())
adjlst = [[] for _ in range(n+1)]
indegree = [0] * (n+1)   # 위상정렬을 실행하기 위한 진입차수 리스트

for _ in range(m) :
    a, b = map(int, input(). split())
    adjlst[a].append(b)  # edge를 인접리스트에 저장
    indegree[b] += 1    # 저장할때마다 도착노드의 진입차수를 1씩 증가

def topo_sort() :   # 위상정렬 알고리즘
    q = deque()    # 큐

    for i in range(1, n+1) :   # 집입차수가 0인 노드를 큐에 집어넣는다
        if indegree[i] == 0 :
            q.append(i)            
    
    while q :    # 큐에 노드가 있으면 반복
        start = q.popleft()
        print(start, end = " ")   

        for end in adjlst[start] :     # 꺼낸 노드에서 갈 수 있는 노드가 있다면
            indegree[end] -= 1    # 그 도착노드의 진입차수를 1뺀다(도착노드로 가는 간선을 지운다)
            if indegree[end] == 0 :    # 만약 도착노드의 진입차수가 0이라면 큐에 넣는다
                q.append(end)

topo_sort()



