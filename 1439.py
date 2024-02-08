import sys
input = sys.stdin.readline
n = input().rstrip()

cnt = 0
for i in range(len(n)-1) :
    if n[i] != n[i+1] :
        cnt += 1

print(cnt//2) if cnt % 2 == 0 else print(cnt//2 + 1)
        
