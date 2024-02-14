
import sys
input = sys.stdin.readline
n, m, q = map(int, input(). split())
land = [[0]*m for _ in range(n)]
cnt = n*m

def Mow(y, x, dy, dx) :
    global land, cnt     
    while True :
        if land[y][x] :
            return
        else :
            land[y][x] = 1
            cnt -= 1
            ny = y + dy
            nx = x + dx
            if 0 <= ny < n and 0 <= nx < m :
                y = ny
                x = nx
            else :
                return

for _ in range(q) :
    cmd = input().rstrip()
    if cmd[0] == '1' :
        q, dy, dx, y, x = map(int, cmd.split())
        Mow(y-1, x-1, dy, dx)
    elif cmd[0] == '2' :
        q, y, x = map(int, cmd.split())
        print(land[y-1][x-1])
    else :
        print(cnt)