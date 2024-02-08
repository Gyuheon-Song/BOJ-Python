import sys
input = sys.stdin.readline

n, m, t = map(int, input(). split())
uflst = [i for i in range(n+1)]    # 유니온 파인드 리스트
pq = []
used_edge = 0
ans = 0
road = 0     # 도시를 정복할때마다 증가할 도로이용비용

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

for _ in range(m) :
    a, b, c = map(int, input(). split())
    pq.append((c, a, b))

pq.sort(reverse = True)

while used_edge < n-1 :     
    cost, a, b = pq.pop()
    if Find(a) != Find(b) :     # 도로를 연결할때마다
        Union(a, b)
        ans += cost + t*used_edge     # 정복비용 + 도로이용비용을  정답에 더해나간다
        used_edge += 1                # 도시를 한번 정복할때마다 도로이용비용이 t만큼 증가
                                
print(ans)