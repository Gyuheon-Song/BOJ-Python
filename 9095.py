n = int(input())
lst = [1, 2, 3]
ans = [1] * 11

for _ in range(7) :
    lst.append(sum(lst[-3::]))

for i in range(1, 11) :
    ans[i] = ans[i-1] + lst[i-1]

for _ in range(n) :
    want_num = int(input())
    print(ans[want_num-1])

