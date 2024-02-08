import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def DFS(row, col) :         

    if row == m-1 and col == n-1 :        # 목표 도착지점인 오른쪽 밑 구석에 도착했을때 1 반환
        return 1
    
    if visit[row][col] == -1 :       #  한번도 도달하지 않은 칸일때
        visit[row][col] = 0          #  도달한 칸임을 표시
        for i in range(4) :
            drow = row + dr[i]
            dcol = col + dc[i]
            if 0 <= drow < m and 0 <= dcol < n :
                if graph[row][col] > graph[drow][dcol] :     # 다음칸이 내리막의 조건을 만족할 때
                    visit[row][col] += DFS(drow, dcol)       # 그 다음칸의 방문횟수를 더한다
    
    return visit[row][col]    # 해당 칸의 방문횟수 반환

# 목적지까지 도달했을 시 1을 반환받아 해당경로에서 방금 전 칸의 방문횟수에 더한다
# 이랬을 시 1이란 반환값은 출발위치까지 전달되게 되며 방문 해당경로의 방문값은 1이상이 되어 재탐색하지 않는다


m, n = map(int, input(). split())
graph = [list(map(int, input(). split())) for _ in range(m)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
visit = [[-1 for _ in range(n)] for _ in range(m)]
print(DFS(0, 0))