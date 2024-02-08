import sys
input = sys.stdin.readline

n = int(input())
adjmtrx = []
for _ in range(n) :
    adjmtrx.append(list(map(int, input(). split())))

for k in range(n) :
    for i in range(n) :
        for j in range(n) :
            # 어떤 경유지를 경유하여 i부터 j까지 갈 수 있는 경우에 해당 경로를
            # 담고있는 인접행렬의 값을 1로 초기화
            if (adjmtrx[i][k] == 1 and adjmtrx[k][j] == 1) :  
                adjmtrx[i][j] = 1

for i in range(n) :
    print(*adjmtrx[i])
