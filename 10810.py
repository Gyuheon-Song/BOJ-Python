basket , trial = map(int, input(). split())
basket_li = []

for i in range(basket) :
    basket_li.append(0)

for j in range(trial) :
    initial , terminal , ball_num = map(int, input(). split())
    
    for k in range(initial-1, terminal) :
        basket_li[k] = ball_num

print(*basket_li)
    


