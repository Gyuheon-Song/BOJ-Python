from collections import deque
n, k = map(int, input(). split())

def BFS(n, k) :
    chk = [0] * (100001)
    Q = deque()
    Q.append(n)
    chk[n] = 1
    L = 0
    while Q :
        l = len(Q)
        for i in range(l) :
            x = Q.popleft()
            if x == k :
                return L
            for nx in [x-1, x+1, 2*x] :
                if nx >= 0 and nx <= 100000 and chk[nx] == 0 :
                    Q.append(nx)
                    chk[nx] = 1
        L += 1

print(BFS(n, k))    