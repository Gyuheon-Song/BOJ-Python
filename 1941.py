import sys
from collections import deque
input = sys.stdin.readline

arr = [list(map(str, input().rstrip())) for _ in range(5)]

def DFS(depth, std, s_cnt) :
    global ans
    if std > 7 :
        return
    # 25명의 학생들에 대한 탐색을 다 했을때 
    if depth == 25 :
        # 학생수가 7명에 다솜파가 4명 이상인 조합이면서
        if std == 7 and s_cnt >= 4 :
            # 인접한 학생들의 조합이면 ans+=1
            if CHK() :   # chk가 참거짓을 반환한다
                ans += 1
        return

    # 학생을 포함시키는 경우
    visited1[depth//5][depth%5] = True
    DFS(depth+1, std+1, s_cnt + (arr[depth//5][depth%5] == 'S'))   # 다솜파의 경우를 boolean으로 반환하여 더한다
    visited1[depth//5][depth%5] = False  
    
    # 학생을 포함시키지 않는 경우
    DFS(depth+1, std, s_cnt)


def CHK() :   # 인접한 학생들인지 확인 함수
    for i in range(5) :
        for j in range(5) :
            if visited1[i][j] :   # 골라진 학생조합에서 첫 학생을 만났을때
                return BFS(i, j)   # BFS를 통해 그 학생들이 인접한 7명인지를 보자  (참, 거짓 반환)


def BFS(r, c) :   # 인접하게 7명까지 뻗어나갈 수 있는지 탐색
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    q = deque()
    visited2 = [[False] * (5) for _ in range(5)]   # BFS용 또다른 방문배열

    q.append((r, c))  # 첫 학생 좌표
    visited2[r][c] = True   # 방문표시
    cnt = 1   # 1명으로 시작

    while q :
        row, col = q.popleft()  

        for i in range(4) :
            nr = row + dr[i]
            nc = col + dc[i]
            # 범위내의 학생이면서 아직 BFS내에서 방문하지 않았으며, DFS에서 골라진 조합에 해당하는 학생일 때
            if 0 <= nr < 5 and 0 <= nc < 5 and not visited2[nr][nc] and visited1[nr][nc]:
                visited2[nr][nc] = True   # BFS 방문표시
                q.append((nr, nc))
                cnt += 1   # 카운트 하나 늘려준다
    
    return cnt == 7   # 학생이 7명인지의 여부를 반환


ans = 0
visited1 = [[False]*(5) for _ in range(5)]
DFS(0, 0, 0)   # 학생번호, 포함학생수, 다솜학생수
print(ans)