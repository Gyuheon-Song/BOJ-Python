import sys
input = sys.stdin.readline
n, l = map(int, input().strip(). split())

lst = list(map(int, input().strip(). split()))
lst.sort()

for i in range(len(lst)) :
    if l >= lst[i] :
        l += 1

print(l)