t = int(input())
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for _ in range(t) :
    cmd = list(input())
    turtle = [0, 0]
    dir = minx = maxx = miny = maxy = 0
    for i in range(len(cmd)) :
        if cmd[i] == 'F' :
            turtle[0] += d[dir][0]
            turtle[1] += d[dir][1]
            minx = min(minx, turtle[0])
            maxx = max(maxx, turtle[0])
            miny = min(miny, turtle[1])
            maxy = max(maxy, turtle[1])
        elif cmd[i] == 'B' :
            turtle[0] -= d[dir][0]
            turtle[1] -= d[dir][1]
            minx = min(minx, turtle[0])
            maxx = max(maxx, turtle[0])
            miny = min(miny, turtle[1])
            maxy = max(maxy, turtle[1])
        elif cmd[i] == 'L' :
            dir = (dir+1)%4
        elif cmd[i] == 'R' :
            dir = (dir+3)%4
    print((maxx-minx)*(maxy-miny))

    