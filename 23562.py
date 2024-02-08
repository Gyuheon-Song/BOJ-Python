import sys
input = sys.stdin.readline
n, m = map(int, input(). split())
a, b = map(int, input(). split())

board = [input().strip() for _ in range(n)]
k = min(n, m)

def Shape(i, p, q) :       # ㄷ모양 생성 함수
    global chk
    chk = [[False]*(m) for _ in range(n)]
    for j in range(i) :
        for l in range(i) :
            if j < i//3 or j >= 2*(i//3):
                chk[p+j][q+l] = True
            else :
                if l < i//3 :
                    chk[p+j][q+l] = True

ans = 400001
for i in range(3, k+1, 3) :    # 한 변의 길이가 3의 배수인 ㄷ자 모양 생성
    for p in range(n-i+1) :
        for q in range(m-i+1) :
            Shape(i, p, q)            
            cost = 0
            for x in range(n) :
                for y in range(m) :
                    if chk[x][y] :     # ㄷ모양에 포함되는 칸이면
                        if board[x][y] == '#' :    # #이어야 한다
                            continue
                        else :      #    #이 아닌 경우 색칠하는 비용 ++
                            cost += a
                    else :     # ㄷ모양에 포함되지 않는 칸이면
                        if board[x][y] == '.' :     # .이어야 한다
                            continue
                        else :    #    .이 아닌 경우 지우는 비용 ++
                            cost += b
            ans = min(ans, cost)
print(ans)

            






