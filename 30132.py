t = int(input())
d = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
for _ in range(t) :
    n, m = map(int, input(). split())
    mine = [list(input()) for _ in range(n)]
    flag = True
    for i in range(n) :
        for j in range(m) :
            if mine[i][j] == 'F' :
                mine_guaranteed = False
                for l in range(8) :
                    if 0 <= i+d[l][0] < n and 0 <= j+d[l][1] < m :
                        ddr = i + d[l][0]
                        ddc = j + d[l][1]
                        if mine[ddr][ddc] != 'F' :
                            mine_guaranteed |= True
                if not mine_guaranteed :
                    flag = False    
            else :
                cnt = 0
                for k in range(8) :
                    if 0 <= i+d[k][0] < n and 0 <= j+d[k][1] < m :
                        dr = i + d[k][0]
                        dc = j + d[k][1]
                        if mine[dr][dc] == 'F' :
                            cnt += 1
                if str(cnt) != mine[i][j] :
                    flag = False      

    print("Well done Clark!") if flag else print("Please sweep the mine again!")