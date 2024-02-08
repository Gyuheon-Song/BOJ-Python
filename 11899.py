from collections import deque
import sys
input = sys.stdin.readline
s = input()
dq = deque()
cnt = 0
for i in s :
    if i == "(" :
        dq.append(i)
    elif i == ")" :
        if dq :
            dq.pop()
        else :
            cnt += 1
if dq :
    cnt += len(dq)
    print(cnt)
else :
    print(cnt)