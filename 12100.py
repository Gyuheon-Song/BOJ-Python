import copy
n = int(input())
board = [list(map(int, input(). split())) for _ in range(n)]
ans = 0


def move_Left() :    # 왼쪽으로 쓸어넘기기
    global board, n
    combined = [[False]*n for _ in range(n)]   # 합쳐진 적이 있는지 여부
    for r in range(n) :
        for c in range(n) :
            voidc = False     # 한 열에서의 빈 공간의 열번호를 저장
            if board[r][c] == 0 :   # 빈공간인 경우 건너뛰어 탐색
                continue
            for t in range(c-1, -1, -1) :    # 숫자가 있는 칸인 경우 자기로부터 왼쪽으로 탐색
                if board[r][t] == 0 :    # 왼쪽으로 탐색해가며 빈공간인 경우
                    if t == 0 :    # 만약 왼쪽 끝 칸까지 탐색되어 0으로 나타난 경우
                        board[r][t] = board[r][c]   # 원래 칸의 수를 해당 칸에 이동시키고
                        board[r][c] = 0   # 원래 칸은 빈공간 표시
                        break
                    voidc = t   # 그 빈공간의 열번호를 빈공간변수에 저장해놓고 다음 탐색
                    continue
                else :   # 왼쪽으로 탐색해나가며 숫자를 만난 경우
                    if board[r][t] == board[r][c] :    # 원래 칸과 같은 값인 경우
                        if not combined[r][t] :   # 만약 합쳐진 적이 없는 칸인 경우에 해당 칸에 합치고
                            board[r][t] *= 2
                            combined[r][t] = True   # 합쳐진 적 있음 표시
                            board[r][c] = 0    # 합쳐버린 원래 칸은 빈공간 표시
                            break
                        else : # 만약 합쳐진 적이 있는 칸이라면
                            board[r][voidc] = board[r][c]    # 합치는 것이 아닌 이전까지 저장해놓은 가장 왼쪽의 빈공간에 원래 칸의 값 이동시키기
                            board[r][c] = 0    # 원래 칸은 빈공간 표시
                            break
                    else :    # 왼쪽으로 탐색해나가다가 원래 칸과 다른 값을 만난 경우
                        if voidc :   # 빈공간이 있었던 경우 
                            board[r][voidc] = board[r][c]   # 이전까지 저장해놓은 빈 공간이 가장 왼쪽의 빈 공간이므로 그 공간에 수를 밀어서 옮겨놓고
                            board[r][c] = 0   # 원래 칸은 빈공간표시
                            break
                        else :    # 왼쪽에 값이 있지만 그 값이 다르고 현재 칸과 탐색한 칸 사이에 빈공간이 없는 경우 그대로 두고 탐색 중지
                            break

def move_Right() :   # 오른쪽으로 쓸어넘기기
    global board, n
    combined = [[False]*n for _ in range(n)]
    for r in range(n) :
        for c in range(n-1, -1, -1) :  # 각 행의 오른쪽 끝 칸부터 탐색
            voidc = False     # 한 열에서의 빈 공간의 열번호를 저장
            if board[r][c] == 0 :   # 빈공간인 경우 건너뛰어 탐색
                continue
            for t in range(c+1, n) :    # 숫자가 있는 칸인 경우 자기로부터 오른쪽으로 탐색
                if board[r][t] == 0 :    # 왼쪽으로 탐색해가며 빈공간인 경우
                    if t == n-1 :    # 만약 오른쪽 끝 칸까지 탐색되어 0으로 나타난 경우
                        board[r][t] = board[r][c]   # 원래 칸의 수를 해당 칸에 이동시키고
                        board[r][c] = 0   # 원래 칸은 빈공간 표시
                        break
                    voidc = t   # 그 빈공간의 열번호를 빈공간변수에 저장해놓고 다음 탐색
                    continue
                else :   # 오른쪽으로 탐색해나가며 숫자를 만난 경우
                    if board[r][t] == board[r][c] :    # 원래 칸과 같은 값인 경우
                        if not combined[r][t] : # 만약 합쳐진 적이 없는 칸인 경우에
                            board[r][t] *= 2   # 해당 칸에 합치고
                            combined[r][t] = True  # 합쳐진 적 있음 표시
                            board[r][c] = 0    # 합쳐버린 원래 칸은 빈공간 표시
                            break
                        else :   # 만약 합쳐진 적이 있는 칸이라면
                            board[r][voidc] = board[r][c]   # 이전까지 저장해 놓은 가장 오른쪽의 빈 공간에 원래 칸의 수를 이동시키기
                            board[r][c] = 0   # 원래 칸은 빈공간으로 표시
                            break
                    else :    # 오른쪽으로 탐색해나가다가 원래 칸과 다른 값을 만난 경우
                        if voidc : # 빈 공간이 있었던 경우
                            board[r][voidc] = board[r][c]   # 이전까지 저장해놓은 빈 공간이 가장 오른쪽의 빈 공간이므로 그 공간에 수를 밀어서 옮겨놓고
                            board[r][c] = 0   # 원래 칸은 빈공간표시
                            break
                        else :    # 오른쪽에 값이 있지만 그 값이 다르고 현재 칸과 탐색한 칸 사이에 빈공간이 없는 경우 그대로 두고 탐색 중지
                            break

