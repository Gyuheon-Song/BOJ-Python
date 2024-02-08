import sys
input = sys.stdin.readline

n, k = map(int, input(). split())
adjmtrx = [list(map(int, input(). split())) for _ in range(n)]
visited = [False] * (n)    # 백트래킹을 위한 방문배열
visited[k] = True          # 입력받은 현위치는 방문으로 표시
ans = 10e9            # 정답변수에 충분히 큰 수 초기화

# 플로이드 워셜 알고리즘
for p in range(n) :
    for i in range(n) :
        for j in range(n) :
            adjmtrx[i][j] = min(adjmtrx[i][j], adjmtrx[i][p] + adjmtrx[p][j])
                
# 백트래킹하며 최소시간을 찾는 함수
def minTime(now, cnt, time) :    # 현재행성과, 현재까지방문한 행성수, 현재까지 소요된 시간
    global ans
    if cnt == n :    # 모든 행성에 다 방문했을때
        ans = min(time, ans)    # 지금까지 걸린 시간과 기존의 항로의 소요시간 중 작은값 저장
        return
    for next in range(n) :   # n개의 행성에 대해 다음 목적지를 잡을수 있다
        if not visited[next] :   # 목적 행성이 아직 방문하지 않은 행성일때
            visited[next] = True    # 해당 행성을 방문하고

            # 해당항성이 현재행성이되고, 방문행성수는 1증가하며, 시간또한 해당항로만큼 더해주어 재귀호출
            minTime(next, cnt+1, time+adjmtrx[now][next])
            # DFS  
            visited[next] = False

minTime(k, 1, 0)
print(ans)