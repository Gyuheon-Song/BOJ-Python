import sys
input = sys.stdin.readline
n, m = map(int, input(). split())
lst = [0] + list(map(int, input(). split()))
sumlst = [0]*(n+1)
remainlst = [0]*(m)
cnt = 0

for i in range(1, n+1) :
    sumlst[i] = (sumlst[i-1] + lst[i]) % m
    if sumlst[i] == 0 :
        cnt += 1
    remainlst[sumlst[i]] += 1

for i in range(m) :
    if remainlst[i] > 1 :
        cnt += (remainlst[i] * (remainlst[i]-1)) // 2

print(cnt)

