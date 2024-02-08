import sys
input = sys.stdin.readline

word = input().strip()
word = list(word)

if word == word[::-1] :
    print(len(word))
else :
    for i in range(1, len(word)) :
        tmp = word[:i]
        pal = word + tmp[::-1]
        if pal == pal[::-1] :
            print(len(pal))
            break
