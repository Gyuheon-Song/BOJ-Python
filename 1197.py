# 최소 스패닝 트리(MST) : 크루스칼, 프림
# 에지리스트와 유니온파인드리스트 초기설정
# 에지리스트를 가중치 기준으로 오름차순 정렬
# 가중치가 낮은 에지부터 연결시도 -> 사이클이 유무 체크
# 노드의 개수가 n개일 때 연결한 노드의 개수가 n-1이 될 때까지 에지연결시도 반복

import sys
input = sys.stdin.readline
pq = []    # 우선순위큐 외장함수를 호출하면 시간초과 발생
 
v, e = map(int, input(). split())
u_fnd_lst = [i for i in range(v+1)]   # 부모노드를 저장할 유니온파인드 리스트

for _ in range(e) :
    a, b, c = map(int, input(). split())
    pq.append((c, a, b))     # 가중치를 기준으로 우선순위큐에서 노드정렬을 원하므로 가중치가 앞에오게 넣는다

def Union(a, b) :
    a = Find(a)
    b = Find(b)
    if a != b :
        u_fnd_lst[b] = a

def Find(x) :
    if x == u_fnd_lst[x] :
        return x
    else :
        u_fnd_lst[x] = Find(u_fnd_lst[x])
        return u_fnd_lst[x] 

used_edge = 0
ans = 0
pq.sort(reverse=True)    # 우선순위큐를 리스트로 구현

while used_edge < v-1 :   # 연결한 엣지의 개수가 n-1보다 작을때 반복해서 찾기
    c, a, b = pq.pop()    # 우선순위큐에서 언패킹하여 받아오고
    if Find(a) != Find(b) :    # 두 노드가 부모노드(집합)가 다를 때 == 사이클이 존재하지 않을때
        Union(a, b)       # 두 노드를 연결시킨다
        ans += c          # 정답에 가중치를 더해나간다
        used_edge += 1    # 사용된 엣지의 개수가 하나씩 증가한다

print(ans)
        