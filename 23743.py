import sys
import heapq

def Find(x) :   # 파인드
    if x == uflst[x] :
        return x
    else :
        uflst[x] = Find(uflst[x])
        return uflst[x]
    

def Union(a, b) :  # 유니온
    a = Find(a)
    b = Find(b)

    if a != b :
        uflst[max(a, b)] = min(a, b)


n, m = map(int, input(). split())
uflst = [i for i in range(n+1)]
edge = []   # 방들간 워프장치의 설치정보 저장 리스트

for _ in range(m) :
    a, b, c = map(int, input(). split())   
    heapq.heappush(edge, (c, a, b))   # 워프장비 설치소요시간을 가중치로 하는 엣지로 간주하여 시간을 기준으로 하여 우선순위큐에 저장

exitwarp = [0] + list(map(int, input(). rstrip(). split()))   # 바로탈출가능한 워프장치의 방별 설치소요시간

for i in range(1, n+1) :   # 바로탈출가능한 워프장치의 경우 0번방으로 워프한다고 간주
    heapq.heappush(edge, (exitwarp[i], 0, i))

time = 0  # 소요시간
while edge :
    now, r1, r2 = heapq.heappop(edge)  

    if Find(r1) != Find(r2) :  # 두 방이 아직 연결되지 않았다면
        Union(r1, r2)  # 두 방을 연결하고
        time += now   # 워프장치를 설치한다

print(time)