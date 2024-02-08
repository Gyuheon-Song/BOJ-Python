import sys
n = int(input())

lst = []   # 숫자 리스트
dp = [0]*(n)   # 연속하는 3개를 고르지 않는 방법으로 해당 번째의 수까지의 최다합을 저장하는 리스ㅡ

for _ in range(n) :
    lst.append(int(input()))

dp[0] = lst[0]   

if n >= 2 :   # 주어진 수의 길이가 2보다 크거나 같을 때
    dp[1] = lst[0]+lst[1]   # 2번째까지의 최대합은 그냥 두수의 합

if n >= 3 :   # 주어진 숫자의 개수가 3개 이상일 때부터는 조건에 맞춰 영우의 수를 고려
    for i in range(2, n) :
        # 전전번째까지의 최대합+현재 수, 이번 수를 안고르는 경우, 3수 전까지의 최대합+한 숫자 건너뛴 두 숫자의 연속합
        dp[i] = max(dp[i-2]+lst[i], dp[i-1], dp[i-3]+lst[i-1]+lst[i])

print(max(dp))
