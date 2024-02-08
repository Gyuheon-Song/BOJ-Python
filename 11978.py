n = int(input())
farm = [[0]*100]
dirdict = {'N' : 0, 'E' : 1, 'S' : 2, 'W' : 3}
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
route = [[0, 0, 0]]
pos = [0, 0, 0]
time = 0

for _ in range(n) :
    cmd, t = map(str, input(). split())
    for i in range(1, int(t)+1) :
        pos[0] += dir[dirdict[cmd]][0]
        pos[1] += dir[dirdict[cmd]][1]
        time += 1
        route.append([pos[0], pos[1], time])

l = len(route)
x = 1001
flag = False

for i in range(l-1) :
    for j in range(i+1, l) :
        if route[i][0] == route[j][0] and route[i][1] == route[j][1] :
            flag = True
            x = min(x, route[j][2]-route[i][2])

print(x) if flag else print(-1)


