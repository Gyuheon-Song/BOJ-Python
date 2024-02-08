from collections import deque
dq = deque()
n = int(input())
for i in range(n) :
    dq.append(i+1)

if n == 1 :
    print(*dq)

else :
    while len(dq) > 2 :
        dq.popleft()
        dq.append(dq.popleft())
    dq.popleft()
    print(*dq)
