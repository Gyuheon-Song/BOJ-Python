from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
Q = deque()
for _ in range(n) :
    com = list(input(). split())
    l = len(Q)
    if com[0] == "push_front" :
        Q.appendleft(int(com[1]))
    elif com[0] == "push_back" :
        Q.append(int(com[1]))
    elif com[0] == "pop_front" :
        if l != 0 :
            print(Q.popleft())
        else :
            print(-1)
    elif com[0] == "pop_back" :
        if l != 0 :
            print(Q.pop())
        else :
            print(-1)
    elif com[0] == "size" :
        print(l)
    elif com[0] == "empty" :
        if l != 0 :
            print(0)
        else :
            print(1)
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