import sys
input = sys.stdin.readline

item = [0]   # 지역의 아이템 개수를 저장할 리스트
n, m, r = map(int, input(). split())
ans = 0  # 예은이가 얻을 수 있는 최대 아이템 개수를 저장할 정답변수

adjmtrx = [[sys.maxsize] * (n+1) for _ in range(n+1)]     # 간선의 정보를 저장할 인접행렬
item += list(map(int, input(). split()))    # 지역의 아이템 개수 정보를 리스트에 입력받는다 

for _ in range(r) :
    a, b, c = map(int, input(). split())
    adjmtrx[a][b] = c      # 양방향 간선
    adjmtrx[b][a] = c

# 플로이드 워셜 알고리즘
for k in range(1, n+1) :
    for i in range(1, n+1) :
        for j in range(1, n+1) :
            if j == i :
                adjmtrx[i][j] = 0       # 처음 낙하지점의 경우 탐색을 위해 소모해야하는 가중치가 0이다
            else :
                adjmtrx[i][j] = min(adjmtrx[i][j], adjmtrx[i][k]+adjmtrx[k][j])

for i in range(1, n+1) :
    item_num = 0     # 낙하지점별로 획득할 수 있는 아이템을 따로 계산해야 하므로 매 낙하지점마다 아이템개수 0으로 초기화
    for j in range(1, n+1) :
        if adjmtrx[i][j] <= m :     # 가고자 하는 지역까지의 가중치가 주어진 탐색범위 이내일때
            item_num += item[j]     # 해당지역의 아이템 개수를 아이템 개수변수에 더해준다
    ans = max(ans, item_num)        # 지역별 탐색마다 최대값을 정답에 최신화한다

print(ans)

