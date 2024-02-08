import sys
input = sys.stdin.readline
n = int(input())

def SqrDistance(a, b) :
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

def Pythagoras(p, q, r) :
    if SqrDistance(p, q) + SqrDistance(q, r) == SqrDistance(p, r) or SqrDistance(p, q) + SqrDistance(p, r) == SqrDistance(q, r) or SqrDistance(q, r) + SqrDistance(p, r) == SqrDistance(p, q) :
        return True
    return False

dot = []
for _ in range(n) :
    dot.append(list(map(int, input(). strip(). split())))

cnt = 0
for i in range(n-2) :
    for j in range(i+1, n-1) :
        for k in range(j+1, n) :
            if Pythagoras(dot[i], dot[j], dot[k]) :
                cnt += 1

print(cnt)