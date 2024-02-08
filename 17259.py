import sys
input = sys.stdin.readline
b, n, m = map(int, input(). split())
factory = [[0]*(b) for _ in range(b)]
workerlst = []
d = [[1, 0], [-1, 0], [0, -1]]   # 선물의 우측에는 직원 존재 불가하므로 3면만 탐색하면 된다
ans = 0

class Workers :   # 직원 객체(행번호, 열번호, 포장에걸리는 시간, 남은 포장 시간, 포장가능여부)
    def __init__(self, r, c, t, pack, canwork) :
        self.r = r
        self.c = c
        self.t = t
        self.pack = pack
        self.canwork = canwork

def Rotate() :    # 컨베이어 벨트 회전 함수
    global m
    if factory[b-1][0] == 1 :     # 만약 컨베이어 벨트 끝에 선물이 남아있는 경우 폐기
        factory[b-1][0] = 0
        m -= 1
    for i in range(b-1) :     # 컨베이어 벨트의 아래 모서리를 왼쪽으로 한칸씩 이동
        factory[b-1][i] = factory[b-1][i+1]
    
    for i in range(b-1, 0, -1) :     # 컨베이어 벨트의 오른쪽 모서리를 아래로 한칸씩 이동
        factory[i][b-1] = factory[i-1][b-1]
    
    for i in range(b-1, 0, -1) :    # 컨베이어 벨트의 위 모서리를 오른쪽으로 한칸씩 이동
        factory[0][i] = factory[0][i-1]


def isThereWorker(r, c) :    # 선물 주변의 포장 가능한 직원 찾기
    global m, ans
    for i in range(3) :   # 인접한 곳
        nr = r + d[i][0]
        nc = c + d[i][1]
        if 0 <= nr < b and 0 <= nc < b :
            # 선물 주변에 직원이 존재하고 해당 직원이 포장 가능한 상태이면
            if factory[nr][nc] >= 10 and workerlst[factory[nr][nc]-10].canwork == True :
                factory[r][c] = 0   # 벨트에서 선물을 빼서 포장을 시작하고
                m -= 1    # 전체 선물의 개수를 1 감소
                ans += 1   # 포장한 선물의 개수 1 증가
                workerlst[factory[nr][nc]-10].canwork = False   # 해당 직원은 일정시간동안 포장 불가 상태에 돌입
                break
        else :
            continue

for i in range(n) :
    r, c, t = map(int, input(). strip(). split())
    worker = Workers(r, c, t, t, True)     # 직원의 각 정보를 담은 객체 생성
    workerlst.append(worker)    # 직원 리스트에 생성한 객체 저장
    factory[r][c] = i + 10    # 공장배열의 직원 위치에 직원의 인덱스 + 10을 저장 -> 선물표시와 헷갈리지 않기 위해

notOnBelt = m   # 벨트에 아직 올리지 않은 선물의 개수
while m :   # 포장해야할 선물이 존재하는동안
    Rotate()   # 컨베이어 벨트를 한칸씩 돌린다
    if notOnBelt > 0 :  # 벨트에 아직 올라가지 않은 선물이 존재한다면 벨트의 첫 번째 자리에 선물 올리기
        factory[0][0] = 1
        notOnBelt -= 1
    
    else :
        factory[0][0] = 0  # 모든 선물이 일단 벨트에 올려졌다면 더이상 선물은 올라가지 않고 벨트만 돌아간다
    
    # 오른쪽 위와 오른쪽 아래 꼭짓점은 인접한 직원이 존재할 수 없으므로 제외하고 탐색
    # 가장 오래된 선물부터 순차적으로 탐색하는 것이 중요!! 왼쪽 아래 -> 오른쪽 아래 -> 오른쪽 위 -> 왼쪽 위

    for i in range(b-1) :     # 아래 모서리 컨베이어 벨트에 놓여 있는 선물에 대해
        if factory[b-1][i] == 1 :
            isThereWorker(b-1, i)   # 인접한 직원이 있는지 탐색

    for i in range(b-2, 0, -1) :   # 오른쪽 모서리 컨베이어 벨트에 놓여 있는 선물에 대해
        if factory[i][b-1] == 1 :
            isThereWorker(i, b-1)   # 인접한 직원이 있는지 탐색

    for i in range(b-2, -1, -1) :    # 위 모서리 컨베이어 벨트에 놓여 있는 선물에 대해
        if factory[0][i] == 1 :
            isThereWorker(0, i)    # 인접한 직원이 있는지 탐색
    
    for i in range(n) :    # 직원들의 포장작업상태 수정
        if not workerlst[i].canwork :   # 만약 포장 불가 상태, 즉 포장 중인 직원이라면
            workerlst[i].pack -= 1    # 포장중인 시간 1씩 감소
            if workerlst[i].pack == 0 :   # 포장시간 감소 연산이 이루어지고 남은 포장 시간이 0, 즉 포장 완료한 경우
                workerlst[i].canwork = True   # 포장 가능여부를 참으로 바꿔주고
                workerlst[i].pack = workerlst[i].t    # 포장소요 시간을 다시 초기 포장 소요시간으로 초기화시켜준다

print(ans)







