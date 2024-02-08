import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input(). split())
uflst = [i for i in range(n+1)]    # 유니온 파인드 리스트
pq = []     # 우선순위큐
used_edge = 0
cost = 0    # 최소 도로설치비용
total = 0   # 모든 도로를 다 설치할 시 소모되는 비용

def Find(x) :
    if x == uflst[x] :
        return x
    else :
        uflst[x] = Find(uflst[x])
        return uflst[x]

def Union(a, b) :
    a = Find(a)
    b = Find(b)
    if a == b :
        return
    uflst[max(a, b)] = min(a, b)

for _ in range(m) :
    a, b, c = map(int, input(). split())
    heapq.heappush(pq, (c, a, b))    # 우선순위큐에 도로정보를 비용을 기준으로 하여 저장
    total += c   # 모든 도로에 대한 비용을 계산

while used_edge < n-1 and pq:     # 사용된 도로가 최소개수인 n-1개보다 적거나 큐에 연결할 수 있는 도로정보가 남아있을때
    pay, s, e = heapq.heappop(pq)   # 최소힙에서 도로정보를 빼온다
    if Find(s) != Find(e) :     # 두 건물이 연결되지 않은 관계일 때
        Union(s, e)      # 두 건물을 연결한다
        cost += pay      # 최소연결비용을 계산하기 위함
        used_edge += 1   # 사용된 도로의 개수도 세어준다

if used_edge == n-1 :     # 와일문을 돌렸을 때 연결된 도로의 개수가 최소도로개수인 n-1개일 때
    print(total-cost)     # 최소비용으로 모든 건물을 연결한 것이므로 절약비용을 계산
else :        # 와일문을 다 돌렸음에도(모든 도로의 정보를 다 고려했음에도) 연결도로의 개수가 n-1개가 아닐때
    print(-1)    # 모든 건물이 연결되지 못했다

