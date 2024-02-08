remain_li = []

for i in range(10) :
    n = int(input())
    remain = n%42
    remain_li.append(remain)

unique_val = set(remain_li)

print(len(unique_val))
