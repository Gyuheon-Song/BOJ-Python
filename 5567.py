import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())
graph = [[0] * (n+1) for _ in range(n+1)]   # 친구관계를 저장할 인접리스트
visited = [0 for _ in range(n+1)]      # 친구관계의 정도를 저장할 배열

for i in range(m):              # 양방향 친구관계를 인접리스트에 저장
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(x):     # BFS
    q = deque()
    visited[x] = 1
    q.append(x)
    while q:
        a = q.popleft()    
        for i in graph[a]:    # a의 친구이며
            if visited[i] == 0:   # 친구관계를 아직 세지 않았다면
                q.append(i)    # 큐에 넣어 탐색을 추가로 돌린다
                visited[i] = visited[a] + 1  # 친구관계가 하나 건너이므로 1을 더한다

bfs(1)
result = 0
for i in range(2,n+1):
    if visited[i] < 4 and visited[i] != 0:    # 친구의 친구라면 친구관계가 3, 친구라면 관계는 2 이므로
        result += 1           # 친구관계 수치가 4보다 작은 것만 센다
print(result)