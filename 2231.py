n = int(input())
ans = 1000000
for x in range(1, 999960) :
    lst = list(map(str, str(x)))
    lst = list(map(int, lst))
    if x + sum(lst) == n :
        ans = min(ans, n - sum(lst))   

print(ans) if ans != 1000000 else print(0)
    