import sys
input = sys.stdin.readline

def Find(x) :     # 파인드
    if x == uflst[x] :
        return x
    else :
        uflst[x] = Find(uflst[x])
        return uflst[x]

def Union(a, b) :   # 유니온
    a = Find(a)
    b = Find(b)
    uflst[max(a, b)] = min(a, b)

n, m = map(int, input(). split())
direction = {}   # 방향키를 그래프탐색 벡터로 저장할 딕셔너리
direction['D'] = [1, 0]
direction['U'] = [-1, 0]
direction['R'] = [0, 1]
direction['L'] = [0, -1]
_map = [list(input().rstrip()) for _ in range(n)]
uflst = [i for i in range(n*m)]   # 유니온 파인드 리스트의 크기를 총 칸의 개수만큼 할당

for tmp in range(n*m) :   # 2차원 배열의 인덱스에 대해 유니온 파인드를 실행하기 위한 전처리도 해야한다
    col = tmp%m    # 열의 인덱스는 열의 개수로 나눈 나머지이다 (e.g. 6*5 행렬  -> 19의 경우에 열의 인덱스는 19%(5-1) = 3)
    row = tmp//m   # 행의 인덱스는 열의 개수로 나눈 몫이다     (행의 인덱스는 19//(5-1) = 4)
    cur = _map[row][col]   # 현재 칸에 들어있는 방향키
    nr = row + direction[cur][0]   # 다음 칸의 행의 좌표
    nc = col + direction[cur][1]   # 다음 칸의 열의 좌표
    next_tmp = (nr*m) + nc    # 다음 칸의 좌표를 1차원 배열로 환산
    if next_tmp < 0 or next_tmp >= n*m :   # 지도 범위 내의 칸이 아닌경우 건너뛴다
        continue
    Union(tmp, next_tmp)    # 지도 내의 범위인 경우 다음칸과 현재칸을 같은 집합으로 처리

visited = {}   # 집합의 대표칸을 저장할 딕셔너리
safe = 0   # 안전지대의 개수

for i in range(n*m) :
    if Find(uflst[i]) not in visited :   # 모든 칸에 대해서 부모칸을 탐색하고 아직 카운트하지 않은 집합이면
        safe += 1    # 안전지대 하나 증가
        visited[uflst[i]] = True   # 해당 집합은 카운트처리

print(safe)