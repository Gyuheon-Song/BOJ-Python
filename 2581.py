a = int(input())
b = int(input())
ans = 0

mini = 10001
for num in range(a, b+1) :
    if num > 2 :
        cnt = 0
        for i in range(2, num//2 + 2) :
            if num % i == 0 :
                cnt += 1
            else :
                continue
        if cnt == 0 :
            ans += num
            mini = min(mini, num)
    elif num == 2 :
        ans += 2
        mini = num
if ans == 0:
    print(-1)
else :
    print(ans)
    print(mini)

                
