from collections import deque
import sys
input = sys.stdin.readline

word = deque(input().rstrip())  # 덱으로 입력받기

stack = []   # 스택구현

while word :   # 입력받은 단어의 왼쪽부터 꺼내서 스택에 담아준다
    stack.append(word.popleft())

    if len(stack) >= 4 :   # 스택에 4개이상의 알파벳이 존재하게 되면
        if stack[-4::] == ['P', 'P', 'A', 'P'] :  # 그리고 그 끝의 4개의 문자가 PPAP라면
            for _ in range(3) :   # PPAP -> P 로 바꿔줘야하므로 3개의 문자를(PAP) 오른쪽에서 빼준다
                stack.pop()

if len(stack) == 1 :  # 모든 과정을 거치고 나서 스택에 문자가 1개 남아있으면
    if stack == ['P'] :  # 하나남은 문자가 P라면 PPAP문자열이다
        print("PPAP")
    else :   # A는 NP이다
        print("NP")
else :  # PPAP를 다 P로 바꾸고 나서 스택의 길이는 1보다 길다면 P에서 시작한 문자가 아니므로
    print("NP")