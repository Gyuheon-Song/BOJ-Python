import sys
input = sys.stdin.readline

n, t = map(int, input(). split())   # 도시의 수와 텔포시간
city = [0]     # 도시의 특별함과 좌표정보를 담을 리스트 생성
adjmtrx = [[2001] * (n+1) for _ in range(n+1)]    # 도시간 이동시간의 정보를 담을 인접행렬을 최대시간인 2000시간보다 크게 초기화

for _ in range(n) :
    city.append(list(map(int, input(). split())))    # 도시정보를 리스트로 매핑하여 도시리스트에 저장

# 인접행렬에 경유지없이 각 도시간 이동시간 정보(양방향)를 넣는다
for i in range(1, n+1) :
    for j in range(1, n+1) :
        if city[i][0] == 0 or city[j][0] == 0 :   # 두 도시중 하나라도 특별한 도시가 아니면
            # 좌표를 통해 계산한 시간이 걸리게 된다
            adjmtrx[i][j] = abs(city[i][1]-city[j][1]) + abs(city[i][2]-city[j][2])
            adjmtrx[j][i] = abs(city[i][1]-city[j][1]) + abs(city[i][2]-city[j][2])
        else :     # 두 도시 모두 측별한 도시라면
            # 텔포시간, 기존에 구해놓았던 이동시간, 좌표를 통해 구한 이동시간 중 가장 최소시간이 이동시간이 된다
            adjmtrx[i][j] = min(t, abs(city[i][1]-city[j][1]) + abs(city[i][2]-city[j][2]))
            adjmtrx[j][i] = min(t, abs(city[i][1]-city[j][1]) + abs(city[i][2]-city[j][2]))

# 플로이드 워셜 알고리즘
for k in range(1, n+1) :
    for i in range(1, n+1) :
        for j in range(1, n+1) :
            if adjmtrx[i][j] > adjmtrx[i][k]+adjmtrx[k][j] :
                adjmtrx[i][j] = adjmtrx[i][k]+adjmtrx[k][j]

m = int(input())

for _ in range(m) :
    a, b = map(int, input(). split())
    print(adjmtrx[a][b])