import sys
input = sys.stdin.readline
import math

n = int(input())
lst = list(map(int, input(). split()))
prime = [i for i in range(5000001)]


for i in range(2, 2237) :
    if prime[i] == i :
        for l in range(i*2, 5000001, i) :
            if prime[l] == l :
                prime[l] = i
        
for j in lst :
    ans = []
    while j > 1 :
        ans.append(prime[j])
        j = j // prime[j]
    print(*ans)