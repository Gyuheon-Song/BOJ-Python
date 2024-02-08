import sys
input = sys.stdin.readline

def Find(x) :         # 부모노드 찾는 함수
    if x == u_fnd_lst[x] :
        return x
    else :
        u_fnd_lst[x] = Find(u_fnd_lst[x])
        return u_fnd_lst[x]
    
def Union(a, b) :    # 합집합연산
    a = Find(a)
    b = Find(b)
    u_fnd_lst[b] = a

n, m = map(int, input(). split())
gender = [0] + list(map(str, input(). split()))  # 학교별 성별을 저장하는 리스트
u_fnd_lst = [i for i in range(n+1)]    # 유니온 파인드용 리스트
pq = []   # 우선순위큐
used_edge = 0   # 사용된 엣지의 수 저장 변수
ans = 0     

for _ in range(m) :
    a, b, c = map(int, input(). split())  # 학교정보와 가중치를 입력받는다
    if gender[a] != gender[b] :     # 그러나 성별이 같은 두 학교를 잇는 엣지의 경우는 무시하고
        pq.append((c, a, b))    # 서로 다른 성별의 학교를 잇는 엣지만 가중치 기준으로 우선순위큐에 저장

pq.sort(reverse = True)    # 우선순위 큐 구현

while used_edge < n-1 and pq :    # 사용된 엣지가 n-1개보다 작으면서 우선순위큐에 남은 길이 있을 때 반복
    cost, s, e = pq.pop()   # 우선순위큐에서 언패킹
    if Find(s) != Find(e) :   # 두 학교를 연결했을 때 사이클이 생기지 않을 때
        Union(s, e)     # 두 학교를 연결(합집합)
        used_edge += 1  # 사용된 엣지++
        ans += cost    # 해당 엣지의 가중치를 더해나간다

if used_edge == n-1 :    # 학교간 연결을 n-1개의 엣지를 사용하여 연결했을 때 모든학교가 연결되어있다
    print(ans)
else :    # 엣지의 개수가 n-1개가 안될 때 모든 학교는 연결되지 못했다
    print(-1)