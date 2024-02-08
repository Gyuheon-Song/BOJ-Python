import sys
input = sys.stdin.readline
from collections import deque
import copy

n, m = map(int, input(). split())
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
lab = [list(map(int, input(). split())) for _ in range(n)]
ans = 0

def BFS() :
    global ans
    cnt = 0   # 벽을 세우고 나서 안전지역의 개수를 저장할 변수
    temp = copy.deepcopy(lab)    # 원본이 변형될때마다 같이 바뀔 수 있도록 깊은 복사
    q = deque()   

    # 연구소에서 바이러스가 있는 칸이면(2) 큐에 넣는다
    for i in range(n) :    
        for j in range(m) :
            if temp[i][j] == 2 :
                q.append((i, j))
    # 큐에 있는 발원지부터 바이러스가 번진다
    while q :
        r, c = q.popleft()
        for i in range(4) :
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nc < 0 or nr >= n or nc >= m :
                continue
            elif temp[nr][nc] == 0 :
                temp[nr][nc] = 2
                q.append((nr, nc))
    # 바이러스가 다 번지고 난 후에 안전지대(0)의 개수를 센다
    for i in range(n) :
        cnt += temp[i].count(0)
    # 정답변수에 안전지대가 최대인 값을 계속 초기화한다
    ans = max(ans, cnt)


def MakeWall(wallnum) :    # 브루트포스 벽세우기
    if wallnum == 3 :    # 벽을 3개 세웠다면 바이러스가 번지는 시뮬을 돌린다
        BFS()
        return
    # 브루트포스 벽(DFS)
    for i in range(n) :
        for j in range(m) :
            if lab[i][j] == 0 :
                lab[i][j] = 1
                # 벽을 세우고 세운 벽의 개수에 1을 더해서 재귀호출
                MakeWall(wallnum+1)
                lab[i][j] = 0     # 세운 벽이 3개가 되어 바이러스전염 시뮬레이션을 돌리고 벽을 하나씩 허물면서 백트래킹

MakeWall(0)  # 벽세우기를 하며 바이러스 시뮬레이션을 돌린다((0인 칸의 개수)C3 번의 BFS가 돌게 될 것이다)
print(ans)




            
