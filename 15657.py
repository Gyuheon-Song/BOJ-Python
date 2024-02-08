import sys
input = sys.stdin.readline
n, m = map(int, input(). split())
lst = list(map(int, input(). split()))
lst.sort()
ans = []

def DFS(start) :
    if len(ans) == m :
        print(" ".join(map(str, ans)))
        return
    for i in range(start, len(lst)) :
        ans.append(lst[i])
        DFS(lst.index(lst[i]))
        ans.pop()        

DFS(0)