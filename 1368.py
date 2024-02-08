import sys
import heapq
input = sys.stdin.readline


def Find(x) :    # 파인드
    if x == uflst[x] :
        return x
    else :
        uflst[x] = Find(uflst[x])
        return uflst[x]
    

def Union(a, b) :   # 유니온

    a = Find(a)
    b = Find(b)

    if a != b :   # 두 논이 다른 집합인 경우
        uflst[max(a, b)] = min(a, b)    # 합연산
        return True  # 참 반환
    else :
        return False  # 거짓 반환
    

n = int(input())
uflst = [i for i in range(n+1)]
edge = []

for i in range(1, n+1) :
    heapq.heappush(edge, (int(input()), 0, i))   # 직접 우물을 파는 것을 0번 논과 연결되있는것으로 생각

paddy = [list(map(int, input(). split())) for _ in range(n)]  # 논 입력받는다

for i in range(n) :
    for j in range(n) :
        if i == j :  
            continue
        heapq.heappush(edge, (paddy[i][j], i+1, j+1))   # 가중치를 기준으로하여 우선순위큐에 저장,  논의 번호는 인덱스보다 1 크다
cost = 0

while edge :
    cur, s, e = heapq.heappop(edge)   # 우선순위큐에서 꺼내서
    if Union(s, e) :   # 만약 이미 같은 집합이면 연산 X, 다른 집합일 경우 병합하고 가중치를 더해나간다
        cost += cur

print(cost)







