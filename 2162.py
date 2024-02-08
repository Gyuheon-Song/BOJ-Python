import sys
input = sys.stdin.readline

def CCW(x1, y1, x2, y2, x3, y3) :    # 1-2선분과 1-3선분의 외적
    res = (x2-x1) * (y3-y1) - (x3-x1) * (y2-y1)  # 외적
    if res > 0 :   # 외적값이 양수이면 시계방향, 1 반환
        return 1
    elif res < 0 :    # 외적값이 음수이면 반시계, -1 반환
        return -1
    else :      # 외적값이 0이면 같은 직선에 위치, 0 반환
        return 0


def CHK(x1, y1, x2, y2, x3, y3, x4, y4) :   # 선분교차판정
    # 1-2선분과 1-3  // 1-2선분과 1-4 의 외적값 중 하나라도 0 이거나 그리고 3-4선분과 3-1  // 3-4선분과 3-2 의 외적값 중 하나라도 0 이면 같은 직선에 한 점이 존재 무조건 존재
    if CCW(x1, y1, x2, y2, x3, y3) * CCW(x1, y1, x2, y2, x4, y4) == 0 and CCW(x3, y3, x4, y4, x1, y1) * CCW(x3, y3, x4, y4, x2, y2) == 0 :
        # 만약 선분의 양 끝점이 다른 선분과 교차할 수 밖에 없는 위치이면 1 반환 
        if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2) :
            return 1
        # 두 점이 한 선분의 반대편에 있거나 한 선분 위에 존재한다면 1 반환
    elif CCW(x1, y1, x2, y2, x3, y3) * CCW(x1, y1, x2, y2, x4, y4) <= 0 and CCW(x3, y3, x4, y4, x1, y1) * CCW(x3, y3, x4, y4, x2, y2) <= 0 :
        return 1
    
    return 0

n = int(input())
lst = [[]]
uflst = [-1 for _ in range(n+1)]   # 유니온 파인드용 리스트이지만 -1로 초기화해놓는다

for _ in range(n) :
    lst.append(list(map(int, input(). split())))  

def Find(x) :
    # 그룹의 대표원소인 경우에 대표원소를 반환
    if uflst[x] < 0 :
        return x
    # 계속 그룹의 대표선분을 찾아가며 경로압축
    else :
        k = Find(uflst[x])
        uflst[x] = k
        return k

# 유니온 함수
def Union(a, b) :
    a = Find(a)
    b = Find(b)
    if a == b :   # 두 선분의 그룹이 같으면 리턴
        return
    # 음수의 형식으로 더 큰 그룹에 원소의 개수를 하나 추가하고 방금 추가된 원소에는 큰 그룹의 번호를 초기화한다
    elif uflst[a] < uflst[b] :
        uflst[a] += uflst[b]
        uflst[b] = a
    else :
        uflst[b] += uflst[a]
        uflst[a] = b

# 선분교차판정을 총해 그룹 형성
for i in range(1, n) :
    for j in range(i+1, n+1) :
        x1, y1, x2, y2 = lst[i]
        x3, y3, x4, y4 = lst[j]
        if CHK(x1, y1, x2, y2, x3, y3, x4, y4) :
            Union(i, j)

group = 0
biggest = 0

for i in range(1, n+1) :
    # 음수인 경우는 해당 선분이 대표선분이며 그 절댓값이 그룹의 크기를 나타낸다
    if uflst[i] < 0 :
        group += 1    # 대표선분의 개수 == 그룹의 수
        biggest = max(biggest, abs(uflst[i]))

print(group)
print(biggest)