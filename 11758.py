n = 3
lst = []
while n > 0 :
    lst.append(list(map(int, input().split())))
    n -= 1
a, b, c = lst[0], lst[1], lst[2]

val = ((b[0]-a[0]) * (c[1]-a[1])) - ((b[1]-a[1]) * (c[0]-a[0]))

if val == 0 :
    print(0)
elif val > 0 :
    print(1)
else :
    print(-1)