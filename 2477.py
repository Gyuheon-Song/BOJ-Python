n = int(input())
arr = [[0, 0] for _ in range(7)]
d = [[1, 0], [-1, 0], [0, -1], [0, 1]]

for i in range(1, 7) :
    dir, dist = map(int, input(). split())
    arr[i][0] = (arr[i-1][0] + d[dir-1][0]*dist)
    arr[i][1] = (arr[i-1][1] + d[dir-1][1]*dist)

x = []
y = []

for j in range(6) :
    x.append(arr[j][0])
    y.append(arr[j][1])

for point in [[max(x), max(y)], [max(x), min(y)], [min(x), max(y)], [min(x), min(y)]] :
    if point not in arr :
        break

ans = abs((max(x)-min(x)))*abs((max(y)-min(y)))
x = list(set(x))
y = list(set(y))
x.sort()
y.sort()
ans -= abs(point[0]-x[1])*abs(point[1]-y[1])

print(ans*n)
