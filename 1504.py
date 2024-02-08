import sys
import heapq
input = sys.stdin.readline

n, e = map(int, input(). split())
adjlst = [[] for _ in range(n+1)]

for _ in range(e) :
    u, v, d = map(int, input(). split())
    adjlst[u].append((v, d))
    adjlst[v].append((u, d))

node1, node2 = map(int, input(). split())

def Dajikstra(depart, arrive) :
    INT = int(10e9)
    distance = [INT] * (n+1)
    hq = []

    heapq.heappush(hq, (0, depart))
    distance[depart] = 0

    while hq :
        now = heapq.heappop(hq)
        now_node = now[1]
        if distance[now_node] < now[0] :
            continue
        for temp in adjlst[now_node] :
            next_node = temp[0]
            dist = temp[1]
            if distance[next_node] > distance[now_node] + dist :
                distance[next_node] = distance[now_node] + dist
                heapq.heappush(hq, (distance[next_node], next_node))
    return distance[arrive]

# 경로 1 -> node1 -> node2 -> n
path1 = Dajikstra(1, node1) + Dajikstra(node1, node2) + Dajikstra(node2, n)
# 경로 2 -> node2 -> node1 -> n
path2 = Dajikstra(1, node2) + Dajikstra(node2, node1) + Dajikstra(node1, n)

if path1 >= 10e9 and path2 >=10e9 :
    print(-1)
else :
    print(min(path1, path2))