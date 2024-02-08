import sys
input = sys.stdin.readline

n = int(input())

lst = list(map(int, input(). split()))

# 투포인터
left = 0
right = n-1
res = sys.maxsize  # 차의 최솟값을 저장할 변수

while left < right :    
    cur = lst[left] + lst[right]   # 현재 값을 두 용액의 합으로 초기화

    if abs(cur) <= res :   # 현재 산성도의 절댓값이 최솟값 변수보다 작거나 같을때
        x = lst[left]    # 두 용액의 정보를 일단 저장하고
        y = lst[right]
        res = abs(cur)   # 용액의 차의 최솟값을 최신화한다
    
    if cur <= 0 :    # 만약 현재 용액의 차가 0보다 작다면
        left += 1    # 왼쪽 포인터를 하나 증가
    
    else :         # 현재 용액의 차가 0보다 작다면
        right -= 1 # 오른쪽 포인터를 하나 감소
    
print(x, y)
