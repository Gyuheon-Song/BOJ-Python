import sys
input = sys.stdin.readline
n, m = map(int, input(). split())
lst = list(map(int, input(). split()))

for i in range(n-1) :
    lst[i+1] += lst[i]

for _ in range(m) :
    a, b = map(int, input(). split())
    if a == 1 :
        print(lst[b-1])
    else :
        print(lst[b-1]-lst[a-2])
