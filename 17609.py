import sys
input = sys.stdin.readline

def CheckPalindrome(s) :  # 팰린드롬 여부 확인
    left = 0   # 두 포인터
    right = len(s) - 1
    if s == s[::-1] :   
        return 0  # 그 자체로 팰린드롬이면 0 반환
    else :  # 유사팰린드롬인지 아예 팰린드롬이 아닌지를 구분하자
        while left < right :   # 포인터의 좌우가 반전되기 전까지 반복
            if s[left] == s[right] :   # 양끝부터 문자를 비교하며 일치하면 포인터를 양끝부터 조여온다
                left += 1    
                right -= 1
            else :   # 회문의 규칙이 아닌 때가 왔을때
                tmp1 = s[:left] + s[left+1:]   # 왼쪽 포인터의 문자를 건너뛰고 생각
                tmp2 = s[:right] + s[right+1:]  # 오른쪽 포인터의 문자를 건너뛰고 생각
                if tmp1 == tmp1[::-1] or tmp2 == tmp2[::-1] :   # 어느쪽을 제외하고서라도 회문의 구조가 만들어지면
                    return 1  # 유사회문
                else :   # 회문이 되지 않는다면 그 문자는 유사 팰린드롬도 아니다
                    break
    return 2   # 아무것도 아닌 문자열을 2 반환

t = int(input())

for _ in range(t) :
    word = list(input().rstrip())
    print(CheckPalindrome(word))

