import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t) :
    n = int(input())
    numlst = [input().rstrip() for _ in range(n)]
    numlst.sort()
    flag = True
    for i in range(n-1) :
        if numlst[i] == numlst[i+1][:len(numlst[i])] :
            flag = False
            break
    print("NO") if not flag else print("YES")

