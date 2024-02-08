import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input(). split())
jewel = []   # 보석들의 가치와 무게를 저장할 우선순위큐
bag = []     # 가방의 용량을 저장할 리스트

for _ in range(n) :
    w, v = map(int, input(). split())
    jewel.append([w, v])     # 보석 리스트에 저장
jewel.sort()                 # 무게를 기준으로 오름차순으로 정렬

for _ in range(k) :
    cpct = int(input())
    bag.append(cpct)
bag.sort()    # 가방의 용량을 오름차순으로 정렬

ans = 0
price = []   # 가격이 높은 순서대로의 보석의 가격들을 저장할 최대우선순위큐

for i in bag :  # 각 가방들의 용량에 대해(오름차순)
    while jewel and i >= jewel[0][0] :   # 가방의 용량으로 훔칠 수 있는 보석들을 탐색하여 훔칠 수 있다면
        heapq.heappush(price, -heapq.heappop(jewel)[1])   # 보석가격큐에 그 보석의 가치를 저장한다(음수부호를 붙여 추후에 가치가 큰 보석부터 나올 수 있도록)
    if price :   # 만약 가방용량보다 작은 무게의 보석이 있다면
        ans -= heapq.heappop(price)  # 정답변수에 더해나간다(음수부호를 상쇄시키자)         

print(ans)




