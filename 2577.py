a = int(input())
b = int(input())
c = int(input())
d = str(a*b*c)
d = list(d)
n = len(d)
lst = [0]*(10)
for i in d :
    lst[int(i)] += 1

for item in lst :
    print(item)
