import sys
input = sys.stdin.readline

n = int(input())
tree = {}

for _ in range(n) :
    root, left, right = map(str, input(). strip(). split())
    tree[root] = [left, right]

def Pre(root) :
    if root != "." :
        print(root, end = "")
        Pre(tree[root][0])
        Pre(tree[root][1])

def In(root) :
    if root != "." :
        In(tree[root][0])
        print(root, end = "")
        In(tree[root][1])

def Post(root) :
    if root != "." :
        Post(tree[root][0])
        Post(tree[root][1])
        print(root, end = "")

Pre("A")
print()
In("A")
print()
Post("A")

