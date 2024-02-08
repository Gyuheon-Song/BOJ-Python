import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
u_fnd_lst = [i for i in range(n+1)]  # 유니온 파인드리스트
pq = []    # 우선순위큐를 구현할 리스트
ans = 0    # 정답변수
used_edge = 0     # 사용된 엣지수를 저장할 변수

for _ in range(m) :
    a, b, c = map(int, input(). split())    # 컴퓨터와 비용 입력받는다
    pq.append((c, a, b))     # 가중치 기준 정렬을 위해 가중치를 가장 앞으로 하여 우선순위큐에 저장

pq.sort(reverse = True)    # 우선순위큐 구현을 위해 리스트 역정렬

def Find(x) :        # 부모노드 찾기
    if x == u_fnd_lst[x] :    # 자기자신이 부모노드이면 자기자신 반환
        return x
    else :
        u_fnd_lst[x] = Find(u_fnd_lst[x])   # 부모노드가 자기자신이 아니면 부모노드를 재귀적으로 찾아올라간다
        return u_fnd_lst[x]   # 부모노드를 찾아 반환
    
def Union(a, b) :    # 사이클이 발생하지 않을 때 연결하는 집합의 합연산
    a = Find(a)
    b = Find(b)
    if a != b :      # 부모노드가 다를 경우(사이클이 발생하지 않는 경우)
        u_fnd_lst[b] = a      # 두 컴퓨터를 연결(부모노드를 넣어준다)

def Chk(a, b) :      # 부모노드가 동일한지(사이클이 발생하는지) 판단하는 함수
    p = Find(a)
    q = Find(b)
    if p == q :
        return True
    return False

while used_edge < n-1 :     # 연결한 엣지의 수가 n-1보다 작을때 반복
    c, a, b = pq.pop()      # 우선순위큐에서 빼서 언패킹
    if not Chk(a, b) :      # 부모노드가 동일하지 않을 경우(사이클이 발생하지 않을 경우)
        Union(a, b)         # 두 노드를 연결한다(엣지를 사용하여 연결)
        used_edge += 1      # 사용한 엣지의 개수 하나씩 증가
        ans += c            # 해당엣지의 가중치를 정답변수에 더하여 초기화

print(ans)