def Star(n,row,col) :
    if n == 3 :           # n이 3일때 가장 기본단위규칙의 별찍기
        result[row][col] = "*"
        result[row+1][col-1] = result[row+1][col+1] = "*"
        for i in range(-2, 3) :
            result[row+2][col+i] = "*"
    else :
        Star(n//2, row, col)   #가장 기본단위의 별찍는 최소크기인 3이 아닌 경우 윗 꼭짓점은 고정
        Star(n//2, row+n//2, col-n//2)   # 왼쪽 아래 꼭짓점의 위치부터 별찍기함수 재귀호출
        Star(n//2, row+n//2, col+n//2)   # 오른쪽 아래 꼭짓점의 위치부터 별찍기함수 재귀호출


n = int(input())
result = [[" "]*(2*n-1) for _ in range(n)]
Star(n, 0, n-1)   # n을 입력받았을때 가장 위의 꼭짓점의 별이 찍히는 위치
for k in result :
    print("".join(k))
