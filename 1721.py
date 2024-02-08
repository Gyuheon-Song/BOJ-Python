import sys
import copy
from collections import deque
input = sys.stdin.readline
cubelst = []

n = int(input())
for _ in range(n**2) :
    cubelst.append(list(map(int, input(). strip(). split())))

uppercube = [[[0]*5 for _ in range(n)] for _ in range(n)]
rotation = [[0]*n for _ in range(n)]
visited = [False]*(n**2)
d = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def Facechk(lst, rcnt) :    # 큐브를 시계방향으로 회전시키면서 북쪽 면의 수를 인덱스 0으로 하는 리스트를 반환하는 함수
    Q = deque(lst)
    for _ in range(rcnt) :
        Q.appendleft(Q.popleft())    # 0번 인덱스에는 항상 큐브에서 북쪽 방향을 향해 있는 면의 수가 온다
    return list(Q)

def LocateCube(row, col) :    # 상자를 원하는 위치에 배치하는 함수
    global cubelst, uppercube, rotation, visited, n

    if row >= n or col >= n :   # 만약 탐색이 종료되어 조건에 맞는 큐브상태일때 출력하고 끝
        for i in range(n) :
            for j in range(n) :
                print(uppercube[i][j][0], end = ' ')
            print("")
        for item in rotation :
            print(*item)
        for i in range(n) :
            for j in range(n) :
                print(uppercube[i][j], end = ' ')
            print("")
        exit(1)
        return
    
    for i in range(n**2) :    # 모든 큐브들에 대해서 조건에 맞게 놓아보기
        if visited[i] :  # 배치하고자 하는 큐브가 사용한 큐브인 경우 다음 큐브로 건너뛴다
            continue
        # 가장자리에 위치해 있을때 가장자리를 향한 면의 수는 0이어야 한다
        for turn in range(4) :     # 배치하려고 하는 큐브를 집어 회전시키면서 4면의 수 확인하고 해당 공간에 배치 불가한 위상인 경우 회전을 더 시켜보며 확인
            cubephase = Facechk(copy.deepcopy(cubelst[i][1:]), turn)
            if row == 0 :   # 북쪽 가장자리 위치에 큐브를 놓고자 할 때
                if cubephase[0] != 0 :   # 선택한 큐브의 북쪽 면의 수가 0이 아닌 경우 건너뛴다
                    continue
            if col == 0 :     # 서쪽 가장자리 위치에 큐브를 놓고자 할 때
                if cubephase[3] != 0 :    # 선택한 큐브의 서쪽 면의 수가 0이 아닌 경우 건너뛴다
                    continue
            if row == n-1 :    # 남쪽 가장자리 위치에 큐브를 놓고자 할 때
                if cubephase[2] != 0 :   # 선택한 큐브의 남쪽 면의 수가 0이 아닌 경우 건너뛴다
                    continue
            if col == n-1 :    # 동쪽 가장자리 위치에 큐브를 놓고자 할 때
                if cubephase[1] != 0 :   # 선택한 큐브의 동쪽 면의 수가 0이 아닌 경우 건너뛴다
                    continue
            chk = True   # 가장자리 체크 완료 표지

            for dir in range(4) :    # 가장자리 체크가 끝난 후 4개의 면에 대해 
                dr = row + d[dir][0]
                dc = col + d[dir][1]
                if 0 <= dr < n and 0 <= dc < n :
                    if uppercube[dr][dc][0] != 0 :     # 만약 현재 큐브의 네 방면상 어느 곳에 큐브가 존재한다면
                        if dir == 0 :   # 북쪽에 다른 큐브가 맞닿아 있다면
                            if uppercube[dr][dc][3] != cubephase[0] : # 내가 집은 큐브의 현재 위상의 북쪽 면과 인접한 큐브의 남쪽 면의 숫자가 일치하지 않으면
                                chk = False   # 해당 자리에서 틀린 배치 혹은 위상이므로 False 표지
                                break   # 해당 큐브 놓기 중단
                        if dir == 1 : # 동쪽에 다른 큐브가 맞닿아 있다면
                            if uppercube[dr][dc][4] != cubephase[1] :  # 내가 집은 큐브의 현재 위상의 동쪽 면과 인접한 큐브의 서쪽 면의 숫자가 일치하지 않으면
                                chk = False  # 불가한 배치이므로 False 표지
                                break  # 해당 큐브 놓기 중단
                        if dir == 2 : # 남쪽에 다른 큐브가 맞닿아 있다면
                            if uppercube[dr][dc][1] != cubephase[2] :  # 내가 집은 큐브의 현재 위상의 남쪽 면과 인접한 큐브의 북쪽 면의 숫자가 일치하지 않으면
                                chk = False  # 불가한 배치이므로 False 표지
                                break  # 해당 큐브 놓기 중단
                        if dir == 3 :  # 서쪽에 다른 큐브가 맞닿아 있다면
                            if uppercube[dr][dc][2] != cubephase[3] :  # 내가 집은 큐브의 현재 위상의 서쪽 면과 인접한 큐브의 동쪽 면의 숫자가 일치하지 않으면
                                chk = False # 불가한 배치이므로 False 표지
                                break  # 해당 큐브 놓기 중단
            
            if chk :   # 만약 모든 조건을 만족하면 해당 위치에 큐브를 배치
                visited[i] = True  # 사용한 큐브임을 표지
                uppercube[row][col] = [cubelst[i][0]] + cubephase  # 윗면의 숫자와 나머지 사방면의 숫자를 시계방향 순서로 하는 리스트를 저장
                rotation[row][col] = turn   # 방금 배치한 큐브의 시계방향 회전수를 저장

                if col == n-1 :    # 한 열의 배치가 완료되었다면
                    LocateCube(row+1, 0)   # 다음 행의 0번 열에서 부터 계속 배치
                elif col < n-1 :    # 아직 한 열의 배치가 다 끝나지 않았다면
                    LocateCube(row, col+1)   # 해당 행의 다음 열에 큐브 배치
                
                # 배치하다가 불가한 경우 방금 위치에 대한 큐브의 정보 모두 초기화 (백트래킹)
                uppercube[row][col] = [0]*5  
                rotation[row][col] = 0
                visited[i] = False

