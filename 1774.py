import sys
input = sys.stdin.readline
import math
import heapq

n, m = map(int, input(). split())
uflst = [i for i in range(n+1)]   # 유니온 파인드 리스트
pq = []                          # 우선순위 큐
god = [[0, 0]]             # 신들의 좌표를 저장할 리스트

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
    uflst[b] = uflst[a]

used_edge = 0    # 사용된 엣지의 수

for _ in range(n) :
    x, y = map(int, input(). split())
    god.append((x, y))     # 신들의 좌표정보를 저장

for _ in range(m) :
    g1, g2 = map(int, input(). split())    # 이미 연결된 통로를 입력받아
    if Find(g1) != Find(g2) :           # 두 신들간의 연결이 되어있지 않다면
        Union(g1, g2)            # 해당 통로를 직접 잇는 통료를 형성하고
        used_edge += 1           # 사용된 통로의 개수++

for i in range(1, n+1) :
    for j in range(i+1, n+1) :
        # 우선순위큐에 각 신들간의 거리를 기준으로하여 신의 번호와 함께 저장
        heapq.heappush(pq, (math.sqrt(abs(god[i][0]-god[j][0])**2 + abs(god[i][1]-god[j][1])**2), i, j))

ans = 0.0   

while used_edge < n-1 and pq:    # 사용된 통로의 개수가 n-1보다 작을때
    d, s, e = heapq.heappop(pq)   # 최소힙에서 꺼내온다
    if Find(s) != Find(e) :     #  두 신들간의 연결이 되어있지 않을때
        ans += d      # 거리를 더해나가고
        Union(s, e)   # 그 두 신들은 이어준다
        used_edge += 1

print('%.2f' %(ans))