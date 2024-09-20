import sys
input = sys.stdin.readline

poly = input().rstrip()
ans = []
coef = []
flag = True

for ch in poly :
    if ch == 'x' :
        flag = False
        int_coef = int(''.join(coef))
        int_coef //= 2
        if int_coef != 1 :
            ans.append(str(int_coef))
        ans.append("xx")
        coef.clear()
    elif ch == '+' or ch == '-' :
        ans.append(ch)
    else :
        coef.append(ch)

if coef :   # 상수항이 주어진 경우
    if flag :  # 0차 다항식인 경우
        int_coef = int(''.join(ans+coef))  # 음수양수 고려
        if int_coef == 0 :   # 상수가 0인 경우
            print('W')   # 적분상수만 출력하고 종료
            exit()
        elif int_coef == 1 :   # 상수가 +1 인 경우
            ans.append('x')
        elif int_coef == -1 :    # 상수가 -1인 경우
            ans.append("x")
        else :  # 다른 임의의 상수인 경우
            ans.append(str(abs(int_coef)))
            ans.append('x')
        ans.append("+W")
        print(''.join(ans))
    else :    # 일차 다항식인 경우
        int_coef = int(''.join(coef))
        if int_coef == 1 :  # 상수가 +1 또는 -1인 경우
            ans.append('x')
        else :
            ans.append(str(int_coef))  # 다른 임의의 상수인 경우
            ans.append('x')
        ans.append("+W")
        print(''.join(ans))
else :     # 상수항이 주어지지 않은 경우
    print(''.join(ans), end = '')
    print("+W")

    
        

