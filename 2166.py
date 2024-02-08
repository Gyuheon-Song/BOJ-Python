import sys
input = sys.stdin.readline

n = int(input())
k = n
lst = []

while n > 0 :
    lst.append(list(map(int, input(). split())))
    n -= 1

lst.append(lst[0])
sum1 = 0
sum2 = 0
for i in range(k) :
    sum1 += lst[i][0] * lst[i+1][1]
    sum2 += lst[i+1][0] * lst[i][1]

calc = abs(sum1-sum2)

ans = round(0.5 * (calc), 1)

print(ans)
