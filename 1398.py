import sys
input = sys.stdin.readline

n, m = map(int, input(). split())
adjmtrx = [[sys.maxsize] * (n+1) for _ in range(n+1)]
temp = sys.maxsize  # 베이컨수를 저장할 변수
ans = 0         # 베이컨 수가 가장 작은 사람을 저장할 정답변수

for i in range(1, n+1) :
    adjmtrx[i][i] = 0        # 자기 스스로 친구일 순 없기에 0으로 초기화

for _ in range(m) :
    a, b = map(int, input(). split())
    adjmtrx[a][b] = 1           # 서로 친구인 경우 양방향 간선으로 간주하고 가중치를 1로 초기화
    adjmtrx[b][a] = 1

# 플로이드 워셜 알고리즘
for k in range(1, n+1) :
    for i in range(1, n+1) :
        for j in range(1, n+1) :
            adjmtrx[i][j] = min(adjmtrx[i][j], adjmtrx[i][k]+adjmtrx[k][j])

for i in range(1, n+1) :    # 각 사람에 대해 케빈베이컨 수를 구하자
    kev_num = 0   # 케빈 베이컨 수를 0에서 시작
    for j in range(1, n+1) :   # 다른사람들과 몇사람 건너 아는지 탐색하고
        kev_num += adjmtrx[i][j]   # 케빈베이컨 수에 단계수를 더해나간다
    if kev_num < temp :       # 만약 앞전에 구했던 최소 케빈베이컨의 수보다 작을 경우
        temp = kev_num      # 방금 구한 케빈 베이컨의 수를 최소 베이컨수로 초기화하고
        ans = i         # 이러한 최소 베이컨 수를 나타낸 사람의 정보를 초기화한다

print(ans)
