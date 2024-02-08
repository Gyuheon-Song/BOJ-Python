import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
adjlst = [[] for _ in range(n+2)]  # 사이클을 없애주기 위해 배열의 크기를 n+2로 할당
indegree = [0] * (n+2)
score = [0] * (n+2)
path = [1]   # 지나온 노드를 저장할 배열
prev = [[] for _ in range(n+2)]   # 이전 노드를 저장할 배열
visited = [False] * (n+2)   # 중복방지 방문배열

for _ in range(m) :
    a, b, c = map(int, input(). split())
    if b != 1 :    # 만약 도착점이 1이 아니면 그냥 저장
        adjlst[a].append((b, c))
        indegree[b] += 1
    else :   # 도착점이 1일때는 사이클이 만들어지므로 n+1 노드로 도착점을 바꾸어준다
        adjlst[a].append((n+1, c))
        indegree[n+1] += 1

def Topo_sort() :   # 위상정렬 알고리즘
    q = deque([1])   # 1번 노드에서 시작
    
    while q :
        now = q.popleft()

        for next, t in adjlst[now] :
            indegree[next] -= 1
            if score[next] <= score[now] + t :
                score[next] = score[now] + t  
                if not visited[next] :    # 아직 방문하지 않은 노드라면 해당노드의 이전노드와 점수를 저장
                    prev[next].append((now, t))
            if indegree[next] == 0 :
                q.append(next)
                visited[next] = True

def Path(k) :   # 경로를 거슬러가며 찾는 함수
    q = deque([k])

    while q :
        now = q.popleft()

        for before, point in prev[now] :   # 이전노드 배열에서 이전노드와 점수를 언패킹
            if score[before] == score[now] - point :   # 현재노드까지의 경로에 이전노드로부터의 경로가 포함되어있다면
                path.append(before)   # 이전노드를 지나온 것이므로 경로배열에 저장
                q.append(before)   # 이전노드를 큐에넣어 전전 노드를 찾자

Topo_sort()   # 위상정렬
Path(n+1)   # 1로 돌아오는 엣지들의 도착점을 1이 아닌 n+1번 노드로 바꾸어줬기에 n+1번 노드에서 역추적을 한다

print(score[n+1])   # n+1번 노드까지의 점수
print(*path[::-1])   # 역추적 경로를 뒤집으면 정답
