from collections import deque
import sys
input = sys.stdin.readline

n = int(input())   # 트리의 정점의 수 입력
tree = [[] for _ in range(n+1)]    #  트리에서의 정저간 연결정보를 인접리스트의 형태로 저장
level = [0] * (n+1)    # 노드별 트리에서의 깊이를 저장할 리스트
parent = [0] * (n+1)   # 노드별 부모노드를 저장할 리스트
visited = [False] * (n+1)    # 방문배열

for _ in range(n-1) :     # 트리에서의 정점간 연결정보를 인접리스트에 양방향 저장
    s, e = map(int, input(). split())
    tree[s].append(e)
    tree[e].append(s)

def BFS(root, depth) :   # BFS로 정점별 깊이를 계산
    q = deque([(root, depth)])   # 큐에 루트와 루트의 깊이를 입력

    while q :
        [parent_node, lv] = q.popleft()   # 큐에서 뺀 두 변수가 정점과 깊이이다
        visited[parent_node] = True    # 부모노드를 방문한 것으로 표시
        level[parent_node] = lv      # 부모노드의 깊이를 저장

        for child in tree[parent_node] :  # 부모노드와 이어져있는 자식노드를 탐색
            if not visited[child] :       # 자식노드를 아직 방문하지 않았다면
                parent[child] = parent_node      # 자식노드에 대한 부모노드를 부모노드 리스트에 저장
                q.append((child, lv+1))     # 자식노드와, 깊이에 1을 더한 값을 큐에 넣어준다
    
def LCA(a, b) :    # 최소공통조상 찾기
    while level[a] != level[b] :     # a와 b의 깊이가 다른 경우에 탐색한다
        if level[a] > level[b] :     # a가 b보다 더 트리의 밑에 있을때
            a = parent[a]            # a를 a의 부모노드값으로 초기화(깊이가 더 얕아진다 = 트리의 윗조상으로 올라간다)
        else :                       # b가 a보다 더 트리의 밑에 있을 때
            b = parent[b]            # b를 b의 부모노드값으로 초기화
    
    while a != b :                 # 위의 연산을 한 이후 a와 b의 각각에서 서로 깊이가 같은 부모노드가 결정되었을 것이다
                                   # 그럼에도 그 깊이가 같은 노드가 같지 않다면 
        a = parent[a]              # 하나 더 올라가면 a와 b의 공통조상일 것이다
        b = parent[b]
    
    return a

BFS(1, 1)

m = int(input())
for _ in range(m) :
    a, b = map(int, input(). split())
    print(LCA(a, b))