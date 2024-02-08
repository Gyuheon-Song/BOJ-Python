import sys
input = sys.stdin.readline

n, k = map(int, input(). split())
adjmtrx = [[0]*(n+1) for _ in range(n+1)]

for _ in range(k) :
    a, b = map(int, input(). split())    # 사건의 전후순서를 가중치 1로 표현한다
    adjmtrx[a][b] = 1

# 플로이드 워셜 알고리즘
for k in range(1, n+1) :
    for i in range(1, n+1) :
        for j in range(1, n+1) :
            # 만약 다른 사건을 통해 비교가 가능하면 해당 비교과정의
            # 가중치의 합은 2일 것이므로 이때 두 사건은 서로 전후관계라는 1로 표기한다
            if adjmtrx[i][k] + adjmtrx[k][j] == 2 :    
                adjmtrx[i][j] = 1

s = int(input())

for _ in range(s) :
    temp1, temp2 = map(int, input(). split())   # 어떠한 두 사건을 입력받는다
    if adjmtrx[temp1][temp2] == 1 :   # 두사건의 전후관계가 성립함을 나타내는 1일때
        print(-1)   
    elif adjmtrx[temp2][temp1] == 1 :    # 두 사건의 전후관계는 성립하지 않지만 사건의 역의 전후관계가 성립할 때
        print(1)
    else :          # 전후관계를 알 수 없을 때
        print(0)
