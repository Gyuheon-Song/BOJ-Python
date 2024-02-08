import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
city = [[0]*(n+1)]    # 도시간 연결정보르 담는 인접행렬
uflst = [i for i in range(n+1)]    # 유니온 파인드 리스

def Find(x) :     # 부모노드 찾는 함수
    if x == uflst[x] :
        return x
    else :
        uflst[x] = Find(uflst[x])
        return uflst[x]

def Union(a, b) :     # 부모노드가 같을 때 작은 부모노드로 통합(합집합)
    a = Find(a)
    b = Find(b)
    if a < b :
        uflst[b] = a
    else :
        uflst[a] = b

for _ in range(n) :
    city.append([0] + list(map(int, input(). split())))

travel = list(map(int, input(). split()))   # 여행해야하는 도시(연결되어있는지 확인해야하는 도시들의 리스트)

for i in range(1, n+1) :
    for j in range(i, n+1) :
        if city[i][j] == 1 :   # 연결정보를 받아 유니온 연산
            Union(i, j)

ans = True  # 여행가능여부

for i in range(0, m-1) :
    if Find(travel[i]) == Find(travel[i+1]) :   # 여행해야하는 도시들의 부모노드 비교
        continue   # 부모노드가 같은 경우 계속진행
    else :   # 부모노드가 다를 경우
        ans = False   # 여행불가
        break

if ans :
    print("YES")
else :
    print("NO")
