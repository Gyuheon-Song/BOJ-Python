import sys
input = sys.stdin.readline
lst = list(map(int, input(). split()))
sum = 0
for num in lst :
    sum += num**2

ans = sum%10
print(ans)