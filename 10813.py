
basket , trial = map(int, input(). split())
basket_li = []

for i in range(basket) :
    basket_li.append(i+1)
for j in range(trial) :
    a , b = map(int, input(). split())
    basket_li[a-1],basket_li[b-1] =  basket_li[b-1],basket_li[a-1]

print(*basket_li)


