import sys
input = sys.stdin.readline

n, m = map(int, input(). split())
u_fnd_lst = [i for i in range(n+1)]    # 유니온 파인드 리스트
used_edge = 0    # 연결된 엣지의 개수를 저장할 변수
ans = 0          # 연결된 엣지의 가중치들을 합할 변수
expensive = 0    # 가장 비싼길 하나만 끊으면 (마을내 최소비용의 길로만 구성된)두개의 마을로 분리가 가능하다
pq = []          # 우선순위큐를 구현할 리스트

def Find(x) :          # 부모노드를 찾는 함수
    if x == u_fnd_lst[x] :     # 자기자신이 부모노드라면 자기자신 반환
        return x
    else :
        u_fnd_lst[x] = Find(u_fnd_lst[x])    # 부모노드가 자기자신이 아니라면 재귀적으로 거슬러가면서 부모노드 탐색 및 경로압축
        return u_fnd_lst[x]

def Union(a, b) :    # 서로다른 집합(사이클이 존재하지 않는다)일 때 합연산(노드연결)
    a = Find(a)
    b = Find(b)
    if a != b :
        u_fnd_lst[b] = a   # 합연산하고자 하는 원소의 인덱스에 부모노드를 초기화한다

def Chk(a, b) :      # 서로 동일한 부모노드를 가지는지(사이클이 존재하는지) 판단
    p = Find(a)
    q = Find(b)
    if p == q :     # 부모노드가 동일할 때 참 반환(사이클이 존재할 때 참)
        return True
    return False

for _ in range(m) :
    a, b, c = map(int, input(). split())
    pq.append((c, a, b))  # 가중치정렬을 위해 가중치를 앞으로 해서 우선순위큐에 올린다

pq.sort(reverse = True)    # 우선순위큐 구현

while used_edge < n-1 :     # 노드의 개수가 n-1보다 작을때 반복
    c, a, b = pq.pop()      # 언패킹
    if not Chk(a, b) :      # 사이클이 존재하지 않을 때
        Union(a, b)         # 엣지 연결
        expensive = max(expensive, c)    # 연결이 될때마다 가장 비싼 비용인지를 비교하여 비싼 값 저장
        used_edge += 1       # 연결된 엣지 개수 1씩 증가
        ans += c            # 연결된 엣지의 가중치를 더한다

print(ans-expensive)    # 총 비용에서 가장 가중치가 큰 엣지를 제거하면 두개의 최소가중치합을 가진 집합으로 나뉘게된다 