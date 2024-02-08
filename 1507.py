import sys
input = sys.stdin.readline

n = int(input())
adjmtrx = [[0]*(n+1)]      # 간선들의 정보를 저장할 인접행렬
chkmtrx = [[1]*(n+1) for _ in range(n+1)]   # 가중치를 제외한 연결유무만을 저장하는 체크용 행렬
                                            # 초기에는 모든 도로가 이어져 있다고 가정 
ans = 0   

for _ in range(n) :
    adjmtrx.append([0] + list(map(int, input(). split())))

# 역 플로이드 워셜 알고리즘
# 이미 입력으로 주어지는 것 자체가 다이렉트 경로의 최단시간 정보(플로이드 워셜을 한번 돌린상태라 생각)이다
# 다이렉트 경로가 경유경로보다 소요시간이 작은 경우만 남겨야 한다
for k in range(1, n+1) :
    for i in range(1, n+1) :
        for j in range(1, n+1) :
            if i == j or i == k or j == k :    # 제자리로 돌아오는 간선은 제외
                continue
            else :
                # 만약 경유지를 통해 다이렉트 도로와 동일한 시간에 도착 지점에 도달할 수 있다면, 도착지점까지의 다이렉트 도로가 있는 것은 낭비이다
                if adjmtrx[i][j] == adjmtrx[i][k] + adjmtrx[k][j] :
                    # 따라서 체크용 행렬에서 낭비인 도로를 삭제한다
                    chkmtrx[i][j] = 0

                    # 만약 다이렉트 도로가 다른 지점을 경유해서 가는 도로보다 시간이 오래 걸리면,
                    # 플로이드 워셜이 이미 시행된 입력정보와 모순이다 
                elif adjmtrx[i][j] > adjmtrx[i][k] + adjmtrx[k][j] :
                    ans = -1


if ans != -1 :
    for i in range(1, n+1) :
        for j in range(i, n+1) :
            if chkmtrx[i][j] == 1 :
                ans += adjmtrx[i][j]

print(ans)