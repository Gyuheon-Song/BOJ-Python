dial = list(input())

dial_li = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

second = 0

for i in dial :
    for j in dial_li :
        if i in j :
            second += dial_li.index(j) + 3

print(second)


        





    
    
        

    




