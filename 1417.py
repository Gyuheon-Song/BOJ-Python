import heapq as hpq
n = int(input())
hq = []

dasom = int(input())
cnt = 0

for _ in range(n-1) :
    hpq.heappush(hq, -int(input()))

if n != 1 :
    while True :
        popular = -hpq.heappop(hq)
        if dasom > popular :
            break
        popular -= 1
        dasom += 1
        cnt += 1
        hpq.heappush(hq, -popular)

if n == 1 :
    print(0)
else :
    hpq.heappush(hq, -popular)
    popular = -hpq.heappop(hq)
    if dasom == popular :
        print(cnt + 1)
    else :
        print(cnt)
