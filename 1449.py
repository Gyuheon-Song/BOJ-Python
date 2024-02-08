import sys
input = sys.stdin.readline
n, l = map(int, input().strip(). split())
hole = list(map(int, input(). split()))
chklst = [True]*(1001)
hole.sort()

for h in hole :
    chklst[h] = False

cnt = 0
for i in range(1, 1001) :
    if not chklst[i] :
        if i+l < 1001 :
            for j in range(l) :
                chklst[i+j] = True
        else :
            cnt += 1
            break
        cnt += 1

print(cnt)