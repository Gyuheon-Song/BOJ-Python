import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input(). split())
adjlst = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
semester = [1] * (n+1)   # 과목을 들을 수 있는 학기를 저장하는 리스트

def Topo_sort(n) :   # 위상정렬
    q = deque()

    for i in range(1, n+1) :    # 진입차수가 0인 과목들을 큐에 넣는다 == 1학기에 들을 수 있다
        if indegree[i] == 0 :
            q.append(i)            

    while q :    
        now = q.popleft()     # 선수과목들을 꺼내고 그 다음에 들을 수 있는 과목들을 탐색한다
        for next in adjlst[now] :
            indegree[next] -= 1   #진입차수 하나씩 감소
            # 선수과목이 있는 과목은 방금꺼낸 선수과목의 학기의 다음 학기부터 들을 수 있으므로 현재학기+1 과 해당과목에 이미 저장되어 있는 학기값 중 큰 값을 저장한다
            semester[next] = max(semester[next], semester[now] + 1)
            if indegree[next] == 0 :    # 진입차수가 0이면 큐에 올린다
                q.append(next) 

for _ in range(m) :
    a, b = map(int, input(). split())
    adjlst[a].append(b)
    indegree[b] += 1

Topo_sort(n)

print(*semester[1:])