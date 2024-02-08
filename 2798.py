import sys
input = sys.stdin.readline
n, m = map(int, input(). split())
lst = list(map(int, input(). split()))
lst = list(map(int, lst))
lst.sort()
sum = 0
for i in range(n-2) :
    for j in range(i+1, n-1) :
        for k in range(j+1, n) :
            sum_3 = lst[i] + lst[j] +lst[k]
            if sum_3 <= m :
                sum = max(sum, sum_3)

print(sum)
