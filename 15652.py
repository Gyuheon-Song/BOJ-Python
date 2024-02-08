n, m = map(int, input(). split())
ans = []

def DFS(start) :
    if len(ans) == m :
        print(" ".join(map(str, ans)))
        return
    for i in range(start, n+1) :
        ans.append(i)
        DFS(i)
        ans.pop()

DFS(1)