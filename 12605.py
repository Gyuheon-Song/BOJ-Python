from collections import deque

n = int(input())

for i in range(n) :
    lst = []
    s = deque(map(str, input(). split()))
    k = len(s)
    while s :
        lst.append(s.pop())
        ans = " ".join(lst)
    print(f"Case #{i+1}: {ans}")