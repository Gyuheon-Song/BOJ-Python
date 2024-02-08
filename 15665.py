n, m = map(int, input(). split())
lst = list(map(int, input(). split()))
ans = []
lst = list(set(lst))
lst.sort()

def DFS(cnt, ans) :
    if cnt == m :
        return print(*ans)
    
    for i in lst :
        DFS(cnt+1, ans+[i])
    
    cnt -= 1

DFS(0, ans)
    
