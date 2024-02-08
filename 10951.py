summation = []
a , b = map(int, input(). split())

while True :
    summation.append(a+b)
    try :
        a , b = map(int, input(). split())

    except :
        break

for item in summation :
    print(item)


