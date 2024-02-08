import sys
input = sys.stdin.readline
n, m = map(int, input(). split())
lst = list(map(int, input(). split()))
lst.sort()
ans = []

def DFS() :
    if len(ans) == m :
        print(" ".join(map(str, ans)))
        return
    for i in range(len(lst)) :
        if lst[i] not in ans :
            ans.append(lst[i])
            DFS()
            ans.pop()

DFS()