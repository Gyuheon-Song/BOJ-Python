from collections import deque
import sys
input = sys.stdin.readline

n, l = map(int, input(). split())
lst = list(map(int, input(). split()))
dq = deque()

for i in range(n) :

    while dq and dq[-1][1] > lst[i] : # 리스트의 값을 덱에 저장하기 전, 마지막 값보다 리스트의 값이 작은 경우
        dq.pop()                      # 덱에 있던 값을 뻬고 그 값보다 작았던 리스트의 값을 덱에 저장
                                      # -->> 이 결과로 항상 덱의 왼쪽에는 가장 작은 값만 저장된다.

    dq.append((i+1, lst[i]))  # 인덱스와 리스트의 값을 튜플로 덱에 저장

    if dq[-1][0] - dq[0][0] >= l :   # 최근에 덱에 저장되었던 값의 인덱스와 덱의 가장 앞부분의
        dq.popleft()                 # 인덱스의 차가 l보다 크거나 갑은 경우 => 슬라이딩 윈도우의 길이가 l보다 길어지는 경우
                                     # 가장 앞의 값을 덱에서 뺀다 --> 다음 큰 값이 덱의 가장 앞부분에 위치    

    print(dq[0][1], end = " ")  # 덱의 가장 앞부분을 출력