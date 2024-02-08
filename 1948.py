import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
adjlst = [[] for _ in range(n+1)]
indegree = [0] * (n+1)   # 진입차수 리스트
time = [0] * (n+1)   # 시간 리스트
prev = [[] for _ in range(n+1)]    # 역추적을 위한 이전노드를 담는 리스트

for _ in range(m) :
    a, b, c = map(int, input(). split())
    adjlst[a].append((b, c))
    indegree[b] += 1

start, end = map(int, input(). split())

def Topo_sort() :   # 위상정렬 알고리즘
    q = deque()

    for i in range(1, n+1) :   # 진입차수 0인 경우만 큐에 담는다
        if indegree[i] == 0 :
            q.append(i)
    
    while q :
        now = q.popleft()

        for next, t in adjlst[now] :   # 다음노드와 가중치를 언팩하고
            indegree[next] -= 1   # 다음노드의 진입차수 1 감소
            if time[next] <= time[now] + t :   # 만약 다음노드까지 걸리는 시간의 최근값보다 현재노드까지 걸리는 시간에 가중치를 더한 값이 크다면
                time[next] = time[now] + t     # 다음노드까지 걸리는 시간 초기화
                prev[next].append((now, t))    # 다음노드의 이전노드에 현재노드와 다음노드로 가는 가중치 저장
            if indegree[next] == 0 :   # 만약 진입차수가 0인 다음노드는
                q.append(next)    # 큐에 넣어준다

def No_rest(k) :   # 가장 오래 걸리는 경로의 총 노드수를 구하자
    global edge
    q = deque()
    q.append(k)   

    while q :
        now = q.popleft()

        for before, t in prev[now] :   # 이전노드들을 담았던 리스트에서 언패킹
            if time[before] == time[now] - t :   # 이전노드까지 걸리는 최대시간이 현재노드에서 해당 엣지의 가중치를 뺀 값과 동일하다면
                                                 # 해당 엣지가 최대시간이 소요되는 경로의 일부라는 의미이므로
                edge += 1     # 엣지 카운트 올려주자
                if not backtrack[before] : # 만약 방금 다룬 이전노드가 이전에 탐색하지 않았더라면 
                    backtrack[before] = True     # 탐색한 것으로 표지하고
                    q.append(before)    # 큐에 넣어준다

Topo_sort()
edge = 0   # 엣지의 개수 초기화선언
backtrack = [False] * (n+1)   # 중복탐색을 막기 위한 리스트
No_rest(end)   # 도착노드에서 역추적하자

print(max(time), edge, sep = "\n")

