import sys
from collections import deque
input = sys.stdin.readline

num = input().rstrip()
cnt = 0
ans = deque()
count = [0]*(10)

for i in range(len(num)) :
    cnt += int(num[i])
    count[int(num[i])] += 1

if cnt % 3 != 0 or count[0] == 0:
    print(-1)

else :
    for i in range(10) :
        while count[i] > 0 :
            ans.appendleft(str(i))
            count[i] -= 1
    print(*ans, sep = "")

