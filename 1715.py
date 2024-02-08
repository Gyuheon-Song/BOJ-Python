import sys
import heapq

input = sys.stdin.readline

n = int(input())
hq = []
ans = 0

while n > 0 :   
    heapq.heappush(hq, int(input().rstrip()))    # 최소힙
    n -= 1

while len(hq) >= 2 :   # 최소힙에 카드묶음이 있으면
    tmp = 0
    for i in range(2) :   # 가장 작은 두 묶음씩 꺼내
        x = heapq.heappop(hq)
        tmp += x          # 묶어준다
    heapq.heappush(hq, tmp)  # 그 묶음을 다시 최소힙에 넣어준다
    ans += tmp   # 해당 묶음을 위한 비교비용을 정답에 더해준다

print(ans)   