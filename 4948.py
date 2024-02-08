import math
import sys
input = sys.stdin.readline

lst = [True] * 246913
for i in range(2, 246913) :
    for j in range(2, int(math.sqrt(246913)) + 1) :
        if lst[i] :
            if i % j == 0 :
                for k in range(i*i, 246913, i) :
                    lst[k] = False                 

def Prime(num) :
    cnt = 0
    for i in range(num + 1, num*2 + 1) :
        if lst[i] :
            cnt += 1
    return cnt

while True :
    n = int(input())
    if n == 0 :
        break
    print(Prime(n))