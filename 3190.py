import sys
from collections import deque
input = sys.stdin.readline

n = int(input())   # 보드의 크기
k = int(input())    # 사과의 개수
apple = [list(map(int, input(). split())) for _ in range(k)]   # 사과의 위치좌표를 저장
l = int(input())   # 뱀의 방향전환 정보
d_change = [0]*(10001)   # 초를 인덱스로 가지는 방향을 담은 리스트

for i in range(l) :   
    t, turn = map(str, input(). split())
    d_change[int(t)] = turn

# 북, 동, 남, 서 를 방향인덱스로 표현할 것이다(시계방향)
dr = [-1, 0, 1, 0]   
dc = [0, 1, 0, -1]

direction = 1  # 초기방향은 동쪽
time = 0   # 시간
snake = deque([(1, 1)])   # 처음 뱀의 좌표를 넣은 뱀의 몸좌표리스트

while True :
    time += 1   # 1초 경과
    cr, cc = snake[-1]  # 뱀의 머리좌표
    # 진행방향으로 한칸 머리이동
    nr = cr + dr[direction]
    nc = cc + dc[direction]

    # 벽에 닿거나 뱀 몸에 부딪힌 경우 종료
    if 1 <= nr <= n and 1 <= nc <= n and (nr, nc) not in snake :
        snake.append((nr, nc))  # 이동한 뱀의 머리위치를 저장

        if [nr, nc] in apple :  # 이동한 위치에 사과가 있다면
            apple.remove([nr, nc])   # 사과리스트에서 사과를 빼준다
        else :  # 이동한 위치에 사과가 없다면
            snake.popleft()    # 꼬리부분 제거
        
        if d_change[time] == 'D' :   # 우회전
            direction = (direction+1) % 4
        elif d_change[time] == 'L' :   # 좌회전
            direction = (direction+3) % 4

    else :
        break

print(time)