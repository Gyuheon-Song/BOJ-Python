n = int(input())
x = []
y = []
ans = 0
for _ in range(n) :
    a, b = map(int, input(). split())
    x.append(a)
    y.append(b)

x.sort()
y.sort()
k = n//2

for i in range(n) :
    ans += (abs(x[i]-x[k]) + abs(y[i]-y[k]))

print(ans)