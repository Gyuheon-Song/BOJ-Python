
def Row_chk(r, num) :   # 행 체크
    for x in range(9) :
        if sudoku[r][x] == num :
            return False
    return True

def Col_chk(c, num) :  # 열 체크
    for x in range(9) :
        if sudoku[x][c] == num :
            return False
    return True

def Sqr_chk(r, c, num) :   # 사각형 체크
    nr = (r//3)*3    # 재귀분할과 동일한 좌표설정
    nc = (c//3)*3
    for i in range(3) :    
        for j in range(3) :
            if sudoku[nr+i][nc+j] == num :
                return False
    return True
    
def DFS(depth) :   # DFS 탐색
    
    if depth >= len(void) :   # 만약 빈칸의 개수를 다 채웠을 때
        for k in range(9) :   # 출력
            print("".join(map(str, sudoku[k])))
        exit()
    
    row, col = void[depth]    # 빈칸의 좌표

    for m in range(1, 10) :   # 빈칸에 숫자를 넣어보자
        if Row_chk(row, m) and Col_chk(col, m) and Sqr_chk(row, col, m) :   # 넣을 수 있는지 체크
            sudoku[row][col] = m   # 숫자를 넣고
            DFS(depth+1)    # depth증가
            sudoku[row][col] = 0  # 백트래킹

void = []
sudoku = []

for i in range(9) :
    tmp = list(map(int, input()))
    for j in range(len(tmp)) :
        if tmp[j] == 0 :
            void.append((i, j))    # 빈칸의 좌표를 넣자
    sudoku.append(tmp)

DFS(0)


