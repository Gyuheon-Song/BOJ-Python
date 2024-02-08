n = int(input())

dp = [0]*(n+1)  # 인덱스의 수를 1로 만들기 위한 최소횟수를 저장하는 리스트
parent = [-1]*(n+1)   # 최소횟수로 1을 만드는 과정에서의 다음 수를 저장하는 리스트

for i in range(1, n+1) :

    if i % 3 == 0 :   # 3으로 어지는 수에 대해
        dp[i] = min(dp[i//3] + 1, dp[i-1] + 1)   # 1을 뺀 숫자가 1이 되기위한 최소횟수와 3으로 나눈 수가 1이 되기위한 최소 횟수 중 작은 값 저장
        if dp[i] == dp[i//3] + 1 :  # 만약 3으로 나눈 수가 더 적은 횟수만에 1이 될 수 있으면 
            parent[i] = i//3  # 부모노드로 저장
        else :
            parent[i] = i-1  # 1을 뺀 수가 더 적은 횟수만에 1이 될 수 있으면 그 수를 부모노드로 저장
    elif i % 2 == 0 :
        dp[i] = min(dp[i//2] + 1, dp[i-1] + 1)
        if dp[i] == dp[i//2] + 1 :
            parent[i] = i//2
        else :
            parent[i] = i-1
    else :
        dp[i] = dp[i-1] + 1
        parent[i] = i-1
                    
    if i % 2 == 0 and i % 3 == 0 :   # 6의 공배수인 경우
        dp[i] = min(dp[i//2] + 1, dp[i//3] + 1, dp[i-1] + 1)  # 3가지 경우에 대해 최소횟수를 저장
        if dp[i] == dp[i//2] + 1:
            parent[i] = i//2
        elif dp[i] == dp[i//3] + 1 :
            parent[i] = i//3
        else :
            parent[i] = i-1


tmp = n
print(dp[n]-1)
while tmp != 0 :  # 1까지의 경로를 출력
    print(tmp, end = " ")
    tmp = parent[tmp]



    