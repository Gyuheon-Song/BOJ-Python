import sys
input = sys.stdin.readline

tree = {}
total = 0

while True :
    wood = input().rstrip()
    if not wood :
        break
    if wood not in tree.keys() :
        tree[wood] = 1
        total += 1
    elif wood in tree.keys() :
        tree[wood] += 1
        total += 1

for key in tree.keys() :
    tree[key] = (tree[key]/total)*100

ans = sorted(tree.items())

for key, value in ans :
    print(key, "{:.4f}".format(value))
