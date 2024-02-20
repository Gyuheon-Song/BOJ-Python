import math
r = float(input())

euclidS = math.pi * math.pow(r, 2)
nonEuclidS = math.pow(2*r, 2) / 2

print("%.6f" % euclidS)
print("%.6f" % nonEuclidS)