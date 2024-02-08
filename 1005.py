import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

def topo_sort(n) :   # 위상정렬 알고리즘
    q = deque()

    for i in range(1, n+1) :    # 모든 건물들에 대해
        if indegree[i] == 0 :   # 진입차수가 0 인 건물번호를 큐에 저장
            q.append(i)
            dp[i] = time[i]     # 해당 건물을 짓는 시간을 저장
    
    while q :    # 큐에 건물이 있을때
        start = q.popleft()   # 큐에서 하나씩 뺀다
        for end in adjlst[start] :    # 다음에 지을 수 있는 건물들에 대해
            indegree[end] -= 1     # 다음건물의 진입차수를 1 감소
            dp[end] = max(dp[start] + time[end], dp[end])   # dp에 다음건물을 짓는데까지의 총 건설시간과,
                                                # 이전건물을 건설하는데까지의 총 건설시간 + 다음건물 단독으로 짓는데 소요되는시간 중 최댓값저장한다
                                                # 같은 선 건설조건을 가지고 있는 건물은 긴 시간이 걸리는 건물이 지어지는동안 빠른 건물은 이미 지어지기 때문
            if indegree[end] == 0 :
                q.append(end)


for _ in range(t) :
    n, k = map(int, input(). split())
    adjlst = [[] for _ in range(n+1)]   # 연결된 건물을 저장하는 인접리스트
    indegree = [0] * (n+1)     # 진입차수를 저장하는 리스트
    time = [0] + list(map(int, input(). split()))    # 건물별 건설시간 저장 리스트
    dp = [0] * (n+1)     # 해당 인덱스 번호를 가진 건물까지 건설하는데 걸리는 총 시간
    
    for _ in range(k) :
        a, b = map(int, input(). split())
        adjlst[a].append(b)   # edge정보를 인접리스트에 저장
        indegree[b] += 1      # 나중에 지을 수 있는 건물의 진입차수를 1 증가
    
    topo_sort(n)  # 위상정렬알고리즘

    build = int(input())   # 소요되는 건설시간을 알고자 하는 건물 번호
    print(dp[build])       # dp의 건물번호의 인덱스에 그 정보가 저장되어있다
    
   