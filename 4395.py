t = int(input())

for _ in range(t) :
    x, y = map(int, input(). split())
    if x == y :
        print(0)
        continue
    else :
        n = 0
        d = y-x
        while True :
            if d <= n*(n+1) :
                break
            n += 1
        if d <= n*n :
            print(2*n-1)
        else :
            print(2*n)