import sys
input = sys.stdin.readline
n, k = map(int, input(). split())
lan = [int(input()) for _ in range(n)]
start, end = 1, max(lan)

while start <= end :
    mid = (start + end) // 2
    num = 0
    for i in lan :
        num += i // mid
    if num >= k :
        start = mid + 1
    else :
        end = mid - 1
print(end)
