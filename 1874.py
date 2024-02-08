from collections import deque

n = int(input())
nums = []
lst = deque()
rst = []

for _ in range(n) :
    lst.append(int(input()))

for i in range(1, n+1) :
    nums.append(i)
    rst.append("+")
    while nums and nums[-1] == lst[0] :
        nums.pop()
        lst.popleft()
        rst.append("-")    

if lst :
    print("NO")
else :
    for item in rst :
        print(item)