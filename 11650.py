import sys
input = sys.stdin.readline
n = int(input())
lst = []
for i in range(n) :
    k ,v = map(int, input(). split())
    lst.append([k, v])
lst.sort()
for item in lst :
    print(*item)
