import heapq as hq
import sys

input = sys.stdin.readline

n, m = map(int, input(). strip(). split())

numlst = list(map(int, input(). strip(). split()))
numhq = []

for i in range(n) :
    hq.heappush(numhq, numlst[i])

for _ in range(m) :
    a = hq.heappop(numhq)
    b = hq.heappop(numhq)
    a += b
    b = a
    hq.heappush(numhq, a)
    hq.heappush(numhq, b)

print(sum(numhq))
    