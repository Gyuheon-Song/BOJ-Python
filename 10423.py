import sys
input = sys.stdin.readline

n, m, k = map(int, input(). split())
power = list(map(int, input(). split()))     # 발전소 입력받기 
uflst = [i for i in range(n+1)]    # 유니온파인드 리스트
pq = []    # 우선순위 큐
ans = 0

for i in range(1, n+1) :    # 발전소가 있는 도시의 부모노드는 모두 0으로 한다
    if i in power :         # 발전소가 있는 도시들이 이미 서로 연결되어있다고 가정하고 풀자
        uflst[i] = 0        # 부모노드가 0인 것을 함수로 확인했을때 서로 연결되지 않도록

def Find(x) :    # 부모노드 찾기
    if x == uflst[x] :
        return x
    else :
        uflst[x] = Find(uflst[x])
        return uflst[x]

def Union(a, b) :   # 항상 번호가 작은 도시가 부모노드가 될 수 있게 집합의 합연산을 한다
    a = Find(a)     # 그래야 발전소와 연결되었을 때 부모노드가 0이게 된다
    b = Find(b)
    if a < b :
        uflst[b] = a
    else :
        uflst[a] = b

for _ in range(m) :
    u, v, w = map(int, input(). split())
    pq.append((w, u, v))

pq.sort(reverse = True)

while pq :
    cost, s, e = pq.pop() 
    if Find(s) != Find(e) :    # 부모노드가 0(발전소와이어진)이 아닌 도시들만 연결
        Union(s, e)
        ans += cost

print(ans)
