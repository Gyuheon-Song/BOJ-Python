import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
s = list(map(str, input().rstrip()))
t = list(map(str, input().rstrip()))
ans = 0

def Rule(word, s) :
    global ans
    if word == s:
        return True
    elif len(word) <= len(s) :
        return False
    elif word[0] == "B" and Rule(word[::-1][:-1], s):
        return True
    elif word[-1] == "A" and Rule(word[:-1], s) :
        return True
    else :
        return False
         
if Rule(t, s) :
    print(1)
else :
    print(0)







# 아래코드는 시간초과가 난다. 따라서 t에서 제거하는 방식으로 짜보자

# def Rule(word) :
#     global ans
#     if word == t :
#         ans = 1
#         return
#     elif len(word) >= len(t) :
#         return
#     else :
#         Rule(word+["A"])
#         Rule((word+["B"])[::-1])
           
# Rule(s)
# print(ans)




