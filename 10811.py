basket, trial = map(int, input(). split())
basket_num =[]

for i in range(basket) :
    basket_num.append(i+1)

for j in range(trial) :
    initial , terminal = map(int, input(). split())
    extract_li = basket_num[initial-1 : terminal]
    reverse_li = extract_li[::-1]
    basket_num[initial-1 : terminal] = reverse_li

print(*basket_num) 