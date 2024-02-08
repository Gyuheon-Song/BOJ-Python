import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input(). split())
adjlst = [[] for _ in range(n+1)]
indegree = [0] * (n+1)    # 진입차수
problem = []   # 문제를 풀 순서를 저장하는 리스트

def Topo_sort(n) :   # 위상정렬
    q = []

    for i in range(1, n+1) :  # 진입차수가 0인 문제를 먼저 최소힙에 넣어준다(같은 우선순위라면 번호가 작은(쉬운)문제를 먼저 풀기 위함)
        if indegree[i] == 0 :
            heapq.heappush(q, i)
    
    while q :
        pb_now = heapq.heappop(q)   # 최소힙에서 먼저 풀 문제를 꺼내주고
        problem.append(pb_now)      # 그 문제를 리스트에 저장
        for pb_next in adjlst[pb_now] :    # 다음에 풀어야 좋은 문제들의 진입차수를 1씩 감소시키고
            indegree[pb_next] -= 1
            if indegree[pb_next] == 0 :    # 진입차수가 0이 된 문제들을 최소힙에 저장한다
                heapq.heappush(q, pb_next)

for _ in range(m) :
    a, b = map(int, input(). split())
    adjlst[a].append(b)
    indegree[b] += 1

Topo_sort(n)  # 위상정렬
print(*problem)   # 먼저 풀어야 좋은 문제들을 푸는데 그 주에서도 난이도가 쉬운 문제를 먼저 푸는 순서로 정렬되어있다.