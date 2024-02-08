import sys
from collections import deque
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m, g, r = map(int, input(). split())

# 0 == 호수, 1 == 배양액 불가, 2 == 배양액 가능 
# 주변을 호수로 둘러싼다
garden = [[0] * (m+2)] + [[0]+list(map(int, input(). split()))+[0] for _ in range(n)] + [[0] * (m+2)]
nutri = []  # 배양액 뿌릴 수 있는 칸의 좌표를 저장하는 리스트

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for i in range(1, n+1) :
    for j in range(1, m+1) :
        if garden[i][j] == 2 :   # 배양 뿌릴 수 있는 땅이면 저장
            nutri.append((i, j))

tc = len(nutri)  # 총 배양액을 뿌릴 수 있는 칸의 수

# 가능한 장소에 배양액 뿌리는 모든 경우 탐색
def DFS(admin, rcnt, gcnt, nutri_tp_lst) :   # 매개변수 -->>  탐색한 칸의 수, 사용한 빨간배양액, 사용한 초록 배양액, 배양액 사용가능 칸에 투여한 배양액의 종류를 저장한 리스트
    global ans

    if admin == tc :    # 배양액을 뿌릴 수 있는 총 칸의 수만큼 탐색을 했을 때
        if rcnt == r and gcnt == g :   # 투여한 배양액의 수가 색별로 정확히 맞다면 
            ans = max(ans, BFS(nutri_tp_lst))   # 정답 구하자
        return
    
    DFS(admin+1, rcnt+1, gcnt, nutri_tp_lst+[-1])   # 빨간 배양액 사용한 경우 해당 값에 증가처리하고 종류리스트에는 -1을 담는다
    DFS(admin+1, rcnt, gcnt+1, nutri_tp_lst+[1])    # 초록 배양액 사용한 경우 해당 값에 증가처리하고 종류리스트에는 1을 담는다
    DFS(admin+1, rcnt, gcnt, nutri_tp_lst+[0])        # 배양액 사용하지 않은 경우 해당 값에 증가처리하고 종류리스트에는 0을 담는다


def BFS(nutri_tp_lst) :
    q = deque()
    visited = [[0]*(m+2) for _ in range(n+2)]   # 배양액 색별로 채워져가는 시간을 표시할 방문리스트
    cnt = 0    # 꽃의 개수

    for i in range(tc) :
        if nutri_tp_lst[i] == 0 : # 배양액을 쓰지 않았다면 그냥 진행
            continue
        ti, tj = nutri[i]  # 배양액을 썻다면 해당 좌표를 언팩
        q.append((ti, tj))  # 큐에 좌표를 넣어주고
        visited[ti][tj] = nutri_tp_lst[i]   # 방문배열에는 어떤 색을 사용했는지의 숫자를 넣어주자

    while q :
        cr, cc = q.popleft()

        if visited[cr][cc] == 10000 :     # 현재 칸이 꽃이라면 예외처리
            continue

        for i in range(4) :
            nr = cr + dr[i]
            nc = cc + dc[i]
            if garden[nr][nc] == 0 or visited[nr][nc] == 10000 :  # 탐색할 위치가 호수이거나 꽃인 경우는 예외처리
                continue
        
            if visited[nr][nc] == 0 :     # 첫 방문인 경우
                if visited[cr][cc] < 0 :  # 현재칸이 빨간 배양액이 있는 칸인 경우 음수로 표시되어있을 것이다
                    visited[nr][nc] = visited[cr][cc] - 1
                    q.append((nr, nc))
                else :            # 현재칸이 초록 배양액이 있는 칸인 경우
                    visited[nr][nc] = visited[cr][cc] + 1
                    q.append((nr, nc))
            
            else :                        # 가려고자 하는 칸이 배양액이 퍼지고 있는 칸이면
                if visited[cr][cc] < 0 :    # 현재칸에서 빨간색이 퍼지고 있을 때
                    if visited[cr][cc] + visited[nr][nc] -1 == 0: # 다음칸에 초록색이 같은 시간에 퍼진다면
                        cnt += 1    # 꽃이 필 것이다
                        visited[nr][nc] = 10000  # 꽃 표기
                else :                   # 현재 칸에서 초록색이 퍼지고 있을 때
                    if visited[cr][cc] + visited[nr][nc] + 1 == 0 :  # 다음칸에 빨간색이 같은 시간에 퍼진다면
                        cnt += 1   # 꽃이 핀다
                        visited[nr][nc] = 10000   # 꽃 표기
    
    return cnt  # 꽃 개수 반환


ans = 0   # 정답변수 초기화선언

DFS(0, 0, 0, [])

print(ans)


