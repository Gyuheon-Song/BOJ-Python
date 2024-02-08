n = int(input())
lst = []
for _ in range(n) :
    lst.append(list(map(int, input(). split())))

lst.sort(key = lambda x: x[0])
ans = 0
for i in range(n) :
    ans += ((i+1)*lst[i][0] + lst[i][1])

print(ans)