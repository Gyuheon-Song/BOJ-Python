n = int(input())
lst = []
for _ in range(n) :
    lst.append(int(input()))

lst.sort(reverse = True)
ans = 0

for i in range(n) :
    if (i+1) % 3 == 0 :
        continue
    else :
        ans += lst[i]

print(ans)