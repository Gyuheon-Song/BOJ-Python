n = int(input())

rowlst = [0]*n    # 인덱스를 행으로 하고 몇열에 배치할지 저장하는 리스트
cnt = 0         # 총 가짓수

def position(x) :    # 퀸을 놓을 수 있는 곳인지 판단하는 함수(행을 매개변수로 받는다)
    for i in range(x) :  # 같은열의 위치이거나, 대각선의 위치이면 False 반환
        if rowlst[x] == rowlst[i] or abs(rowlst[x]-rowlst[i]) == abs(x-i) :
            return False
    return True

def Queen(row) :   # 퀸을 놓는 함수
    global cnt
    if row == n :    # n개의 행에 걸쳐서 다 위치시켰을 때 가짓수++
        cnt += 1
        return
    else :    # 아직 모든 행에 대해서 배치하지 못했을 때
        for i in range(n) :  # n개의 열에 대해서 놓아보기 시도
            rowlst[row] = i   # row행의 i열에 놓아보고
            if position(row) :   # 만약 해당 자리에 위치시켜도 될 때
                Queen(row+1)     # 위치시킨 후 다음 행으로 넘어간다

Queen(0)
print(cnt)


