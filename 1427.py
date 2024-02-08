import sys
input = sys.stdin.readline
lst = []
n = int(input())
for i in str(n) :
    lst.append(int(i))
lst.sort()
lst = lst[::-1]
print(*lst, sep = '')