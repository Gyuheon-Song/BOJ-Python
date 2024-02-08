import sys
input = sys.stdin.readline

dad = list(map(str, input(). split()))
mom = list(map(str, input(). split()))

lst = mom + dad
lst = list(set(lst))
lst = sorted(lst)

for c1 in lst :
    for c2 in lst :
        print(c1, c2)
    
