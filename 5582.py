import sys
input = sys.stdin.readline

w1 = list(input().strip())
w2 = list(input().strip())

dp = [[0]*(len(w1)+1) for _ in range(len(w2)+1)]

ans = 0
for i in range(len(w2)+1) :
    for j in range(len(w1)+1) :
        if i == 0 or j == 0 :
            dp[i][j] = 0
        elif w2[i-1] == w1[j-1] :
            dp[i][j] = dp[i-1][j-1] + 1
            ans = max(ans, dp[i][j])
        else :
            dp[i][j] = 0

print(ans)



