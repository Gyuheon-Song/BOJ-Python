import sys
input = sys.stdin.readline

n, m = map(int, input(). split())
adjmtrx = [[sys.maxsize]*(n+1) for _ in range(n+1)]


for _ in range(m) :
    a, b = map(int, input(). split())
    adjmtrx[a][b] = 1    # 양방향 이동시간 1로 초기화
    adjmtrx[b][a] = 1

for i in range(1, n+1) :
    adjmtrx[i][i] = 0

# 플로이드 워셜 알고리즘 
for k in range(1, n+1) :
    for i in range(1, n+1) :
        for j in range(1, n+1) :
            adjmtrx[i][j] = min(adjmtrx[i][j], adjmtrx[i][k] + adjmtrx[k][j])

time = sys.maxsize
ans = []

# 어떤 두 건물을 임의로 지정
for i in range(1, n) :
    for j in range(i+1, n+1) :
        t = 0    # 두 건물에 대해 다른건물들로부터의 이동시간의 총합을 구하자
        for k in range(1, n+1) :
            # 한 건물과 두 치킨집과의 거리 중 작은 값을 이동시간에 더한다
            t += min(adjmtrx[k][i], adjmtrx[k][j])
            # 만약 그 시간이 앞서 구했던 시간들보다 적다면
        if t < time :
            time = t     # 최소시간으로 저장하고
            ans = [i, j, 2*time]    # 정답리스트에 두 치킨집의 위치와, 다른 건물들까지의 왕복시간의 총합을 저장한다 

print(*ans)