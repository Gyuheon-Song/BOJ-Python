n, k = map(int, input(). split())
n_fact = 1
k_fact = 1
a = n - k
a_fact = 1
for i in range(1, n) :
    i += 1
    n_fact *= i

for j in range(1, k) :
    j += 1
    k_fact *= j

for m in range(1, a) :
    m += 1
    a_fact *= m

print(n_fact//(a_fact*k_fact))

"""""
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

result = 1
for i in range(K):
    result *= N
    N -= 1

divisor = 1
for i in range(2, K+1):
    divisor *= i

print(result // divisor)
"""