# 플로이드 워셜 알고리즘
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
adjmtrx = [[sys.maxsize] * (n+1) for _ in range(n+1)]    # 인접 행렬 만들기

for _ in range(m) :
    a, b, c = map(int, input(). split())   # 노선정보를 입력받는다
    if adjmtrx[a][b] > c :     # 가중치가 이미 전에 받았던 노선의 가중치보다 작을때
        adjmtrx[a][b] = c      # 노선의 가중치를 작은 값으로 초기화해준다

for i in range(n+1) :      # 출발지와 도착지가 같은 노선의 거리(혹은 비용)는 0으로 초기화한다
    adjmtrx[i][i] = 0

for stopover in range(1, n+1) :   # 각 지점들을 경유지로 설정
    for depart in range(1, n+1) :  # 출발점
        for arrive in range(1, n+1) :  # 도착점
            # 기존의 가중치와, 어떤 한 경유지를 경유하여 도착점까지 가는 가중치 중 더 작은 값으로 초기화
            adjmtrx[depart][arrive] = min(adjmtrx[depart][arrive], adjmtrx[depart][stopover] + adjmtrx[stopover][arrive])

for i in range(1, n+1) :
    for j in range(1, n+1) :
        if adjmtrx[i][j] == sys.maxsize :
            print(0, end = " ")
        else :
            print(adjmtrx[i][j], end = " ")
    print("")
            
            
