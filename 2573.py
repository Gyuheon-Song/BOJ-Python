import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input(). split())

ice = [list(map(int, input(). split())) for _ in range(n)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def Solve() :  # 1년부터 최악의 경우인 90000년까지 전체순회 반복작업 실행

    for year in range(1, 100000) :
        # 사방의 0의 개수를 카운트하여 저장하는 배열
        surr = [[0]*m for _ in range(n)]
        # 테두리는 어차피 바다이므로 제외하고 순회한다
        for i in range(1, n-1) :
            for j in range(1, m-1) :
                # 현재 칸이 물인 경우는 그냥 진행
                if ice[i][j] == 0 :
                    continue
                # 사방에 대하여
                for k in range(4) :
                    nr = i + dr[k]
                    nc = j + dc[k]
                    # 사방에 0인 칸이 있다면
                    if ice[nr][nc] == 0 :
                        # 0인 칸의 개수만큼 더한다
                        surr[i][j] += 1

        # 높이 낮추기
        for i in range(1, n-1) :
            for j in range(1, m-1) :
                # 만약 주변에 0이 존재한다면
                if surr[i][j] > 0 :
                    # 현재 빙산의 높이에서 사방의 0의 개수만큼 뺀 값을 저장(그러나 연산의 결과가 음수인경우 0이 될 수 있도록 max연산)
                    ice[i][j] = max(0, ice[i][j]-surr[i][j])

        # 빙산의 덩어리 개수 세보자
        visited = [[False]*(m) for _ in range(n)]   # 방문배열
        cnt = 0   # 덩어리 개수 변수
        for i in range(1, n-1) :
            for j in range(1, m-1) :
                if not visited[i][j] and ice[i][j] > 0 :   # 아직 방문하지 않은 칸이면서 해당 칸에 빙산이 존재한다면
                    BFS(i, j, visited)     #  BFS로 덩어리의 범위를 방문처리
                    cnt += 1   # 덩어리 개수 1증가
                    if cnt > 1 :  # 덩어리의 개수가 2이상이면
                        return year  # 년도를 반환
        
        if cnt == 0 :   # 만약 빙산이 없다면
            return 0   # 0을 반환


def BFS(r, c, visited) :
    q = deque()

    q.append((r, c))
    visited[r][c] = True

    while q :
        row, col = q.popleft()
        for i in range(4) :
            nr = row + dr[i]
            nc = col + dc[i]
            if not visited[nr][nc] and ice[nr][nc] > 0 :
                q.append((nr, nc))
                visited[nr][nc] = True

ans = Solve()
print(ans)