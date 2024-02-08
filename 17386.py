import sys
input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input(). split())
x3, y3, x4, y4 = map(int, input(). split())

def CCW(a1, b1, a2, b2, a3, b3) :
    return a1*b2 + a2*b3 + a3*b1 - a2*b1 - a3*b2 - a1*b3    

if CCW(x1, y1, x2, y2, x3, y3) * CCW(x1, y1, x2, y2, x4, y4) < 0 and CCW(x3, y3, x4, y4, x1, y1) * CCW(x3, y3, x4, y4, x2, y2) < 0 :
    print(1)
else :
    print(0)
