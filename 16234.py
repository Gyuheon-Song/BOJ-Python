import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input(). split())

population = [list(map(int, input(). split())) for _ in range(n)]  # 국가별 인구수를 저장하는 리스트
day = 0   # 인구이동이 발생하는 날을 저장
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
q = deque()  # 너무 많은 초기화 선언을 방지하기 위해 밖에서 선언

while day <= 2000 :   # 2000일보다 작은 답만 나오는 입력이 주어진다

    visited = [[False]*(n) for _ in range(n)]    # 방문배열
    flag = False  # 인구이동 발생유무 표지

    for i in range(n) :
        for j in range(n) :
            if not visited[i][j] :   # 아직 방문하지 않은 칸에 대해
                
                # BFS를 while 안에서 짜준다( 따로 함수를 구성할 시 함수호출이 많아지는 조건의 입력이 들어오는 문제이다-->> 되려 복잡도가 증가할 가능성이 있다)
                q.append((i, j))
                visited[i][j] = True
                nation = [(i, j)]   # 연합된 국가들의 좌표를 저장하는 리스트
                sm = population[i][j]   # 국가들의 인구를 더해나갈 변수

                while q :
                    row, col = q.popleft()
                    for k in range(4) :
                        nr = row + dr[k]
                        nc = col + dc[k]
                        # 사방탐색에 대해 방문하지 않은 국가이며 인구차이가 조건에 부합할 때
                        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and l <= abs(population[nr][nc]-population[row][col]) <= r :
                            q.append((nr, nc))
                            visited[nr][nc] = True
                            nation.append((nr, nc))  # 인구이동한 국가를 넣어준다
                            sm += population[nr][nc]   # 인구이동을 하기 위해 인구수를 더해나간다
                
                if len(nation) > 1 :  # 만약 인구이동이 발생하여 인구이동 국가의 수가 1보다 크면
                    for tr, tc in nation :  # 해당 국가들의 인구를 분배한다
                        population[tr][tc] = sm // len(nation)   # 해당 국가들의 인구의 총합 // 국가의 수
                    flag = True   # 인구이동이 발생했음을 표지
                          
    if not flag :  # 만약 인구이동이 발생하지 않았다면 중단
        break

    day += 1   # 인구이동이 발생했다면 일수를 1증가시킨다

print(day)
