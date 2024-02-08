import sys
import math
input = sys.stdin.readline

def Prime(num) :
    if num == 1 :
        return False
    for i in range(2, int(math.sqrt(num)) + 1) :
        if num % i == 0 :
            return False
    return True

def Palindrome(num) :
    return num == num[::-1] 
        

a, b = map(int, input(). split())
if b > 10000000 :
    b = 9999999

if a % 2 == 0 :
    for num in range(a+1, b+1, 2) :
        if len(str(num)) % 2 == 0 and num != 11 :
            continue
        if Palindrome(str(num)) :
            if Prime(num) :
                print(num)
else :
    for num in range(a, b+1, 2) :
        if len(str(num)) % 2 == 0 and num != 11 :
            continue
        if Palindrome(str(num)) :
            if Prime(num) :
                print(num)
print(-1)



    


