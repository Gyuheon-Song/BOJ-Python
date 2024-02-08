n = int(input())

def Euclid(x, y) :
    global r
    if x % y != 0 :
        r = x % y
        Euclid(y, r)
        return x*y//r
    else :
        return x
    

for _ in range(n) :
    a, b = map(int, input(). split())
    if a > b :
        x, y = a, b
    else :
        x, y = b, a
    print(Euclid(x, y))
    