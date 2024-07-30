import sys
input = sys.stdin.readline

n = int(input())  # 미지수의 개수

# 행렬 입력받기 (n x (n + 1) 크기)
init_mat = [list(map(int, input().split())) for _ in range(n)]  
ans = [0] * n  # x1~xn까지의 정답배열

# 가장 앞의 계수가 0이 아닌 순으로 행 정렬 (기본 행 연산)
sorting_indexlst = []

for i in range(n):
    for j in range(n + 1): 
        if init_mat[i][j] != 0:
            sorting_indexlst.append([j, i])
            break

sorting_indexlst.sort()
mat = []   

for item in sorting_indexlst:    # 계수가 0이 아닌 가장 앞의 항이 존재하는 방정식부터 계수행렬을 정렬
    mat.append(init_mat[item[1]])

# 가우스 소거법
for i in range(n - 1): 
    if mat[i][i] != 0:  # 현재 행의 주대각선 계수가 0이 아닐 때
        for k in range(i + 1, n):  # 다음 행부터
            if mat[k][i] != 0:  # 0이 아닐 경우에만
                coef = mat[k][i] / mat[i][i]
                for j in range(i, n + 1):
                    mat[k][j] -= mat[i][j] * coef

# xn 구하기
ans[n - 1] = mat[n - 1][n] / mat[n - 1][n - 1]

# Xn부터 x1까지 거슬러 올라가며 해를 구한다
for r in range(n - 2, -1, -1):
    tmp = mat[r][n]
    for c in range(r + 1, n):
        tmp -= ans[c] * mat[r][c]
    
    if mat[r][r] == 0:  # 주대각선 계수가 0인 경우
        ans[r] = 0  # 해가 존재하지 않을 수 있음
    else:
        ans[r] = tmp / mat[r][r]

for num in ans:
    print("{:.0f}".format(num), end=" ")