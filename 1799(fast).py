import sys
input = sys.stdin.readline


# 체스판의 흑/백은 비숍이 상호이동을 할 수 없다
# 따라서 체스판 탐색을 할 때 흑/백을 나누어 대각선번호를 0부터 2씩 증가하는 탐색과, 1부터 2씩 증가하는 탐색으로
# 나누어 연산하면 시간복잡도를 줄일 수 있다


n = int(input())
# n-Queen과 비슷하게 풀이 but, 사선방향으로 놓자(사선은 총 2n-1개)
board = [list(map(int, input(). split())) for _ in range(n)]
# 사선번호별 좌표저장 리스트(우상향 대각선)
lst = [[] for _ in range(2*n-1)]
visited = [False] * (2*n-1)
l = 2*n-1

def DFS(depth, cnt) :
    global ans
    # 남은 동일 색상 우상향 대각선((l-현재 depth)개)에다가 방금까지 놓은 비숍의 수를 다 더하여도 여태까지 구해놓은 현재최대 배치가능 비숍 수보다 작을 때
    # 더이상 해당 회차의 DFS는 무의미하므로 return 
    if ans >= cnt + (l+1-depth)//2 :
        return

    # 만약 마지막 사선까지 비숍의 배치를 완료했다면 리턴
    if depth >= l :
        ans = max(ans, cnt)
        return
    
    # 현재의 사선에서 비숍을 하나 놓고 다음 대각선으로 이동하자
    for ci, cj in lst[depth] :
        # 좌하향 대각선방향을 고려했을 때 비숍이 아직 없다면
        if not visited[ci-cj] :
            visited[ci-cj] = True
            DFS(depth+2, cnt+1)   # 다음 동일한 색의 우상향 대각선을 따져보고 방금놓은 비숍의 개수를 더하여 재귀호출
            visited[ci-cj] = False

    # 비숍을 놓지 않고 다음 동일한 색의 대각선으로 넘어가는 방법도 탐색해야 한다
    DFS(depth+2, cnt)

# 비숍을 놓을 수 있는 위치인 경우, 리스트의 i+j 위치에 append
for i in range(n) :
    for j in range(n) :
        if board[i][j] == 1 :
            lst[i+j].append((i, j))  

ans= 0
# 백색 대각선부터 비숍배치탐색
DFS(0, 0)
# 백색 대각선만 고려했을 때의 배치가능 비숏 개수 저장
white = ans
# 흑색 대각선 연산을 위해 정답변수 초기화
ans = 0
# 흑색 대각선에서 비숍배치탐색
DFS(1, 0)
# 백색과 흑색대각선에서의 배치가능 최대 비숍의 개수를 더하여 출력
print(ans + white)