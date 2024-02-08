import sys
input = sys.stdin.readline

n, m = map(int, input(). split())
adjmtrx = [[0]*(n+1) for _ in range(n+1)]
cnt = 0

for _ in range(m) :
    short, tall = map(int, input(). split())
    adjmtrx[short][tall] = 1

# 플로이드 워셜 알고리즘
for k in range(1, n+1) :
    for i in range(1, n+1) :
        for j in range(1, n+1) :
            # 만약 나보다 더 큰 사람까지의 비교할 수 있는 경로가 있거나 더 큰 사람까지의 비교절차를 경유해서 알 수 있다면
            if adjmtrx[i][j] == 1 or (adjmtrx[i][k] == 1 and adjmtrx[k][j] == 1) :
                adjmtrx[i][j] = 1  # 그 사람이 나보다 크다는 것을 알 수 있다

for i in range(1, n+1) :
    know = 0   # 키를 아는 사람의 수를 0으로 초기화
    for j in range(1, n+1) :
        know += (adjmtrx[i][j] + adjmtrx[j][i])    # 나보다 키가 크다는 것을 비교를 통해 알 수 있는 사람과, 역방향인 나보다 키가 작다는 것을 비교하여 알 수 있는 사람의 수
    if know == n-1 :  # 비교를 통해 키를 알 수 있는 사람의 수가 본인을 제외한 n-1명이라면,
        cnt += 1 # 그 사람은 자신의 키가 n명 중에 몇번째인지를 알 수 있다

print(cnt)

