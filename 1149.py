import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input(). split()))
ans = lst.copy()           # 첫번째 리스트 복사

for _ in range(n-1) :
    lst = list(map(int, input(). split()))     # 리스트 입력받기
    tmp = lst.copy()                   # 가장 최근 임시리스트 생성
    for i in range(3) :
        if i == 0 :                    # 첫번째 칸일때
            tmp[i] += min(ans[1], ans[2])   # 이전 리스트의 두,세번째 값중 작은 값을 최근임시리스트의 첫칸 값과 더하여 초기화
        elif i == 1:                   # 중간 칸인때
            tmp[i] += min(ans[0], ans[2])   # 이전 리스트의 첫,세번째 값중 작은 값을 최근임시리스트의 중간 값과 더하여 초기화
        else :                         # 세번째 칸일때
            tmp[i] += min(ans[0], ans[1])   # 이전 리스트의 첫, 중간 값중 작은 값을 최근임시리스트의 마지막 값과 더하여 초기화
    ans = tmp                  # 정답리스트에 위에서 연산에 의해 초기화된 최근임시리스트에 대입

print(min(ans))
