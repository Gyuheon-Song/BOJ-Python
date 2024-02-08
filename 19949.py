n, k = map(int, input(). split())
sum = 0
for i in range(1, k+1) :
    sum += i

if sum > n :
    print(-1)
else :
    if sum == n :
        print(k-1)
    else :
        n -= sum
        if n % k == 0 :
            print(k-1)
        else :
            print(k)