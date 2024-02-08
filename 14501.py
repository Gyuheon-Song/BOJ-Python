import sys
input = sys.stdin.readline

n = int(input())

lst = [list(map(int, input(). split())) for _ in range(n)]

dp = [0 for _ in range(n+1)]

for i in range(n) :
    for j in range(i+lst[i][0], n+1) :
        dp[j] = max(dp[j], dp[i]+lst[i][1])

print(dp[-1])

# 백트래킹 풀이
# lst = [0]
# ans = 0

# for _ in range(n) :
#     lst.append(list(map(int, input(). split())))

# def DFS(x, profit) :
#     global ans
#     if x >= n+1 :
#         ans = max(ans, profit)
#         return
#     if x+lst[x][0] <= n+1 and x <= n :
#         DFS(x+lst[x][0], profit+lst[x][1])
#         DFS(x+1, profit)
#     else :
#         if x < n :
#             DFS(x+1, profit)
#         ans = max(ans, profit)

# for i in range(1, n+1) :
#     if i + lst[i][0] <= n+1 :
#         DFS(i+lst[i][0], lst[i][1])

# print(ans)
