import sys
from collections import deque
input = sys.stdin.readline


def BFS(sr, sc, er, ec) :
    visited = [False] * n
    q = deque()
    q.append((sr, sc))

    while q :
        tr, tc = q.popleft()

        if abs(tr-er) + abs(tc-ec) <= 1000 :
            return "happy"

        for i in range(n) :   # 미방문 모든 편의점좌표에 대해서 범위 내인지 체크
            if not visited[i] :
                nr, nc = store[i]
                if abs(tr-nr) + abs(tc-nc) <= 1000 :
                    q.append((nr, nc))
                    visited[i] = True
    
    return "sad"

t = int(input())

for _ in range(t) :
    n = int(input())
    store = []
    sr, sc = map(int, input(). split())
    for _ in range(n) :
        tr, tc = map(int, input(). split())
        store.append((tr, tc))
    er, ec = map(int, input(). split())

    ans = BFS(sr, sc, er, ec)
    print(ans)