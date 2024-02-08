import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
adjlst = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
time = [0] * (n+1)
dp = [0]*(n+1)   # 인덱스를 번호로 가지는 건물 짓는 데 최종 소요되는 최소시간을 담을 리스트

def Topo_sort(n) :  # 위상정렬
    q = deque()

    for i in range(1, n+1) :
        if indegree[i] == 0 :  # 만약 진입차수가 0이면 해당건물을 짓는데 소요되는 시간은 단독으로 건설하는 시간과 같다
            q.append(i)    # 진입차수 0인 건물을 큐에 넣는다
            dp[i] = time[i]
    
    while q :
        cur = q.popleft()     # 큐에 넣은 건물을 하나씩 빼고

        for next in adjlst[cur] :   # 지을 수 있는 다음 건물의 진입차수를 1씩 감소
            indegree[next] -= 1
            # 다음 건물을 짓는데 소요되는 총 시간은 -> 다음건물의 소요시간에 이전건물까지의 최종소요시간을 더한 값과,  다음건물까지의 총 건설시간 중 큰 값 저장
            # 건설을 병행할 수 있으므로 긴 시간의 건물을 지으면 다른 빠른 건물들은 그 와중에 지을 수 있기에 최댓값을 저장하는 것이다
            dp[next] = max(dp[next], dp[cur] + time[next])
            if indegree[next] == 0 :
                q.append(next)


for i in range(1, n+1) :
    lst = list(map(int, input(). split()))
    time[i] = lst[0]
    if len(lst) > 2 :
        for j in range(1, len(lst)-1) :
            adjlst[lst[j]].append(i)
            indegree[i] += 1

Topo_sort(n)

print(*dp[1::], sep = "\n")


    
        