LocateCube(0, 0)


# import sys
# input = sys.stdin.readline
# data = []
# n = int(input())
# nn = n ** 2

# for _ in range(nn):
#     line = list(map(int, input().split()))
#     data.append(line)

# from collections import deque

# def calc(d, count):
#     q = deque(d)
#     for _ in range(count):
#         x = q.pop()
#         q.appendleft(x)
#     return list(q)

# answer = [[0] * n for _ in range(n)]

# answer_top = [[[0] * 5 for _ in range(n)] for _ in range(n)]
# visited = [0] * nn
# dx = [0, 1, -1, 0]
# dy = [1, 0, 0, -1]

# from copy import deepcopy

# def func(pos_x, pos_y):
#     global data, visited, answer, answer_top, n, nn
    
#     #만약 끝까지 탐색이 끝났다면 결과 출력하고 종료
#     if pos_x >= n or pos_y >= n:
#         for h in range(n):
#             for w in range(n):
#                 print(answer_top[h][w][0], end = ' ')
#             print()
#         for h in range(n):
#             for w in range(n):
#                 print(answer[h][w], end = ' ')
#             print()
#         for i in range(n) :
#             for j in range(n) :
#                 print(answer_top[i][j], end = ' ')
#             print("")

#         exit()
#         return
    
#     #입력으로 받은 모든 상자퍼즐들을 확인한다
#     for i in range(nn):
# 		#만약 이미 사용한 상자라면 건너뛴다.
#         if visited[i] == 1:
#             continue

#         #일단 가장자리인지 확인하고 가장자리 값이 0이 아니라면 건너뛴다.
#         for j in range(4):
#             cube = calc(deepcopy(data[i][1:]), j)
#             if pos_x == 0:
#                 if cube[0] != 0:
#                     continue
#             if pos_y == 0:
#                 if cube[3] != 0:
#                     continue
#             if pos_x == n-1:
#                 if cube[2] != 0:
#                     continue
#             if pos_y == n-1:
#                 if cube[1] != 0:
#                     continue
# 			#가장자리 값이 모두 0이라면 이제 인접면의 수를 체크한다.
#             check = False
#             for e in range(4):
#                 nx = pos_x + dx[e]
#                 ny = pos_y + dy[e]
#                 if 0 <= nx < n and 0 <= ny < n:
#                 	#인접면의 값이 존재한다면 내가 현재 두려고 하는 상자와의 값이 일치한지 확인
#                    	#만약 일치하지 않는다면 check = True하고 break
#                     if answer_top[nx][ny][0] != 0:
#                         if e == 0:
#                             if answer_top[nx][ny][4] != cube[1]:
#                                 check = True
#                                 break
#                         if e == 1:
#                             if answer_top[nx][ny][1] != cube[2]:
#                                 check = True
#                                 break
#                         if e == 2:
#                             if answer_top[nx][ny][3] != cube[0]:
#                                 check = True
#                                 break
#                         if e == 3:
#                             if answer_top[nx][ny][2] != cube[3]:
#                                 check = True
#                                 break
#             #모두 일치한다면 해당 좌표에 상자를 위치시키고 다음 좌표로 넘어간다.
#             if not check:
#                 visited[i] = 1
#                 answer_top[pos_x][pos_y] = [data[i][0]] + cube
#                 answer[pos_x][pos_y] = j

#                 if pos_y == n-1:
#                     func(pos_x + 1, 0)
#                 elif pos_y < n-1:
#                     func(pos_x, pos_y + 1)
#                 #만약 최종 결과를 찾을 수 없다면 초기화하고 다음 상자가 올 수 있도록 준비
#                 answer_top[pos_x][pos_y] = [0] * 5
#                 answer[pos_x][pos_y] = 0
#                 visited[i] = 0

# func(0, 0)
    