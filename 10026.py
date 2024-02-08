import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
rgb = [list(input().rstrip()) for _ in range(n)]   # 색 구역 2차원배열
visited = [[False]*(n) for _ in range(n)]     # 방문리스트 false로 초기화

dr = [-1, 0, 1, 0]    
dc = [0, 1, 0, -1]
clrweak = 0     # 색약이 구별할 수 있는 구역개수
clr = 0         # 비색약

def BFS(row, col) :    
    q = deque()
    q.append((row, col))    # 행과 열을 큐에 삽입
    visited[row][col] = True   # 해당 행과 열을 방문으로 표시
    while q :
        r, c = q.popleft()     # 큐에서 행과 열 언패킹
        for i in range(4) :    # 사방탐색
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nc < 0 or nr >= n or nc >= n :
                continue
            # 탐색한 칸이 탐색이전의 칸과 같은 색이며 아직 방문하지 않은 칸일때 해당 칸을 방문처리 후 큐에 삽입
            elif rgb[nr][nc] == rgb[r][c] and (not visited[nr][nc]) :
                visited[nr][nc] = True
                q.append((nr, nc))

# 비색약    
for i in range(n) :
    for j in range(n) :
        if not visited[i][j] :
            clr += 1
            BFS(i, j)

# 색약의 구간구별개수를 구하기 위한 방문배열 초기화
visited = [[False]*(n) for _ in range(n)]

# 색약조건을 위해 초록과 빨강을 한 색으로 통일
for i in range(n) :
    for j in range(n) :
        if rgb[i][j] == "G" :
            rgb[i][j] = "R"

# 색약
for i in range(n) :
    for j in range(n) :
        if not visited[i][j] :
            clrweak += 1
            BFS(i, j)

print(clr, clrweak)




# DFS로도 풀이가능
# def DFS(row, col) :
#     visited[row][col] = True
#     color = rgb[row][col]
#     for i in range(4) :
#         nr = row + dr[i]
#         nc = col + dc[i]
#         if 0 <= nr < n and 0 <= nc < n :
#             if not visited[nr][nc] and rgb[nr][nc] == color :
#                 DFS(nr, nc)