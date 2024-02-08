import sys
input = sys.stdin.readline

name = input()
ans = []

for i in range(len(name)) :
    if i == 0 :
        ans.append(name[i])
    elif name[i] == '-' :
        ans.append(name[i+1])
    else :
        continue

print(*ans, sep = "")