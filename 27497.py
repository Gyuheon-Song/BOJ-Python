from collections import deque
n = int(input())
lst = deque()
latest = []
for _ in range(n):
    com = list(map(str, input(). split()))
    
    if com[0] == "1" :
        lst.append(com[1])
        latest.append(com[0])
    elif com[0] == "2" :
        lst.appendleft(com[1])
        latest.append(com[0])
    elif com[0] == "3" and len(latest) > 0 :
        if latest[-1] == "1" :
            lst.pop()
            latest.pop()
        elif latest[-1] == "2" :
            lst.popleft()
            latest.pop()

print("".join(lst)) if len(lst) != 0 else print(0)

        