def move_Up() :   # 위쪽으로 쓸어넘기기
    global board, n
    combined = [[False]*n for _ in range(n)]
    for c in range(n) :
        for r in range(n) :  # 각 열의 위쪽 끝 칸부터 탐색
            voidr = False     # 한 열에서의 빈 공간의 열번호를 저장
            if board[r][c] == 0 :   # 빈공간인 경우 건너뛰어 탐색
                continue
            for t in range(r-1, -1, -1) :    # 숫자가 있는 칸인 경우 자기로부터 위쪽으로 탐색
                if board[t][c] == 0 :    # 위쪽으로 탐색해가며 빈공간인 경우
                    if t == 0 :    # 만약 위쪽 끝 칸까지 탐색되어 0으로 나타난 경우
                        board[t][c] = board[r][c]   # 원래 칸의 수를 해당 칸에 이동시키고
                        board[r][c] = 0   # 원래 칸은 빈공간 표시
                        break
                    voidr = t   # 그 빈공간의 행번호를 빈공간변수에 저장해놓고 다음 탐색
                    continue
                else :   # 위쪽으로 탐색해나가며 숫자를 만난 경우
                    if board[t][c] == board[r][c] :    # 원래 칸과 같은 값인 경우
                        if not combined[t][c] :   # 만약 합쳐진 적이 없는 칸인 경우
                            board[t][c] *= 2    # 해당 칸에 합치고
                            combined[t][c] = True  # 합쳐진 적 있음 표시
                            board[r][c] = 0    # 합쳐버린 원래 칸은 빈공간 표시
                            break
                        else :  # 만약 합쳐진 적이 있는 칸인 경우
                            board[voidr][c] = board[r][c]   # 이전까지 저장해놓은 가장 위쪽의 빈공간에 원래 칸의 수를 이동시킨다
                            board[r][c] = 0   # 원래 칸은 빈공간 표시
                            break
                    else :    # 위쪽으로 탐색해나가다가 원래 칸과 다른 값을 만난 경우
                        if voidr :  # 빈공간이 있었던 경우 
                            board[voidr][c] = board[r][c]   # 이전까지 저장해놓은 빈 공간이 가장 위쪽의 빈 공간이므로 그 공간에 수를 밀어서 옮겨놓고
                            board[r][c] = 0   # 원래 칸은 빈공간표시
                            break
                        else :   # 위쪽에 값이 있지만 그 값이 다르고 현재 칸과 탐색한 칸 사이에 빈공간이 없는 경우 그대로 두고 탐색 중지
                            break

def move_Down() :
    global board, n
    combined = [[False]*n for _ in range(n)]
    for c in range(n) :
        for r in range(n-1, -1, -1) :  # 각 열의 아래쪽 끝 칸부터 탐색
            voidr = False     # 한 열에서의 빈 공간의 열번호를 저장
            if board[r][c] == 0 :   # 빈공간인 경우 건너뛰어 탐색
                continue
            for t in range(r+1, n) :    # 숫자가 있는 칸인 경우 자기로부터 아래쪽으로 탐색
                if board[t][c] == 0 :    # 아래쪽으로 탐색해가며 빈공간인 경우
                    if t == n-1 :    # 만약 아래쪽 끝 칸까지 탐색되어 0으로 나타난 경우
                        board[t][c] = board[r][c]   # 원래 칸의 수를 해당 칸에 이동시키고
                        board[r][c] = 0   # 원래 칸은 빈공간 표시
                        break
                    voidr = t   # 그 빈공간의 행번호를 빈공간변수에 저장해놓고 다음 탐색
                    continue
                else :   # 아래쪽으로 탐색해나가며 숫자를 만난 경우
                    if board[t][c] == board[r][c] :    # 원래 칸과 같은 값인 경우
                        if not combined[t][c] :    # 만약 합쳐진 적이 없는 칸인 경우
                            board[t][c] *= 2   # 해당 칸에 합치고
                            combined[t][c] = True   # 합쳐진 적 있음 표시
                            board[r][c] = 0    # 합쳐버린 원래 칸은 빈공간 표시
                            break
                        else :    # 만약 합쳐진 적이 있는 칸인 경우
                            board[voidr][c] = board[r][c]    # 이전까지 저장해 놓은 가장 아래쪽의 빈 공간에 원래 칸의 수를 이동시키기
                            board[r][c] = 0   # 원래 칸은 빈공간 표시
                            break
                    else :    # 아래쪽으로 탐색해나가다가 원래 칸과 다른 값을 만난 경우
                        if voidr : # 빈공간이 있었던 경우
                            board[voidr][c] = board[r][c]   # 이전까지 저장해놓은 빈 공간이 가장 아래쪽의 빈 공간이므로 그 공간에 수를 밀어서 옮겨놓고
                            board[r][c] = 0   # 원래 칸은 빈공간표시
                            break
                        else :     # 위쪽에 값이 있지만 그 값이 다르고 현재 칸과 탐색한 칸 사이에 빈공간이 없는 경우 그대로 두고 탐색 중지
                            break

def fiveMoves(movecnt) :
    global board, n, ans
    if movecnt == 5 :
        for i in range(n) :
            for j in range(n) :
                ans = max(ans, board[i][j])
        return

    latestBoard = copy.deepcopy(board)

    move_Left()
    fiveMoves(movecnt+1)

    board = copy.deepcopy(latestBoard)

    move_Right()
    fiveMoves(movecnt+1)

    board = copy.deepcopy(latestBoard)

    move_Up()
    fiveMoves(movecnt+1)

    board = copy.deepcopy(latestBoard)

    move_Down()
    fiveMoves(movecnt+1)

    board = copy.deepcopy(latestBoard)

    return

  
fiveMoves(0)
print(ans)