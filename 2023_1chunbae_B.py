n = int(input())
s = input()

rainbow = ['r', 'o', 'y', 'g', 'b', 'i', 'v']
rAINBOW = ['R', 'O', 'Y', 'G', 'B', 'I', 'V']

for i in range(n) :
    if s[i] in rainbow :
        rainbow.remove(s[i])
    elif s[i] in rAINBOW :
        rAINBOW.remove(s[i])

l, L = len(rainbow), len(rAINBOW)

if l == 0 :
    if L == 0 :
        print("YeS")
    else :
        print("yes")
else :
    if L == 0 :
        print("YES")
    else :
        print("NO!")
