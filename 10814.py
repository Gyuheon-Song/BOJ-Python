def solution(member) :
    lst.sort(key = lambda x:x[0])

    return lst
    
n = int(input())
lst = []
for i in range(n) :
    age, name = input().split()
    age = int(age)
    lst.append([age, name])

for item in solution(lst) :
    print(*item)