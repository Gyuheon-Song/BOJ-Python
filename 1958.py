import sys
input = sys.stdin.readline

w1 = input().strip()
w2 = input().strip()
w3 = input().strip()

dp = [[[0]*(len(w1)+1) for _ in range(len(w2)+1)] for _ in range(len(w3)+1)]

ans = 0
for i in range(len(w3)+1) :
    for j in range(len(w2)+1) :
        for k in range(len(w1)+1) :
            if i == 0 or j == 0 or k == 0 :
                dp[i][j][k] = 0
            elif w3[i-1] == w2[j-1] == w1[k-1] :
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                ans = max(ans, dp[i][j][k])
            else :
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
                ans = max(ans, dp[i][j][k])

print(ans)