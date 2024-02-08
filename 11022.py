n = int(input())
case = []
list = []
for i in range(n) :
    a , b = map(int, input(). split())
    case.append(a + b)
    list.append(a)
    list.append(b)

for i in range(n) :
    print(f"Case #{i +1}: {list[2*i]} + {list[2*i+1]} = {case[i]}")