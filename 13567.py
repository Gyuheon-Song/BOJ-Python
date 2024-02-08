m, n = map(int, input(). split())
dir = 0
d = [[0, 1], [-1, 0], [0, -1], [1, 0]]
robot = [m, 0]
flag = True

for _ in range(n) :
    cmd = list(map(str, input(). split()))
    if cmd[0] == "TURN" :
        if int(cmd[1]) == 0 :
            dir = (dir+1)%4
        else :
            dir = (dir+3)%4
    else:
        for _ in range(int(cmd[1])) :
            robot[0] += d[dir][0]
            robot[1] += d[dir][1]
    if robot[0] > m or robot[0] < 0 or robot[1] > m or robot[1] < 0 :
        flag = False

print(robot[1], m-robot[0]) if flag else print(-1)