import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
adjlst = [[] for _ in range(n+1)]
indegree = [0] * (n+1)   # 진입차수를 저장하기 위한 리스트
dp = [0] * (n+1)     # 인덱스를 번호로 가지는 작업을 하는데까지 걸리는 최종 소요시간을 저장할 리스트
time = [0] * (n+1)   # 각 작업을 단독으로 하는데 소요되는 시간 리스트

def Topo_sort(n) :   # 위상정렬 알고리즘
    q = deque()

    for i in range(1, n+1) :
        if indegree[i] == 0 :   # 진입차수가 0인 작업번호를 뮤에 넣고
            q.append(i)
            dp[i] = time[i]   # dp를 단독작업시간으로 초기화
    
    while q :
        cur = q.popleft()    # 현재연산하는 작업

        for next in adjlst[cur] :   # 다음 작업의 진입차수를 1 감소시킨다
            indegree[next] -= 1
            # 다음작업의 총 소요시간을 -> 다음작업에 이미 저장된 총소요시간과,  현재 작업에 소요되는 총 시간 + 다음 작업의 단독작업시간 중 큰 값 저장
            dp[next] = max(dp[next], dp[cur] + time[next])
            if indegree[next] == 0 :   # 진입차수가 0 이라면 큐에 저장
                q.append(next)
    

for i in range(1, n+1) :
    lst = list(map(int, input(). split()))
    time[i] = lst[0]
    dp[i] = time[i]
    for j in lst[2::] :
        adjlst[j].append(i)
        indegree[i] += 1

Topo_sort(n)

print(max(dp))
    