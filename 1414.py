import heapq
import sys
input = sys.stdin.readline


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


n = int(input())

length = {chr(i) : i-96 for i in range(97, 123)}  # 소문자에 대응하는 길이
length.update({chr(i) : i-38 for i in range(65, 91)})  # 대문자에 대응하는 길이
room = []  # 랜선연결정보를 저장하는 리스트
uflst = [i for i in range(n)]  # 유니온 파인드 리스트
edge = []   # MST를 위한 간선의 정보를 담을 우선순위 큐

for _ in range(n) :
    room.append(list(input(). rstrip()))

total = 0   # 존재하는 총 랜선의 길이합
for i in range(n) :
    for j in range(n) :
        if room[i][j] in length.keys() :   # 딕셔너리에 존재하는 문자라면
            room[i][j] = length[room[i][j]]   # 해당 키값에 해당하는 길이로 초기화
            total += room[i][j]   # 해당 랜선의 길이 총 길이에 더해준다
        else :
            room[i][j] = 0   # 딕셔너리에 없는 문자일 경우 랜선이 없으므로 0으로 표지

for i in range(n) :
    for j in range(n) :
        if i == j or room[i][j] == 0 :   # 자기자신과 연결된 랜선이거나 랜선이 없는 경우
            continue  # 건너뛴다

        heapq.heappush(edge, (room[i][j], i, j))   # 다른 컴퓨터와 연결되어있을 경우 그 길이를 기준으로 하여 우선순위큐에 저장

use = 0   # 사용한 랜선의 길이
while edge :
    now, s, e = heapq.heappop(edge)   # 우선순위큐에서 짧은 랜선순으로 꺼낸다

    if Find(s) != Find(e) :   # 두 컴퓨터가 이어져있지 않은 상태라면
        Union(s, e)   # 랜선을 사용하여 두 컴터 연결
        use += now   # 연결한 랜선의 길이 더해나간다

for i in range(n) :   # 모든 컴퓨터의 부모노드를 각 집합의 대표컴터 하나로 통일시키기 위함
    uflst[i] = Find(i)

if len(set(uflst)) == 1 :   # 만약 모두가 연결되어 부모 컴퓨터가 1개라면
    print(total-use)   # 총 랜선에서 사용한 랜선길이를 뺀 길이만큼 기부가능
else :   # 부모 컴터가 여러개이면 모든 컴퓨터가 다 연결되지 않은 상태이므로
    print(-1)   # -1 



