from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input(). split())
ladder = []
snake = []
Q = deque()
chk = [False] * 101

for _ in range(n) :
    ladder.append(list(map(int, input(). split())))

for _ in range(m) :
    snake.append(list(map(int, input(). split())))

def BFS() :
    global L
    Q.append(1)
    chk[1] = True
    L = 1

    while Q :
        k = len(Q)
        for l in range(k) :
            now = Q.popleft()
            for dice in range(1, 7) :
                after = now + dice
                if after == 100 :
                    return
                elif after < 100 and chk[after] == False :
                    for i in range(len(ladder)) :
                        if after == ladder[i][0] :
                            after = ladder[i][1]
                    for j in range(len(snake)) :
                        if after == snake[j][0] :
                            after = snake[j][1]
                    Q.append(after)
                    chk[after] = True          
        L += 1

BFS()

print(L)