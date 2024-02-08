n = int(input())
dp = [0] * (n+1)
dp[2] = 3
for i in range(4, n+1) :
    if i % 2 == 1 :
        dp[i] = 0
    else :
        dp[i] = 3*dp[i-2] + 2*sum(dp[:i-2]) + 2

ans = dp[n]

print(ans)
