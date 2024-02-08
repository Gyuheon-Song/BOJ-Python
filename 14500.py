import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def DFS(r, c, depth, latest) :   # 테트로미노의 모양을 DFS로 구현, depth가 3까지 탐색하면 테트로미노
    global ans
    # 종이에서 가장 큰 수가 나머지 칸을 전부 채운다고 할때 최근까지 탐색한 칸까지의 총합과 그 값을 더해도 기존의 초기화된 정답보다 작으면 종료
    if ans >= latest + large_num*(3-depth) :  
        return
    # depth가 3일때 테트로미노이므로 정답에 최대값을 저장
    if depth == 3 :
        ans = max(ans, latest)
        return
    
    else :
        for i in range(4) :
            nr = r + dr[i]
            nc = c +dc[i]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] :
                # ㅓ 모양을 DFS탐색하기 위해선 depth가 1 일때 중간점을 잡아줘야 한다
                if depth == 1 :
                    visited[nr][nc] = True
                    DFS(r, c, depth+1, latest + paper[nr][nc])
                    visited[nr][nc] = False
                visited[nr][nc] = True
                DFS(nr, nc, depth+1, latest + paper[nr][nc])
                visited[nr][nc] = False
                

n, m = map(int, input(). split())
paper = [list(map(int, input(). split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
ans = 0
large_num = max(map(max, paper))

for row in range(n) :
    for col in range(m) :
        visited[row][col] = True
        DFS(row, col, 0, paper[row][col])
        visited[row][col] = False

print(ans)