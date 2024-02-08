n = int(input())
m = n//2
# 체스판의 길이가 6으로 나눴을 때 2, 3 인경우 일반적으로 생각할 수 있는 경우가 성립하지 않는다
# 일반적인 경우
# 행을 내려가면서 증가or감소하는 순으로 짝수먼저 쭉 나열 그다음 홀수나열, 혹은 그 반대로
if n%6 == 2:
    for i in range(1, m+1):
        print(i*2)
    print(3)
    print(1)
    for i in range(3, m):
        print(i*2 + 1)
    print(5)
elif n%6 == 3:
    for i in range(2, m+1):
        print(i*2)
    print(2)
    for i in range(2, m+1):
        print(i*2 + 1)
    print(1)
    print(3)
else:   # 일반적인 경우
    for i in range(1,m+1):
        print(i+m)
        print(i)
    if n&1:  # n이 홀수일 때 마지막 배치 (n, n)좌표
        print(n)