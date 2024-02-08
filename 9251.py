import sys
input = sys.stdin.readline

w1 = input().strip()
w2 = input().strip()
dp = [0]*(1000)

# 문자열을 돌면서 기준문자열의 각 문자별로, 비교하는 문자열의 문자와 동일할 때
# 해당 문자까지의 최대공통부분수열의 길이 1씩 증가
for i in range(len(w1)) :
    tmp = 0
    for j in range(len(w2)) :
        if tmp < dp[j] :
            tmp = dp[j]
        elif w1[i] == w2[j] :
            dp[j] = tmp + 1

print(max(dp))
