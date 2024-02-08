array = []
max_num = []
for i in range(9) :
    lst = list(map(int, input(). split()))
    array.append(lst)
    max_num.append(max(lst))
n = max(max_num)
print(n)

for lst in array :
    if n in lst :
        print(array.index(lst) + 1, lst.index(max(lst))+1)
       
        