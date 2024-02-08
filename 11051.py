n, k = map(int, input(). split())

def fact(x) :
    ans = 1
    for i in range(1, x+1) :
       ans *= i 
    return ans

def sol(n, k) :
    return fact(n) // (fact(n-k) * fact(k))
    
print(sol(n, k) % 10007)