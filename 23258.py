import sys
input = sys.stdin.readline

n, q = map(int, input(). split())

# 문제의 조건을 만족시키기위해서는 반딧불이의 용량이 C일때, 경유과정에서 들를 수 있는 집의 최대번호는 C-1 이하여야 한다
# 따라서 플로이드 워셜을 위한 3차원 최단거리 인접행렬(dp느낌)
# house[최단거리에서 경유하는 집의 최대번호][출발집번호][도착집번호]
house = [[[float('inf')]*(n+1) for _ in range(n+1)] for _ in range(n+1)]

# 인접행렬의 포맷으로 되어있는 간선정보를 입력받는다
for i in range(1, n+1) :
    tmp = [0] + list(map(int, input(). split()))
    for j in range(1, n+1) :
        house[0][i][j] = tmp[j]  # 처음 입력받을때는 경유지 없으므로 [0][][]에 저장
        if i != j and tmp[j] == 0 :  # 서로다른 집 i와 j를 잇는 간선이 없는경우
            house[0][i][j] = float('inf')  # 최댓값으로 초기화

# 플로이드-워셜
for via in range(1, n+1) :  # 경유지
    for d in range(1, n+1) :
        for a in range(1, n+1) :
            if d == a or a == via or via == d :   # 출발지와 도착지와 경유지 중 어느 두개라도 일치하면
                house[via][d][a] = house[via-1][d][a] # 동일한 경로이다
            else :
                # (via-1)번 이하의 번호의 집을 경유하는 출발->도착의 기존의 최단경로와
                # (via-1)번 이하의 번호의 집을 경유하며 출발집->via번 집 + (via-1)번 이하의 번호의 집을 경유하며 via번집->도착집
                # 비교하여 작은값 저장
                house[via][d][a] = min(house[via-1][d][a], (house[via-1][d][via] + house[via-1][via][a]))

for _ in range(q) :
    c, s, e = map(int, input(). split())
    if house[c-1][s][e] == float('inf') :
        print(-1)
    else :
        print(house[c-1][s][e])