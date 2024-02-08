import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t) :
    n = int(input())
    lst = list(map(int, input(). strip(). split()))
    pay = [0]*n
    highest = 0
    benefit = 0
    for i in range(n-1, -1, -1) :
        if i == n-1 :
            if lst[i] > lst[i-1] :
                highest = lst[i]
        else :
            if highest > lst[i] :
                pay[i] = highest
            else :
                highest = lst[i]
    for i in range(n) :
        if pay[i] > 0 :
            benefit = benefit - lst[i] + pay[i]
    print(benefit)
        



    

