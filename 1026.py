import sys
input = sys.stdin.readline

n = int(input())

a = list(map(int, input().strip(). split()))
b = list(map(int, input().strip(). split()))

a.sort()
b.sort(reverse = True)
ans = 0

for i in range(n) :
    ans += a[i]*b[i]

print(ans)