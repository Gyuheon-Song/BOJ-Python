t = int(input())
ans = [[1, 0], [0, 1]] + [[0, 0] for _ in range(39)]

for i in range(2, 41) :
    ans[i][0] = ans[i-2][0] + ans[i-1][0]
    ans[i][1] = ans[i-2][1] + ans[i-1][1]     
     
for _ in range(t) :
    n = int(input())
    print(*ans[n])


