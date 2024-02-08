n = int(input())
m = int(input())
s = input()

pointer = cnt = ans = 0    # 탐색을 할 포인터와 IOI개수를 셀 cnt, 결과값을 계산할 ans

while pointer < (m-1) :     # 포인터가 끝에 도달하지 못했다면 반복  
    if s[pointer: pointer+3] == "IOI" :   # 가장작은 단위인 "IOI"를 탐색한다
        pointer += 2   # "IOI" 를 찾았을 경우 포인터를 끝의 I로 인덱스 2만큼 이동시킨다
        cnt += 1       # "IOI" 의 개수를 센다
        if cnt == n :  # 만약 "IOI"가 우리가 찾는 길이만큼인 n개와 동일할 때
            ans += 1   # 일단 P(n)을 하나 찾았으므로 결과에 하나 더한다
            cnt -= 1   # 그 다음 "IOI" 를 찾으면 바로 또하나의 P(n)일 것이므로 cnt에서 한토막을 빼놓는다
    else :
        pointer += 1  # "IOI"를 찾지 못하면 초인터를 인덱스 1씩 이동한다
        cnt = 0       # 또한 "IOI"의 길이를 초기화시킨다

print(ans)
