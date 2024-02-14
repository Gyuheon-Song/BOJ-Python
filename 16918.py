r, c, n = map(int, input(). split())

board = [list(input()) for _ in range(r)]
t_planted = [[-10]*c for _ in range(r)]
d = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def plant_Bomb(board, curtime) :   # 폭탄 설치
    for i in range(r) :
        for j in range(c) :
            if board[i][j] == '.' :    # 폭탄이 설치되어 있지 않은 경우 폭탄설치
                board[i][j] = 'O'
                t_planted[i][j] = curtime    # 폭탄을 설치한 시간 기록

def Explode(board) :    # 폭발해야할 폭탄들 폭발
    global curt
    for i in range(r) :
        for j in range(c) :
            if t_planted[i][j] == curt-3 :    # 만약 폭탄 설치 시간이 현재시간에서 3초 전인 경우
                board[i][j] = '.'   # 폭발시키고
                t_planted[i][j] = -10   # 폭탄설치시간 초기화
                for k in range(4) :   # 인접한 칸에 대해
                    dr = i + d[k][0]
                    dc = j + d[k][1]
                    # 격자판 내의 범위에서 인접한 폭탄들이 지금 폭발해야하는 폭탄이 아닌 경우에만 폭발(연쇄작용 배제)
                    if 0 <= dr < r and 0 <= dc < c and t_planted[dr][dc] != curt-3:
                        board[dr][dc] = '.'
                        t_planted[dr][dc] = -10

for i in range(r) :
    for j in range(c) :
        if board[i][j] == 'O' :
            t_planted[i][j] = 0   # 초기 폭탄 설치된 시간 기록

curt = 2   # 처음 1초는 아무것도 하지 않고 1초뒤에는 폭탄을 설치하므로 현재시각 2부터 시작

if n < curt :
    for rows in board :
        print(''.join(rows))
        
else :  
    while (True) :  # 정해진 시간까지 반복
        plant_Bomb(board, curt)   # 폭탄 설치
        curt += 1   # 시간증가
        if curt > n :
            break
        Explode(board)   # 폭발시키기
        curt += 1
        if curt > n :
            break
    
    for rows in board :
        print(''.join(rows))
