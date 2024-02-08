import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, m = map(int, input(). split())

lst = [i for i in range(n+1)]    # 유니온 파인드 리스트

def Union(a, b) :     # 합집합 연산
    a = Find(a)       # 인덱스를 원소로 하며, 같은 집합에 속할 때 대표 원소 하나를 해당 집합
    b = Find(b)       # 내의 원소 인덱스에 저장한다
    if a != b :
        lst[b] = a

def Find(x) :    # 자기 자신이 저장되어 있으면 원소 하나인 부분집합
                 # 다른 원소가 자기 인덱스에 저장되었으면 그 원소와 같은 집합
    if x == lst[x] :      # 만약 어느 집합에도 속해있지 않다면 자기 자신을 반환(원소가 하나인 집합)
        return x
    else :
        lst[x] = Find(lst[x])  # 경로압축 중요  
        # 다른 원소와 같은 집합에 속해있으면 해당 집합의 대표원소를 찾는다
        return lst[x]

def Chk(a, b) :
    a = Find(a)   
    b = Find(b)
    if a == b :      # 두 원소들이 속해있는 집합의 대표원소들이 같다면 두 원소는 같은 집합에 속해있다
        return True
    return False

for _ in range(m) :
    com, a, b = map(int, input(). split())

    if com == 0 :
        Union(a, b)

    else :
        if Chk(a, b) :
            print("YES")
        else :
            print("NO")