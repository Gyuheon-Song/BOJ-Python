from collections import deque
n, k = map(int, input(). split())

number = list(input())
cnt = 0
for i in range(n) :
    number[i] = int(number[i])

number = deque(number)
anslst = deque([])

for i in range(n) :
    if anslst :
        if cnt < k :
            while anslst and anslst[-1] < number[i] :
                if cnt >= k or not anslst:
                    break
                anslst.pop()
                cnt += 1
            anslst.append(number[i])
        else :
            anslst.append(number[i])
    else :
        anslst.append(number[i])

for i in range(k-cnt) :
    anslst.pop()

print(*anslst, sep = '')
    

