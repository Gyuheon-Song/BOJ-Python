n = int(input())

lst = []
for _ in range(n) :
    lst.append(int(input()))

lst.sort()
ans = 0
for i in range(n) :
    ans += abs(i+1-lst[i])
print(ans)