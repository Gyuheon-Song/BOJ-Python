import sys
import math
input = sys.stdin.readline

n = int(input()) 
uflst = [i for i in range(n+1)]
pq = []
stars = [[0, 0]]     # 별들의 좌표를 저장할 리스트
ans = 0
used_edge = 0     # 사용된 간선의 개수를 저장할 리스트 

def Find(x) :  # 부모노드를 찾기
    if x == uflst[x] :
        return x
    else :
        uflst[x] = Find(uflst[x])
        return uflst[x]

def Union(a, b) :   # 두 별을 연결하고 부모노드 합연산
    a = Find(a)
    b = Find(b)
    if a < b :
        uflst[b] = a
    else :
        uflst[a] = b

for _ in range(n) :      # 별들의 좌표 입력받아 리스트에 저장
    stars.append(list(map(float, input(). split())))

for i in range(1, n+1) :
    for j in range(i+1, n+1) :
        # 우선순위 큐에 두 별간 거리를 기준으로 하여 저장
        pq.append((math.sqrt((stars[i][0]-stars[j][0])**2 + (stars[i][1]-stars[j][1])**2), i, j))

pq.sort(reverse = True)   # 우선순위 큐 구현

while used_edge < n-1 :   
    d, s, e = pq.pop()
    if Find(s) != Find(e) :
        Union(s, e)
        used_edge += 1
        ans += d

print(round(ans, 2))