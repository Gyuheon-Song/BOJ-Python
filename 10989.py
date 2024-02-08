import sys
input = sys.stdin.readline
n = int(input())
lst = [0]*10001
for i in range(n) :
    num = int(input())
    lst[num] += 1
for i, num in enumerate(lst) :
    if num != 0 :
        for j in range(num) :
            print(i)
    

