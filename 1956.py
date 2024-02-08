import sys
input = sys.stdin.readline

v, e = map(int, input(). split())   # 노드와 간선의 정보
adjmtrx = [[sys.maxsize]*(v+1) for _ in range(v+1)]  # 인접행렬
ans = sys.maxsize   # 정답변수 초기화

for _ in range(e) :
    a, b, c = map(int, input(). split())
    adjmtrx[a][b] = c   # 인접행렬에 간선의 가중치 초기화

# 플로이드 워셜 알고리즘 실행(도착지까지의 가중치와, 경유지를 경유해서 가는 가중치 중 최솟값으로 초기화)
for k in range(1, v+1) :
    for i in range(1, v+1) :
        for j in range(1, v+1) :
            adjmtrx[i][j] = min(adjmtrx[i][j], adjmtrx[i][k] + adjmtrx[k][j])

for i in range(1, v+1) :  # 만들어놓은 최소가중치 인접행렬에서 제자리로 돌아오는 경로의 최솟값들 중 최솟값이 정답
    ans = min(ans, adjmtrx[i][i])

if ans != sys.maxsize :
    print(ans)
else :
    print(-1)