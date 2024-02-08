n, m = map(int, input(). split())

def maxft(a, b) :
    r = a % b
    if r == 0 :
        return b
    else :
        return maxft(b, r)
    
def minmt(a, b) :
    k = maxft(a, b)
    i = b // k
    return a * i

if n >= m :
    a = n
else :
    a = m


print(maxft(n, m))
print(minmt(n, m))