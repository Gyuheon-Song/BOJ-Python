from collections import deque
Q = deque()
n, k = map(int, input(). split())
lst = []
Q = deque(i for i in range(1, n+1))

while Q :
    Q.rotate(-(k-1))
    lst.append(Q.popleft())

ans = "<"+", ".join(map(str, lst))+">"
print(ans)