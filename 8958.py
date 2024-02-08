import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n) :
    quiz = list(map(str, input()))
    O = []
    score = 0
    for i in quiz :
        if i == "O" :
            O.append(i)
            cnt = len(O)
            score += cnt
        else :
            O = []
    print(score)