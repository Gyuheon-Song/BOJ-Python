import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

g = int(input().rstrip())   # 게이트의 수를 입력받는다
p = int(input().rstrip())   # 비행기의 수를 입력받는다
gate = [i for i in range(g+1)]    # 파인드리스트
plane = []    # 들어오는 비행기 순서에 따라 저장할 비행기리스트
cnt = 0    # 도킹할 수 있는 비행기의 수

def Find_gate(x) :    # 비행기를 도킹시킬 게이트를 찾는 함수
    if x == gate[x] :     # 만약 게이트가 비어있다면 거기에 도킹
        return x
    gate[x] = Find_gate(gate[x])   # 자기 게이트 번호가 아니라면, 해당 게이트는 이미 사용되었으므로 다른게이트 찾기
    return gate[x]   # 최종적으로 도킹가능한 게이트 반환


def Union(a, b) :    # 두 도킹 게이트를 받았을 때 두 게이트에 대해
    a = Find_gate(a)    # 최종적으로 도킹가능한 게이트 찾기
    b = Find_gate(b)    
    gate[max(a, b)] = min(a, b)   # 큰 번호의 게이트에 도킹을 하고 다음 비행기를 위해, 작은 번호의 게이트로의 안내표지 저장


for _ in range(p) :   # 비행기 리스트에 입력받아 저장
    plane.append(int(input().rstrip()))

for i in plane :   # 비행기들은 각자 도킹할 수 있는 최대번호의 게이트번호를 가지고 공항에 들어온다
    dock = Find_gate(i) # 따라서 최종 도킹할 수 있는 게이트를 그 번호로 찾는다
    if dock == 0 :   # 도킹할 수 있는 게이트를 찾아가다가 만약 0번 게이트가 나오면 더이상 도킹할 수 있는
        break        # 게이트가 없다는 뜻이므로 중단
    else :     # 도킹할 수 있는 곳이 있다면
        Union(dock, dock-1)   # 도킹가능 게이트와 그 게이트에 저장할 안내표지로 1작은 게이트를 설정 
        cnt += 1

print(cnt)



