import sys
input = sys.stdin.readline

n, m = map(int, input(). split())
lst = list(map(int, input(). split()))
lst.sort()
ans = []
chk = [0] * n

def DFS() :
        
    if len(ans) == m :
        print(" ".join(map(str, ans)))
        return
    used = None
    for i in range(n) :
        if chk[i] == 0 and used != lst[i] :
            chk[i] = 1
            ans.append(lst[i])
            used = lst[i]
            DFS()
            chk[i] = 0
            ans.pop()

DFS()

