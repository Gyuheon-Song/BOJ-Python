knight = [input() for _ in range(5)]

d = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]
cnt = 0
flag = True

for i in range(5) :
    for j in range(5) :
        if knight[i][j] == 'k' :
            cnt += 1
            for k in range(8) :
                if i+d[k][0] < 0 or i+d[k][0] > 4 or j+d[k][1] <0 or j+d[k][1] > 4 :
                    continue
                elif knight[i+d[k][0]][j+d[k][1]] == 'k' :
                    flag = False

print("valid") if cnt == 9 and flag else print("invalid")
