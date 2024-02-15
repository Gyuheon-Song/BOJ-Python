import sys
input = sys.stdin.readline

n = int(input().strip())
q12 = dict()
q34 = dict()

INF = 1e7

class dot :
    def __init__(self, gradient, quadrant) :
        self.gradient = gradient
        self.quadrant = quadrant

for _ in range(n) :
    x, y = map(int, input(). strip(). split())
    if y >= 0 :
        q = 12
        if x == 0 :
            g = INF
        else :
            g = y / x
    else :
        q = 34
        if x == 0 :
            g = INF
        else :
            g = y / x
    
    balloon = dot(g, q)
    if balloon.quadrant == 12 :
        if balloon.gradient not in q12.keys() :
            q12[balloon.gradient] = 1
        else :
            q12[balloon.gradient] += 1
    else :
        if balloon.gradient not in q34.keys() :
            q34[balloon.gradient] = 1
        else :
            q34[balloon.gradient] += 1

if q12 and q34 :
    max12 = max(q12.values())
    max34 = max(q34.values())
    ans = max(max12, max34)
else :
    if q12 :
        ans = max(q12.values())
    else :
        ans = max(q34.values())

print(ans)

        




