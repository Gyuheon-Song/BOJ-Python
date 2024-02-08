import sys
input = sys.stdin.readline

def Find(x) :        # 부모노드 찾기(사이클 존재여부 찾기)
    if x == u_fnd_lst[x] :
        return x
    else :
        u_fnd_lst[x] = Find(u_fnd_lst[x])
        return u_fnd_lst[x]

def Union(a, b) :        # 부모노드 다를때(길을 연결할 시에도 사이클이 형성되지 않을 때)
    a = Find(a)          # 길을 연결하는 함수
    b = Find(b)
    # if a != b :
    u_fnd_lst[b] = a

def Chk(a, b) :       # 사이클 예상 함수
    a = Find(a)
    b = Find(b)
    if a == b :
        return True
    return False

while True :
    n, m = map(int, input(). split())
    if n == 0 & m == 0 :
        break
    u_fnd_lst = [i for i in range(n)]     # 유니온 파인드 리스트
    pq = []
    used_path = 0    # 사용된 길의 개수를 저장할 변수
    ans = 0          # 사용된 길의 비용을 저장할 변수
    maximum_cost = 0    # 주어진 모든 길의 비용의 총 합 저장 변수

    for _ in range(m) :        # 길의 양방향 정보 받기
        x, y, z = map(int, input(). split())
        pq.append((z, x, y))
        maximum_cost += z

    pq.sort(reverse = True)     # 우선순위큐 구현

    while used_path < n-1 :     # 길이 n-1개보다 적게 사용되었을 때 반복
        price, s, e = pq.pop()
        if not Chk(s, e) :     # 연결시에도 사이클이 생기지 않을 때
            Union(s, e)        # 길을 연결한다
            used_path += 1     # 사용한 엣지의 수 ++
            ans += price       # 사용한 비용(가중치)을 더해나간다

    print(maximum_cost-ans)    # 총 비용에서 사용한 비용 빼면 절약비용
