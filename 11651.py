import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n) :
    x, y = map(int, input(). split())
    lst.append([y, x])
lst.sort()
for i in range(len(lst)) :
    lst[i] = lst[i][::-1]
for item in lst :
    print(*item)
