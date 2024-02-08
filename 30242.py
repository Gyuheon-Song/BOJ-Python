n = int(input())

Q = [*map(int, input(). split())]   # 이미 위치한 퀸들의 좌표를 입력받기(인덱스가 행-1, 원소가 열-1)
slash = [False] * (2 * n - 1)  # 우상향 대각선 (좌상방 꼭짓점부터 인덱스 0)
bslash = [False] * (2 * n - 1)  # 좌상향 대각선 (우상방 꼭짓점부터 인덱스 0)
column = [False] * n           # 열

def FindQueen(column, slash, bslash, L, r) :   # 열과 대각선리스트들, 퀸의 위치리스트, 행번호를 매개변수로 한다

    if r == len(L) :   # 탐색한 행의 번호가 위치시킨 퀸의 개수와 같을 때 (모든 행에 대하여 퀸을 위치시켰을 때)
        print(*L)   # 퀸의 위치리스트를 출력하고
        return True  # 참값반환
    
    elif L[r] != 0 :   # 어떤 행에 이미 퀸이 놓아져 있는 경우
        return FindQueen(column, slash, bslash, L, r+1) # 다음 행을 탐색하자
    
    else :
        for c in range(len(L)) :   # 해당 행에서의 각 열에 대해 퀸을 놓을 수 있는지 판단
            if not column[c] and not slash[c+r] and not bslash[c-r] :   # 해당 열과 그 행,열번호를 지나는 각 대각선들에 대해 퀸을 놓을 수 있다면
                column[c] = slash[c+r] = bslash[c-r] = True # 퀸을 놓고
                L[r] = c+1  # 퀸의 위치리스트에서 행을 인덱스로 하는 위치에, 열번호인 (c+1)을 저장
                if FindQueen(column, slash, bslash, L, r+1) :   # 다음 행에 퀸을 놓을 수 있는 경우의 수가 있을 때
                    return True   # 참값 반환
                # 다음 행에 퀸을 놓을 수 없다면
                L[r] = 0  # 해당 행에는 퀸이 없음을 표시
                column[c] = slash[c+r] = bslash[c-r] = False  # 해당 열과 각 대각선에 대해 퀸을 놓여있지 않음을 표시하고
        return False   # 거짓값을 반환    

for row in range(n) :
    if Q[row] != 0 :    # 만약 어떤 행에 이미 퀸이 위치해있다면
        col = Q[row] - 1  # 해당 인덱스의 원소-1이 열의 번호이다
        column[col] = slash[row+col] = bslash[col-row] = True   # 같은 열과 대각선들에 대해 퀸을 놓을 수 없다는 표시를 해준다

if not FindQueen(column, slash, bslash, Q, 0) :  # 만약 모든 행에 대해 퀸을 놓을 수 없다면 n개의 퀸을 놓지 못했음으로
    print(-1)   # -1 
    # 모든 행에 퀸을 위치시킨 경우에는 함수 내에서 참값에 걸려 퀸의 리스트가 출력될 것이다
