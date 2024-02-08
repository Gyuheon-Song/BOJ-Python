from heapq import heappush, heappop
import sys
input = sys.stdin.readline
heap = []
n = int(input())
for i in range(n) :
    x = int(input())
    if x == 0 :
        if len(heap) == 0 :
            print(0)
        else :
            print(heappop(heap))
    else :
        heappush(heap, x)


