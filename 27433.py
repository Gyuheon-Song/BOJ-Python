def DFS(n):
    if n == 0 :
        return 1
    else :
        return n*DFS(n-1)

n = int(input())
print(DFS(n))