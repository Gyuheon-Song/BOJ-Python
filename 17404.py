import sys
input = sys.stdin.readline
n = int(input())
rgb = [list(map(int, input(). split())) for _ in range(n)]   #집 색칠비용을 입력받는다

ans = INF = sys.maxsize    # 결과를 최댓값으로 초기화

for i in range(3) :
    dp = [[INF, INF, INF] for _ in range(n)]      # 계산을 수행해나갈 임시리스트를 최댓값으로 초기화
    dp[0][i] = rgb[0][i]           # 첫번째 집 색칠비용은 그대로 대입
    for j in range(1, n) :
        dp[j][0] = rgb[j][0] + min(dp[j-1][1], dp[j-1][2])      #  규칙에 맞게 색칠해나갈 수 있는 최솟값을 임시리스트에 초기화
        dp[j][1] = rgb[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = rgb[j][2] + min(dp[j-1][0], dp[j-1][1])
    for k in range(3) :
        if i != k :             # 처음 시작 집의 인덱스가 i이므로 i와 다른 인덱스의 집을 마지막에 칠했을 때의
            ans = min(ans, dp[-1][k])      # 최솟값만을 결과변수에 초기화

print(ans)

