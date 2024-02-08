n = int(input())
lst = [1, 2] + ([0] * 998)

for i in range(2, n) :
    lst[i] = lst[i-1] + lst[i-2]

print(lst[n-1] % 10007)