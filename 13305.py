city = int(input())
distance = list(map(int, input(). split()))
price = list(map(int, input(). split()))
cost = price[0]
i = 0
m = len(price) - 1
length = 0
pay = 0
while i < m :
        cost = min(cost, price[i])
        length = distance[i]
        pay += length * cost
        i += 1

print(pay)


