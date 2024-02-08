import sys
input = sys.stdin.readline

n = int(input())
adjmtrx = [[0]*(n+1) for _ in range(n+1)]    # 친구관계(1, 0으로)를 나타낼 인접행렬
friend = [[0]*(n+1)]   # 친구관계 입력받을 리스트

for _ in range(n) :
    friend.append([0]+list(input().rstrip()))

# 플로이드 워셜 알고리즘 실행
for k in range(1, n+1) :
    for i in range(1, n+1) :
        for j in range(1, n+1) :
            if i == j :      # 자기자신과의 관계는 친구가 아니므로 0으로 놔둔다
                continue
            # 직접 친구이거나 다른 사람을 경유해서 친구인 경우에는 친구관계 1로 표시한다
            if friend[i][j] == "Y" or (friend[i][k] == "Y" and friend[k][j] == "Y") :
                adjmtrx[i][j] = 1

ans = 0

for i in range(1, n+1) :    # 각 사람에 대하여 직접친구이거나 하나건너 친구인 사람수를 센다
    cnt = 0
    for j in range(1, n+1) :
        if adjmtrx[i][j] == 1 :
            cnt += 1
    ans = max(ans, cnt)       # 가장 많은 2-친구를 가진 사람의 2-친구수를 저장한다       

print(ans)             