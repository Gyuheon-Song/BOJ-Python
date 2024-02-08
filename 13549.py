from collections import deque

n, k = map(int, input(). split())

def BFS(start, end) :
    chk = [-1] * 100001
    Q = deque()
    Q.append(start)
    chk[start] = 0
    while Q :
        x = Q.popleft()
        if x == end :
            return chk[x]
        for move in [x-1, x+1, x*2] :
            if move >= 0 and move <= 100000 and chk[move] == -1 :
                if move == x*2 :
                    chk[move] = chk[x]
                    Q.appendleft(move)
                else :
                    chk[move] = chk[x] + 1
                    Q.append(move)

print(BFS(n, k))

