from collections import deque
import sys

input = sys.stdin.readline
n = int(input())

for _ in range(n) :
    cnt = 0
    num, doc_idx = map(int, input(). split())
    Q = deque(map(int, input(). split()))
    idxq = deque([i for i in range(num)])

    while True :
        if Q[0] != max(Q) :
            Q.append(Q.popleft())
            idxq.append(idxq.popleft())
        elif Q[0] == max(Q) :              
            if idxq[0] != doc_idx :
                Q.popleft()
                idxq.popleft()
                cnt += 1
            elif idxq[0] == doc_idx :
                cnt += 1
                break
            
    print(cnt)
       