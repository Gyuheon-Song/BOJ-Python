m, n = map(int, input(). split())
spiral = [[False]*m for _ in range(n)]
dir = 0
d = [[0, 1], [-1, 0], [0, -1], [1, 0]]

pos = [n-1, 0]
spiral[pos[0]][pos[1]] = True

for i in range(n*m-1) :
    if pos[0] + d[dir][0] < 0 or pos[0] + d[dir][0] > n-1 or pos[1] + d[dir][1] < 0 or pos[1] + d[dir][1] > m-1 or spiral[pos[0] + d[dir][0]][pos[1] + d[dir][1]] == True:
        dir = (dir+1)%4
        pos[0] += d[dir][0]
        pos[1] += d[dir][1]
        spiral[pos[0]][pos[1]] = True
        continue
    else :
        pos[0] += d[dir][0]
        pos[1] += d[dir][1]
        spiral[pos[0]][pos[1]] = True

print(pos[1], n-1-pos[0])

