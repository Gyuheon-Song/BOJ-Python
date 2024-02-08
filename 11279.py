from heapq import heappush, heappop
import sys
input = sys.stdin.readline
n = int(input())
heap = []

while n > 0 :
    x = int(input())
    n -= 1
    if x == 0 :
        if len(heap) == 0 :
            print(0)
        else :
            print(-heappop(heap))
    else :
        heappush(heap, -x)