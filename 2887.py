import sys
input = sys.stdin.readline
import heapq

n = int(input())
uflst = [i for i in range(n+1)]   
pq = []
ans = 0
used_edge = 0
planets = []    # 행성의 좌표와 번호를 저장할 리스트

def Find(x) :
    if x == uflst[x] :
        return x
    else :
        uflst[x] = Find(uflst[x])
        return uflst[x]

def Union(a, b) :
    a = Find(a)
    b = Find(b)
    if a < b :
        uflst[b] = a
    else :
        uflst[a] = b

for i in range(1, n+1) :   # 행성의 좌표를 입력받아 리스트에 저장
    x, y, z = map(int, input(). split())
    planets.append((x, y, z, i))

# 모든 간선을 탐색할시 O(N^2)이므로 각 축좌표에 대한 정렬을 하여
# 우선순위큐에 넣어 가장 짧은 3N개의 간선으로 연산을 실행하자

dx = [0] + sorted(planets, key = lambda x : x[0])    # x좌표에 대해 정렬
dy = [0] + sorted(planets, key = lambda x : x[1])    # y좌표에 대해 정렬
dz = [0] + sorted(planets, key = lambda x : x[2])    # z좌표에 대해 정렬

for i in range(1, n) :
    # 각 축 value에 대해 서로 가까운 순위로 위에서 정렬을 시행했으므로
    # 정렬된 순서에 대하여 연달아 정렬된 행성들간의 축좌표별 거리를 우선순위 큐에 넣는다
    heapq.heappush(pq, (abs(dx[i][0]-dx[i+1][0]), dx[i][3], dx[i+1][3]))
    heapq.heappush(pq, (abs(dy[i][1]-dy[i+1][1]), dy[i][3], dy[i+1][3]))
    heapq.heappush(pq, (abs(dz[i][2]-dz[i+1][2]), dz[i][3], dz[i+1][3]))

# 위의 과정에서 각 축간의 거리가 최소인 행성들의 세트가 우선순위 큐에 들어가게 된다
# 따라서 하나씩 뽑을 경우 어떠한 두 행성의 x, y, z축별 좌표간 거리중 가장 작은 것부터 나오고 
# 그 두 행성을 연결하며 유니온파인드 알고리즘을 실행하면 된다
# 이러면 어떤 한 축에 대해 연결된 두 행성에 대해, 알고리즘 실행 중에 다른 축좌표간 거리가 pop되었을때
# 유니온 파인드 알고리즘에 의해 걸러지게 된다
# 이렇게 하여 가장 축좌표간 차가 작은 세트가 나오면 그 세트의 다른 축좌표간 값을 거를 수 있다

while used_edge < n-1 :
    d, s, e = heapq.heappop(pq)
    if Find(s) != Find(e) :
        Union(s, e)
        used_edge += 1
        ans += d

print(ans)

