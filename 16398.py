import sys
input = sys.stdin.readline

n = int(input())
used_flow = 0     # 사용된 플로우 저장변수
ans = 0
pq = []
u_fnd_lst = [i for i in range(n+1)]    # 유니온 파인드 리스트
planet = [[0]*(n+1)]        # 행성별 플로우 관리비 정보 인접리스트

for _ in range(n) :
    lst = list(map(int, input(). split()))
    planet.append([0] + lst)    # 행성별 정보 저장

for i in range(1, n+1) :
    for j in range(i+1, n+1) :
        if i != j :
            cost = planet[i][j]    # i행 j열의 값은 행성 i에서 j로 가는 플로우를 설치했을 시 발생하는 비용
            pq.append((cost, i, j))   # 양방향 엣지정보를 가중치 우선으로 하여 저장
        else :
            continue

def Find(x) :      # 부모노드를 찾는함수
    if x == u_fnd_lst[x] :
        return x
    else :
        u_fnd_lst[x] = Find(u_fnd_lst[x])
        return u_fnd_lst[x]

def Union(a, b) :    # 부모노드가 같지 않을 경우 합집합 연산 함수
    a = Find(a)
    b = Find(b)
    if a != b :
        u_fnd_lst[b] = a

def Chk(a, b) :      # 두 원소가 동일한 집합(사이클존재여부)인지 판단하는 함수
    a = Find(a)
    b = Find(b)
    if a == b :
        return True
    return False

pq.sort(reverse = True)    # 우선순위큐 구현

while used_flow < n-1 :   # 플로우가 n-1개보다 적게 사용됐을 때 반복
    cost, p1, p2 = pq.pop()    # 언패킹
    if not Chk(p1, p2) :     # 두 행성을 연결해도 사이클이 만들어지지 않을 때
        Union(p1, p2)      # 두 행성에 플로우 설치(연결)
        used_flow += 1    # 플로우엣지의 사용횟수 하나씩 증가
        ans += cost        # 플로우 사용비용 더해준다

print(ans)
