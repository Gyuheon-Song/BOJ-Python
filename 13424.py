import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t) :
    n, m = map(int, input(). split())
    adjmtrx = [[sys.maxsize]*(n+1) for _ in range(n+1)]     # 최대거리로 인접행렬 초기화

    for _ in range(m) : 
        a, b, c = map(int, input(). split())
        adjmtrx[a][b] = c              # 양방향 간선
        adjmtrx[b][a] = c

    for i in range(1, n+1) :           # 같은 방의 경우 거리를 0으로 설정
        adjmtrx[i][i] = 0

    # 플로이드 워셜
    for k in range(1, n+1) :
        for i in range(1, n+1) :
            for j in range(1, n+1) :
                adjmtrx[i][j] = min(adjmtrx[i][j], adjmtrx[i][k] + adjmtrx[k][j])
    
    #친구수와 위치하는 방 정보 입력
    friendnum = int(input().rstrip())
    friend = list(map(int, input().rstrip().split()))
    
    # 정답리스트 생성(각 방에 대해 각 친구 까지의 최소거리의 합을 저장한다)
    ans = [0 for _ in range(n+1)]
    # 0번방은 제외
    ans[0] = sys.maxsize

    # 각 친구까지의 거리를 정답리스트에 방번호 인덱스에 저장 
    for i in friend :
        for j in range(1, n+1) :
            ans[j] += adjmtrx[i][j]
    
    # 거리가 최소가 되는 인덱스가 방번호이다
    print(ans.index(min(ans)))