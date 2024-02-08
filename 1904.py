n = int(input())
lst = [1, 2]

for i in range(2, n) :
    lst.append((lst[i-1] + lst[i-2])%15746)

print(lst[n-1])