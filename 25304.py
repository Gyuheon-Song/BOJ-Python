total = int(input())
type = int(input())
cost = []
for i in range(0, type) :
    price, num = map(int, input(). split())
    cost.append(price * num)

total_cost = sum(cost)
if total == total_cost :
    print("Yes")
else :
    print("No")