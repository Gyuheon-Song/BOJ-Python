import sys
input = sys.stdin.readline
import heapq

n, m, x = map(int, input(). split())
adjlst = [[] for _ in range(n+1)]
anslst = [0]  # 각 마을에서 x마을까지의 최단 왕복시간을 담을 리스트 생성

for _ in range(m) :
    u, v, t = map(int, input(). split())
    adjlst[u].append((v, t))
# 방문 마을 다시 방문하면 안된다는 제약사항 없으므로 방문리스트는 따로 만들지 않는다

def Dajikstra(depart, arrive) :
    time = [sys.maxsize] * (n+1)
    hq = []
    heapq.heappush(hq, (0, depart))
    time[depart] = 0

    while hq :
        now = heapq.heappop(hq)
        now_node = now[1]
        for temp in adjlst[now_node] :
            next_node = temp[0]
            usedt = temp[1]
            if time[next_node] > time[now_node] + usedt :
                time[next_node] = time[now_node] + usedt
                heapq.heappush(hq, (time[next_node], next_node))
    
    return time[arrive]

for i in range(1, n+1) :
    res = Dajikstra(i, x) + Dajikstra(x, i)      # 각 마을에서 x마을까지의 왕복 최단시간을 구해야 하므로
    anslst.append(res)                           # 다익스트라 알고리즘에서 출발과 도착지점을 바꾸어 각각 더해준다

print(max(anslst))    # 각 마을에서 x마을까지의 최단왕복시간들 중 가장 오래걸리는 사람의 시간