n = int(input())
lst = []

for _ in range(n) :
    lst.append(int(input()))

lst.sort()
ans = 0
for i in range(len(lst)-2) :
    if lst[i] + lst[i+1] > lst[i+2] :
        ans = max(ans, lst[i] + lst[i+1] + lst[i+2])

print(ans) if ans else print(-1)