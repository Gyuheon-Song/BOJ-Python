import sys
input = sys.stdin.readline
import math

d, n, h = map(int, input(). split())

k = math.ceil((h-d)/(d-n)) + 1
print(k)