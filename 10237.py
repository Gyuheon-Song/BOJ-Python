import sys
from collections import deque
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

t = int(input())


def Topo_sort(now) :    # 위상정렬

    if dp[now] != 0 :
        return dp[now]  

    for i in range(len(adjlst[now])) :
        next = adjlst[now][i][0]
        weight = adjlst[now][i][1]
        tmp = Topo_sort(next) - weight

        if tmp > dp[now] :
            dp[now] = tmp
            path[now] = next
    
    dp[now] += value[now]
    
    return dp[now]

for _ in range(t) :
    n, e = map(int, input(). split())
    adjlst = [[] for _ in range(n+1)]  # 인접리스트
    value = [0] + list(map(int, input(). split()))   # 동굴별 광석 가치
    path = [0] * (n+1)   # 탐사경로 리스트
    dp = [0] * (n+1)   # 최대수익을 저장할 리스트
    ans = []
    for _ in range(e) :
        a, b, c = map(int, input(). split())
        adjlst[a].append((b, c))    

    Topo_sort(1)

    temp = 1
    while temp != 0 :
        ans.append(temp)
        temp = path[temp]

    print(dp[1], len(ans))
    print(*ans)