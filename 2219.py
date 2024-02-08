import sys
input = sys.stdin.readline

n, m = map(int, input(). split())
adjmtrx = [[2*10e6]*(n+1) for _ in range(n+1)]   # 통신시간을 저장할 인접행렬 생성

for _ in range(m) :
    a, b, c = map(int, input(). split())   # 양방향 통신
    adjmtrx[a][b] = c
    adjmtrx[b][a] = c

for k in range(1, n+1) :
    for i in range(1, n+1) :
        for j in range(1, n+1) :
            # 직접통신보다 간접통신이 빠른 경우 최소통신시간으로 초기화
            if adjmtrx[i][j] > adjmtrx[i][k] + adjmtrx[k][j] :   
                adjmtrx[i][j] = adjmtrx[i][k] + adjmtrx[k][j]

min_t = 2*10e6  # 최소시간을 저장할 변수
ans = 0       # 최소시간안에 다른 컴터들과 통신할 수 있는 컴퓨터의 번호를 저장할 변수

for i in range(1, n+1) :
    time = 0    # 각 컴퓨터에 대해 다른 컴터들과의 통신시간을 계산한다
    for j in range(1, n+1) :
        if i != j :     # 자기자신과 통신하는 경우 제외
            time += adjmtrx[i][j]    # 통신시간을 더해나간다
    if time < min_t :    # 기존의 최소시간보다 적은 시간이 걸릴경우
        min_t = time     # 최소시간을 재설정하고
        ans = i          # 해당 최소시간을 가진 컴터의 번호를 정답변수에 저장한다

print(ans)