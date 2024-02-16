import math
while True :
    a = int(input())
    if a == 0 :
        break
    ans = 0
    for i in range(1, a+1) :
        if math.pow(a, 2) % i == 0 :   # a제곱의 두 약수
            f1 = i   # 작은 약수
            f2 = math.pow(a, 2) / i    # 큰 약수
            if ((f2-f1) / 2) > a and ((f1-f2) % 2) == 0 :  # b가 a보다 크면서 c가 자연수인 경우
                ans += 1
    print(ans)

