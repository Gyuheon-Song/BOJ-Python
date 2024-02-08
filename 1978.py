n = int(input())
lst = list(map(int, input(). split()))
prime = 0
for num in lst :
    cnt  = 0
    if num > 2 :
        for i in range(2, (num//2) + 2) :
            if num % i == 0 :
                cnt += 1
        if cnt == 0 :
            prime += 1
    elif num == 2 :
        prime += 1

print(prime)

    
