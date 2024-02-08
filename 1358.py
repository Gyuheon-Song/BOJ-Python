import math
w, h, x, y, p = map(int, input(). split())
r = h//2
cnt = 0

def Distance(xcenter, ycenter, m, n) :
    return math.sqrt((xcenter-m)**2 + (ycenter-n)**2)

for _ in range(p) :
    xi, yi = map(int, input(). split())
    if xi < x-r or yi > y+h :
        continue
    else :
        if xi < x :
            if Distance(x, y+r, xi, yi) <= r :
                cnt += 1
        elif xi > x+w :
            if Distance(x+w, y+r, xi, yi) <= r :
                cnt += 1
        else :
            if y <= yi <= y+h :
                cnt += 1
print(cnt)
        