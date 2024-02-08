import sys
input = sys.stdin.readline

n = int(input())
tree = list(map(int, input(). split()))
k = int(input())

def DFS(del_node) :    # 지우는 노드를 매개변수로 받아 DFS
    tree[del_node] = -2   # 지워야 하는 노드를 전부 -2로 표시할 것이다
    # 부모노드가 들어있는 트리를 탐색
    for i in range(n) :
        # 만약 부모노드르가 지워지는 자식노드라면
        if tree[i] == del_node :
            DFS(i)   # 자식노드도 지워야하므로 자식노드를 매개변수로 하여 DFS

DFS(k)
# DFS를 돌리게 되면 지워야하는 노드들은 -2로 표시되었을 것이다

cnt = 0
# 모든 노드번호들에 대해서 탐색
for i in range(n) :
    # 만약 지워지지 않는 노드이며 그 노드가 누군가의 부모노드가 아니라면 리프노드이다
    if tree[i] != -2 and i not in tree :
        cnt += 1

print(cnt)
