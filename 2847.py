n = int(input())
lst = []
for _ in range(n) :
    lst.append(int(input()))
lst = lst[::-1]
ans = 0
for i in range(n-1) :
    while lst[i] <= lst[i+1] :
        lst[i+1] -= 1
        ans += 1

print(ans)