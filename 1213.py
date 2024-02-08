import sys
from collections import Counter   # 카운터 호출
input = sys.stdin.readline

word = input().strip()
word = sorted(word)

counter = Counter(word)
oddcnt = 0   # 홀수개인 문자의 개수
oddchar = ''    # 홀수개인 문자
ans = ''

for char, cnt in counter.items() :  
    if cnt % 2 != 0 :   # 홀수개인 문자면
        oddcnt += 1    # 홀수개인 문자의 개수 세어준다
        oddchar = char    # 홀수개인 문자를 저장
    ans += char*(cnt // 2)    # 짝수개인 문자는 그 개수의 절반만큼을 이어준다

# 만약 홀수개인 문자가 1개 이하이면 팰린드롬 생성가능
# 절반치만 이어놨던 문자에 홀수개인 문자 하나를 문자열 중간에 넣어주고 앞의 절반을 뒤집어서 연결
print(ans+oddchar+ans[::-1]) if oddcnt < 2 else print("I'm Sorry Hansoo")

