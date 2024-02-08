import sys
input = sys.stdin.readline

n = int(input())
tree = list(map(int, input(). split()))
tree.sort(reverse = True)

for i in range(n) :
    tree[i] -= (n-i-1)

print(max(tree) + n + 1)