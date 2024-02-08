import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input(). split()))
Q = deque()
ans = [0]*n

for i in range(n) :
    while Q and lst[Q[-1]] < lst[i] :
        ans[Q.pop()] = lst[i]    
    Q.append(i)

while Q :
    ans[Q.pop()] = -1

print(*ans)
