def DFS(n) :
    if n == 0 :
        return 0
    if n == 1 :
        return 1
    else :
        return DFS(n-1) + DFS(n-2)

n = int(input())
print(DFS(n))