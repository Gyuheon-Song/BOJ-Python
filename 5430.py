import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for i in range(t):
    command = input().rstrip()
    n = int(input())
    lst = input().rstrip()[1:-1].split(",")
    q = deque(lst)

    rev, front, back = 0, 0, len(q)-1
    flag = False
    if n == 0:
        q = []
        front = 0
        back = 0

    for com in command:
        if com == 'R':
            rev += 1
        elif com == 'D':
            if len(q) < 1:
                flag = True
                print("error")
                break
            else:
                if rev % 2 == 0:
                    q.popleft()
                else:
                    q.pop()
    if not flag:
        if rev % 2 == 0:
            print("[" + ",".join(q) + "]")
        else:
            q.reverse()
            print("[" + ",".join(q) + "]")