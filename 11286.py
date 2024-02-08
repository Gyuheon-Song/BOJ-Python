from heapq import heappush, heappop
import sys
input = sys.stdin.readline
n = int(input())
heap = []

while n > 0 :
    x = int(input())
    n -= 1
    if x == 0 :
        if not heap :
            print(0)
        else :
            print(heappop(heap)[1])
    else :
        heappush(heap, (abs(x), x))