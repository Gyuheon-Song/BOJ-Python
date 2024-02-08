import sys
input = sys.stdin.readline

n = int(input())

lst = list(map(int, input(). split()))

curr = 0  # 가장 큰 연속합을 저장하는 변수
ans = -100000000

for num in lst :    # 배열의 숫자들을 탐색
    curr = max(curr+num, num)   # 해당 숫자와, 그 숫자를 포함한 이전의 최대연속합의 합을 비교하여 큰 값을 저장
    ans = max(ans, curr)    # 정답변수에 가장큰 연속합과 지금까지의 가장 큰 연속합을 비교하여 큰 값 저장

print(ans)

    

