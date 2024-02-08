import copy
n = int(input())
k = int(input())
boardd = [list(map(int, input(). strip(). split())) for _ in range(n)] 
shot = list(map(int, input(). strip(). split()))
lst = []
seq = []
d = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def ChooseLane(cnt) :
    global lst, seq
    if cnt >= k :
        seq.append(lst.copy())
        return 
    for i in range(n) :
        lst.append(i)
        ChooseLane(cnt+1)
        lst.pop()
        
for i in range(n) :
    for j in range(n) :
        if boardd[i][j] > 9 :
            boardd[i][j] = [boardd[i][j], 0]
        else :
            if boardd[i][j] > 0 :
                boardd[i][j] = [boardd[i][j], boardd[i][j]]
            else :
                boardd[i][j] = [0, 0]

ChooseLane(0)
ans = 0
for laneseq in seq :
    score = 0
    shotindex = 0
    board = copy.deepcopy(boardd)
    for lane in laneseq :
        for col in range(n) :
            if board[lane][col][0] == 0 :     # 빈 칸일때 총알이 맞지않고 다음 열로 지나감
                continue
            else :    # 표적이 있는 칸인 경우
                if board[lane][col][0] >= 10 :    # 보너스 표적인 경우
                    score += board[lane][col][0]
                    board[lane][col] = [0, 0]
                    break
                else :
                    if board[lane][col][1] <= shot[shotindex] :     # 막타 쳤을 때
                        score += board[lane][col][0]
                        spread = board[lane][col][0] // 4   # 사방으로 퍼질 표적의 체력
                        board[lane][col] = [0, 0]    # 사라진 표적은 0
                        if spread == 0 :
                            break
                        for i in range(4) :
                            if 0 <= lane + d[i][0] < n and 0 <= col + d[i][1] < n :
                                dr = lane + d[i][0]
                                dc = col + d[i][1]
                                if board[dr][dc] == [0, 0] :   # 사방을 탐색하고 표적이 없는 곳에 표적이 퍼진다
                                    board[dr][dc] = [spread, spread]  # 퍼진 표적의 초기체력과 현재체력 표시
                        break
                    else :    # 막타를 치지 못한 경우
                        board[lane][col][1] -= shot[shotindex]
                        break
        shotindex += 1
    ans = max(ans, score)
    
print(ans)




        






