import sys
input = sys.stdin.readline

n, m = map(int, input(). split())
uflst = [i for i in range(n)]


def Find(x) :
    if x == uflst[x] :
        return x
    else :
        uflst[x] = Find(uflst[x])
        return uflst[x]

def Union(a, b) :
    a = Find(a)
    b = Find(b)
    if a < b :
        uflst[b] = a
    else :
        uflst[a] = b

ans = 0

for i in range(m) :
    s, e = map(int, input(). split())
    if not ans :
        if Find(s) == Find(e) :
            ans = i+1
        else :
            Union(s, e)

print(ans)