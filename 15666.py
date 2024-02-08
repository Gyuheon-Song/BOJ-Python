import sys
input = sys.stdin.readline

n, m = map(int, input(). split())
lst = list(map(int, input(). split()))
setlst = list(set(lst))
setlst.sort()
ans = []
used = 0

def DFS() :  
    global used 
    if len(ans) == m :
        print(" ".join(map(str, ans)))
        return
    for i in range(len(setlst)) :
        if setlst[i] >= used :
            ans.append(setlst[i])
            used = setlst[i]
            DFS()
            used = setlst[i]
            ans.pop()

DFS()