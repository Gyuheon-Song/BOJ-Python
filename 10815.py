import sys
input = sys.stdin.readline
n = int(input())
num_have = list(map(int, input(). split()))
m = int(input())
num_given = list(map(int, input(). split()))

dict = {}  
for i in range(len(num_have)):
    dict[num_have[i]] = 0  

for j in range(m):
    if num_given[j] not in dict:
        print(0, end=' ')
    else:
        print(1, end=' ')


