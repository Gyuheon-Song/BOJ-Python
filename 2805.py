import sys
input = sys.stdin.readline
n, m = map(int, input(). split())
lst = list(map(int, input(). split()))

l, r = 1, max(lst)  # 1부터 가장 큰 나무까지의 길이 중 적절히 잘라야 하는 높이를 찾기

#이분탐색 O(nlogm)
while l <= r :
    mid = (l + r) // 2
    length = 0

    for log in lst :  # 자를 높이를 한번 탐색할 때마다 가져갈 수 있는 나무의 길이 계산
        if mid < log :
            length += log - mid

    if length < m :  # 만약 가져갈 수 있는 길이가 부족한 경우
        r = mid - 1   # 좀더 낮은 높이를 자르자
    else :   # 가져갈 수 있는 길이가 남는 경우
        l = mid + 1   # 좀더 높은 높이에서 자르자

print(r)