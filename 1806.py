n, m = map(int, (input(). split()))
lst = list(map(int, input(). split()))
start = 0
end = 0
ans = 100001
sum = lst[0]

while True :
    if sum < m :
        end += 1
        if end == n :
            break
        sum += lst[end]
    else :
        sum -= lst[start]
        ans = min(ans, end-start+1)
        start += 1
    
print(0) if ans == 100001 else print(ans)


