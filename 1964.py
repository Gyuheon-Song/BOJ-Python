n = int(input())
ans = 1

for i in range(1, n+1) :
    ans += i*3 + 1

print(ans%45678)