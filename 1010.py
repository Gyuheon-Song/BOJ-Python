import math
n = int(input())

for i in range(n) :
    w, e = map(int, input(). split())
    bridge = math.factorial(e)//(math.factorial(w)*math.factorial(e-w))
    print(bridge)