import sys
input = sys.stdin.readline

n, k = map(int, input(). split())
arr = list(input().rstrip())
visited = [False]*(n)
cnt = 0

for i in range(n) :
    if arr[i] == 'P' :
        visited[i] = True
        if i >= k :
            for j in range(i-k, i+k+1) :
                if j >= len(arr) :
                    j = len(arr)-1
                if arr[j] == 'H' and not visited[j]:
                    visited[j] = True
                    cnt += 1
                    break
        else :
            for j in range(i+k+1) :
                if j >= len(arr) :
                    j = len(arr)-1
                if arr[j] == 'H' and not visited[j]:
                    visited[j] = True
                    cnt += 1
                    break

print(cnt)