from collections import deque
n = int(input())
capacity = [[0] * 128 for _ in range(128)]   # 배관의 최대유량을 저장할 인접행렬


def BFS(flow, capacity, source, sink) :
    q = deque()
    q.append(source)   # 시작 노드를 넣는다
    parent = [-1] * 128   # -1로 값이 초기화된 부모노드 저장 리스트
    parent[source] = source   # 시작노드는 자기자신이 부모노드

    while q :
        now = q.popleft()
        for next in range(128) :
            # 부모노드가 
            if parent[next] == -1 and capacity[now][next] - flow[now][next] > 0 :
                q.append(next)
                parent[next] = now
    
    return parent   # 부모노드 리스트를 반환


def maxFlow(capacity, source, sink) :
    flow = [[0] * 128 for _ in range(128)]   # 흐르는 유량을 저장할 인접행렬
    ans = 0
    
    while True :
        parent = BFS(flow, capacity, source, sink)

        if parent[sink] == -1 :   # BFS가 실패하여 sink의 부모노드가 없다면
            return ans
        
        p = sink   
        amount = 10**9
        while p != source :   # 시작노드까지 배관탐색
            amount = min(amount, capacity[parent[p]][p] - flow[parent[p]][p])   # 경로상의 배관 중 남은 용량의 최솟값을 저장
            p = parent[p]    # 부모노드로 재지정하여 올라가며 탐색
        
        ans += amount   # 최대유량이 흘렀을 시 남은 용량을 정답에 더해준다

        p = sink
        while p != source :
            flow[parent[p]][p] += amount
            flow[p][parent[p]] -= amount
            p = parent[p]

for _ in range(n) :
    a, b, c = map(str, input(). split())
    a = ord(a)
    b = ord(b)
    c = int(c)
    capacity[a][b] += c   # 병렬연결 가능
    capacity[b][a] += c

print(maxFlow(capacity, ord('A'), ord('Z')))