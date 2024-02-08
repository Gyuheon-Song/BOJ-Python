from collections import Counter
import sys
input = sys.stdin.readline
n = int(input())
num_have = list(map(int, input(). split()))
m = int(input())
num_chk = list(map(int, input(). split()))

num_have = Counter(num_have)

for i in num_chk :
    print(num_have[i], end = " ")
    


