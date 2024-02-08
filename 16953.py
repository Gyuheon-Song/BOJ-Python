from collections import deque
a, b = map(int, input(). split())
Q = deque()

Q.append(a)
cnt = 1
flag = False

while Q :
    for i in range(len(Q)) :
        tmp = Q.popleft()
        for num in [tmp*2, tmp*10 + 1] :
            if num == b :
                flag = True
                print(cnt+1)
                exit()
            elif num < b :
                Q.append(num)
    cnt += 1

print(cnt) if flag else print(-1)
