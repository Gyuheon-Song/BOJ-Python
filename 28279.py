import sys
from collections import deque
dq = deque()
n = int(sys.stdin.readline())
for i in range(n) :
    com = sys.stdin.readline().split()
    if com[0] == "1" :
        dq.appendleft(int(com[1]))
    elif com[0] == "2" :
        dq.append(int(com[1]))
    elif com[0] == "3" :
        if len(dq) == 0 :
            print(-1)
        else :
            print(dq.popleft())
    elif com[0] == "4" :
        if len(dq) == 0 :
            print(-1)
        else :
            print(dq.pop())
    elif com[0] == "5" :
        print(len(dq))
    elif com[0] == "6" :
        if len(dq) == 0 :
            print(1)
        else :
            print(0)
    elif com[0] == "7" :
        if len(dq) == 0 :
            print(-1)
        else :
            print(dq[0])
    elif com[0] == "8" :
        if len(dq) == 0 :
            print(-1)
        else :
            print(dq[-1])
