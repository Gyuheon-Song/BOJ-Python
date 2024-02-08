n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort()
ans = 0

for i in range(n) :
    ans = max(ans, lst[i]*(n-i))

print(ans)