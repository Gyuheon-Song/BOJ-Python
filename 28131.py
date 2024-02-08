import sys
import heapq
input = sys.stdin.readline

n, m, k = map(int, input(). split())  # 노드, 간선, 지폐단위
start, end = map(int, input(). split())  # 시작, 종점
adjlst = [[] for _ in range(n+1)]   # 인접리스트

for _ in range(m) :   # 간선정보 입력받기
    u, v, w = map(int, input(). split())
    adjlst[u].append((v, w))

Q = [(0, start)]   # 시작지점까지의 거리는 0으로 지정
dp = [[1e9]*(k) for _ in range(n+1)]  # dp[노드번호][해당 노드까지의 가중치의 합 % k] = 해당노드까지의, 열의 인덱스를 나머지값으로 하는 최소비용
dp[start][0] = 0 # 시작지점까지의 비용중 나머지가 0인 경우의 최소비용을 일단 0으로 초기화

while Q :
    weight, now = heapq.heappop(Q)  # 현재노드와 해당노드까지의 최소비용을 꺼내온다

    if dp[now][weight % k] < weight :   # 해당 노드까지의 총비용을 지불단위로 나눈 나머지가 동일한, 기존 비용보다, 방금 확인한 비용이 크다면
        continue  # 최소비용이 아니므로 그대로 진행

    for next, cost in adjlst[now] :  # 해당 노드까지의 총비용을 지불단위로 나눈 나머지가 동일한, 기존 비용보다, 방금 확인한 비용이 작다면
        # 다음 노드를 인접리스트에서 확인해본다

        # 현재노드까지의 총비용에 다음노드까지의 간선의 가중치를 합한 비용을 지불단위로 나눈 나머지가 동일한, 기존의 저장된 비용보다, 
        # 현재노드까지의 총비용을 지불단위로 나눈 나머지가 동일한, 기존최소비용에 다음노드까지의 간선의 가중치를 합한 값이 작다면
        # 방금 탐색한 간선을 통하는 것이 다음노드까지의 총비용을 지불단위로 나눈 일정한 나머지를 가지는 경로의 최소비용일 것이다
        if dp[next][(weight+cost) % k] > dp[now][weight % k] + cost : 
            dp[next][(weight+cost) % k] = dp[now][weight % k] + cost
            heapq.heappush(Q, (dp[next][(weight+cost) % k], next))  # dp를 최신화

# 종착노드와 해당노드까지의 비용을 지불단위로 나누었을 때의 나머지가 0인 비용을 줄력 = dp[종착][나머지=0]
print(dp[end][0]) if dp[end][0] != 1e9 else print("IMPOSSIBLE")
