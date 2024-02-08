# t = int(input())  

# def fib(k, n) :
#     if n == 1 :
#         return 1
#     elif k == 0 :
#         return n
#     else :
#         while 1 <= k :
#             return fib(k, n-1) + fib(k-1, n) 

# for _ in range(t) :
#     k = int(input())
#     n = int(input())
#     print(fib(k, n))

t = int(input())

def Dp(k, n) :
    apt = [[0]*(n + 1) for _ in range(k + 1)]

    for i in range(n + 1) :
        apt[0][i] = i
    
    for j in range(1, k + 1) :
        for l in range(1, n + 1) :
            apt[j][l] = apt[j][l - 1] + apt[j - 1][l]
    
    return apt[k][n]
    
for _ in range(t) :
    k = int(input())
    n = int(input())
    print(Dp(k, n))