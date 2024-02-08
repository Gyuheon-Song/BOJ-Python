summation = []
a , b = map(int, input(). split())

while a + b != 0 :
    summation.append(a+b)
    a , b = map(int, input(). split())

for item in summation :
    print(item)
