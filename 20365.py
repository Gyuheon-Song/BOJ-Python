import sys
input = sys.stdin.readline

n = int(input())
color = input().strip()

blue = 0
red = 0

for i in range(len(color)) :
    if i == 0 :
        if color[i] == 'B' :
            blue += 1
        elif color[i] == 'R' :
            red += 1
    else :
        if color[i] == color[i-1] :
            continue
        else :
            if color[i] == 'B' :
                blue += 1
            elif color[i] == 'R' :
                red += 1

print(1+min(blue, red))