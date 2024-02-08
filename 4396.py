n = int(input())
mine = [list(input()) for _ in range(n)]
opened = [list(input()) for _ in range(n)]
ans = [['.']*n for _ in range(n)]

d = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
flag = True

for i in range(n) :
    for j in range(n) :
        if opened[i][j] == 'x' :
            if mine[i][j] == '*' :
                flag = False
            cnt = 0
            for k in range(8) :
                if 0 <= i+d[k][0] < n and 0 <= j+d[k][1] < n :
                    dr = i + d[k][0]
                    dc = j + d[k][1]
                    if mine[dr][dc] == '*' :
                        cnt += 1
            ans[i][j] = str(cnt)

if not flag :
    for i in range(n) :
        for j in range(n) :
            if mine[i][j] == '*' :
                ans[i][j] = '*'
    for item in ans :
        print(''.join(item))
else :
    for item in ans :
        print(''.join(item))
            
