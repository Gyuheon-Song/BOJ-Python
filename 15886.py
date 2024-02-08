import sys
input = sys.stdin.readline

n = int(input())
arr = input().strip()
ans = 0

if 'E' not in arr or 'W' not in arr :
    print(1)
else :
    for i in range(len(arr)) :
        if arr[i] == 'W' :
            continue
        else :
            if arr[i+1] == 'W' :
                ans += 1
            else :
                continue
    print(ans)            
