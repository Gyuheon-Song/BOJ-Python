import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m = map(int, input(). split())
board = [list(input().rstrip()) for _ in range(n)]
# 쓰인 알파벳을 표시할 일종의 방문배열
alphabet = [False]*26

ans = 0   # 지나갈 수 있는 최대 칸수를 저장하는 변수
cnt = 0   # 지나가는 칸의 개수를 실시간 계산하는 변수

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def DFS(row, col) :
    global ans, cnt
    alphabet[ord(board[row][col])-65] = True
    cnt += 1
    ans = max(ans, cnt)
    for i in range(4) :
            nr = row + dr[i]
            nc = col + dc[i]
            # 만약 이동할 칸이, 보드 밖으로 나가지 않으면서 지나왔던 알파벳이 아닌 칸이라면
            if 0 <= nr < n and 0 <= nc < m and not alphabet[ord(board[nr][nc])-65] :
                DFS(nr, nc)  # 재귀호출로 다음칸부터 다시 탐색
                alphabet[ord(board[nr][nc])-65] = False
                cnt -= 1
            else :
                 continue
                      
DFS(0, 0)  # 시작 칸
print(ans)
