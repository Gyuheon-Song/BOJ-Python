import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input(). split()))
setnums = sorted(list(set(nums)))
dic = {}
for i in range(len(setnums)) :
    dic[setnums[i]] = i

for num in nums :
    print(dic[num], end = " ")
