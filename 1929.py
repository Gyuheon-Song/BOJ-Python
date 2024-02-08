n, m = map(int, input(). split())
lst = [True] * (m + 1)
def Eratos(n, m) :
    end = int(m ** 0.5)
    for i in range(2, end+1) :
        if lst[i] == True :
            for j in range(2*i, m+1, i) :
                lst[j] = False
    
    return [i for i in range(2, m+1) if lst[i] == True and i >= n]

print(*Eratos(n, m), sep = "\n")


