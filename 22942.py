import sys
input = sys.stdin.readline
n = int(input())
circle = []


for i in range(n) :
    x, r = map(int, input(). strip(). split())
    circle.append((x-r, i))
    circle.append((x+r, i))

circle.sort()

stack = []

for c in circle :
    if stack :
        if stack[-1][1] == c[1] :
            stack.pop()
        else :
            stack.append(c)
    else :
        stack.append(c)

print("NO") if stack else print("YES")



    
       

