import sys
input = sys.stdin.readline
n = int(input())
lst = [list(map(int, input(). split())) for _ in range(n)]

for i in range(1, n) :
    for j in range(len(lst[i])) :
        if j == len(lst[i]) - 1 :
            lst[i][j] += lst[i-1][j-1]
        elif j == 0 :
            lst[i][j] += lst[i-1][j]
        else :
            lst[i][j] += max(lst[i-1][j], lst[i-1][j-1])

print(max(lst[-1]))

