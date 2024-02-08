import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input(). split()))
maxlst = lst
minlst = lst

for _ in range(n-1) :
    lst = list(map(int, input(). split()))
    maxlst = [lst[0] + max(maxlst[0], maxlst[1]), lst[1] + max(maxlst), lst[2] + max(maxlst[1], maxlst[2])]
    minlst = [lst[0] + min(minlst[0], minlst[1]), lst[1] + min(minlst), lst[2] + min(minlst[1], minlst[2])]

print(max(maxlst), min(minlst))


    