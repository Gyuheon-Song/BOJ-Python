import math

def CenterOfMass(x1, y1, x2, y2, x3, y3) :
    xcom = (x1 + x2 + x3) / 3
    ycom = (y1 + y2 + y3) / 3
    return [xcom, ycom]

def SizeOfTri(x1, y1, x2, y2, x3, y3) :   # 외적으로 구하기
    v1x = x2 - x1
    v2x = x3 - x1
    v1y = y2 - y1
    v2y = y3 - y1
    size = 0.5 * abs(v1x * v2y - v1y * v2x)
    return size


x1, y1, x2, y2, x3, y3 = map(int, input(). split())
ansx = 2 * math.pi * CenterOfMass(x1, y1, x2, y2, x3, y3)[1] * SizeOfTri(x1, y1, x2, y2, x3, y3)
ansy = 2 * math.pi * CenterOfMass(x1, y1, x2, y2, x3, y3)[0] * SizeOfTri(x1, y1, x2, y2, x3, y3)
print(ansx, ansy)