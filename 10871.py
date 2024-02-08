result = []
n, x = map(int, input() .split())
a = list(map(int,input().split()))
for i in range (0,n) : 
    if a[i]<x :
        result.append(a[i])
print(*result)


