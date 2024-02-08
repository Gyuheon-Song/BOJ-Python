h, w = map(int, input(). split())
pict = [list(input()) for _ in range(h)]
ans = 0
dot = 0
for i in range(h) :
    tmp = 0
    flag = False
    for j in range(w) :
        if pict[i][j] == '/' or pict[i][j] == '\\' :
            if not flag :
                flag = True
                tmp += 1
            else :
                flag = False
                tmp += 1
        elif pict[i][j] == '.' :
            if not flag :
                continue
            else :
                dot += 1
    ans += tmp

print(ans//2 + dot)
