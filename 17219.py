import sys

n, m = map(int, input(). split())
memo = dict()
for _ in range(n) :
    site, pw = map(str, sys.stdin.readline().strip(). split(" "))
    memo[site] = pw

for _ in range(m) :
    ans = input()
    print(memo[ans])
