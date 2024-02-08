from collections import deque
import sys
input = sys.stdin.readline
Q = deque()
n = int(input())
for _ in range(n) :
    com = list(input(). split())
    l = len(Q)
    if com[0] == "push" :
        Q.append(int(com[1]))
    elif com[0] == "front" :
        if l != 0 :
            print(Q[0])
        else :
            print(-1)
    elif com[0] == "back" :
        if l != 0 :
            print(Q[-1])
        else :
            print(-1)
    elif com[0] == "size" :
        print(len(Q))
    elif com[0] == "empty" :
        if l != 0 :
            print(0)
        else :
            print(1)
    elif com[0] == "pop" :
        if l != 0 :
            print(Q.popleft())
        else :
            print(-1)