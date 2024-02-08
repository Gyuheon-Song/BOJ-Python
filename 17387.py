import sys
input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input(). split())
x3, y3, x4, y4 = map(int, input(). split())

def CCW(a1, b1, a2, b2, a3, b3) :
    ccw = a1*b2 + a2*b3 + a3*b1 - a2*b1 - a3*b2 - a1*b3    
    if ccw > 0 :
        return 1
    elif ccw < 0 :
        return -1 
    else :
        return 0

ans = 0


if CCW(x1, y1, x2, y2, x3, y3) * CCW(x1, y1, x2, y2, x4, y4) == 0 and CCW(x3, y3, x4, y4, x1, y1) * CCW(x3, y3, x4, y4, x2, y2 ) == 0 :
    if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2) :
        ans = 1
if CCW(x1, y1, x2, y2, x3, y3) * CCW(x1, y1, x2, y2, x4, y4) <= 0 and CCW(x3, y3, x4, y4, x1, y1) * CCW(x3, y3, x4, y4, x2, y2 ) <= 0 :
    if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2) :
        ans = 1
    
print(ans)

