import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

# 시간초과풀이
# def DFS(s, e, distance) :
#     global res
#     if s == e :
#         res = distance
#         return 
#     else :
#         for next, d in adjlst[s] :
#             if not visited[next] :
#                 visited[next] = True
#                 DFS(next, e, distance+d)
#                 visited[next] = False
    

# n = int(input())
# adjlst = [[] for _ in range(n+1)]
# leaf = [0]

# for _ in range(n-1) :
#     a, b, c = map(int, input(). split())
#     adjlst[a].append((b, c))
#     adjlst[b].append((a, c))

# for i in range(1, n+1) :
#     if len(adjlst[i]) == 1 :
#         leaf.append(i)

# ans = 0

# for i in range(1, len(leaf)-1) :
#     for j in range(i+1, len(leaf)) :
#         visited = [False] * (n+1)
#         res = 0
#         visited[leaf[i]] = True
#         DFS(leaf[i], leaf[j], 0)
#         ans = max(res, ans)

# print(ans)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++

# 아무 노드에서 DFS로 가장 먼 노드를 찾고 그 노드에서 가장 먼 노드를 찾으면 해당 거리가 지름

n = int(input())
adjlst = [[] for _ in range(n+1)]
visited = [-1] * (n+1)   # 노드까지의 거리를 저장하는 리스트

def DFS(start, dist) :   # 시작노드와 거리를 매개변수로 받는 DFS

    for next, d in adjlst[start] :  # 출발노드에서 갈 수 있는 노드와 거리
        if visited[next] == -1 :    # 만약 해당노드를 방문하지 않았다면
            visited[next] = dist + d    # 그 노드까지의 거리는 현재까지의 거리와 방금전 가중치를 더한 값
            DFS(next, dist+d)    # 방금도착한 노드를 출발노드, 방금까지 온 총 거리를 변수로 하여 재귀호출

for _ in range(n-1) :    # 양방향 
    a, b, c = map(int, input(). split())
    adjlst[a].append((b, c))
    adjlst[b].append((a, c))

visited[1] = 0   # 한 노드를 무작워로 잡아도 되지만 문제에서 1이 루트노드이므로 편의상 1에서 출발
DFS(1, 0)  # DFS호출(1에서 출발, 처음거리 0)

x = visited.index(max(visited))    # 1에서 출발했을 때에 최대거리를 가지는 인덱스번호가 1에서 가장 먼 노드이다
visited = [-1] * (n+1)       # 다시 거리를 저장하는 배열을 초기화해주고
visited[x] = 0     # 방금구한 1에서 가장 먼 노드를 x로 하여
DFS(x, 0)    # x노드에서 가장 먼 노드를 구하자

print(max(visited))    # 거리저장배열에서 가장 큰 값이 x에서 가장 먼 노드까지의 거리(=트리의 지름)