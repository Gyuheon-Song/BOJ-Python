import sys
input = sys.stdin.readline

n, m, r = map(int, input(). split())
matrix = [list(map(int, input(). strip(). split())) for _ in range(n)]

for _ in range(r) :    # r번 왼쪽으로 돌리기
    for i in range(min(n, m)//2) :    # 껍질별로 돌려주기
        
        tmp = matrix[i][m-i-1]    # 각 껍질의 오른쪽 위 꼭짓점이 첫 원소

        for j in range(m-i-2, i-1, -1) :     # 윗모서리 좌로밀기
            element = matrix[i][j]
            matrix[i][j] = tmp
            tmp = element

        # tmp에 왼쪽 위 꼭짓점 값이 저장되어 있는 상태
        
        for j in range(i+1, n-i) :     # 좌모서리 아래로 밀기
            element = matrix[j][i]
            matrix[j][i] = tmp
            tmp = element

        # tmp에 왼쪽 아래 꼭짓점 값이 저장되어 있는 상태
            
        for j in range(i+1, m-i) :     # 아랫 모서리 우측으로 밀기
            element = matrix[n-i-1][j]
            matrix[n-i-1][j] = tmp
            tmp = element

        # tmp에 오른쪽 아래 꼭짓점 값이 저장되어 있는 상태
            
        for j in range(n-i-2, i-1, -1) :         # 우 모서리 위로 밀기
            element = matrix[j][m-i-1]
            matrix[j][m-i-1] = tmp
            tmp = element
        
        # tmp 에 오른쪽 위 꼭짓점 저장되어 있는 상태

for row in matrix :
    print(*row)

