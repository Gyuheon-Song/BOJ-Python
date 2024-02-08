import heapq as hq
t = int(input())

for _ in range(t) :
    n = int(input())
    lst = list(map(int, input(). split()))
    ans = 0
    heap = []
    for num in lst :
        hq.heappush(heap, num)
    while len(heap) > 1 :
        tmp1 = hq.heappop(heap)
        tmp2 = hq.heappop(heap)
        ans += (tmp1 + tmp2)
        hq.heappush(heap, tmp1+tmp2)
    
    print(ans)