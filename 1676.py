import sys
import math
input = sys.stdin.readline

lst = []
n = int(input())
fact_n = math.factorial(n)
fact_n = list(str(fact_n))
fact_n = fact_n[::-1]
for i in fact_n :
    if i == "0" :
        lst.append(i)
        continue
    else :
        break
if len(lst) >= 1 : 
    print(len(lst))
else :
    print(0)