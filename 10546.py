from collections import defaultdict, Counter
def solution(a, b) :
    part = Counter(a)
    compl = defaultdict(int)
    for name in b :
        compl[name] = 1
        if name in part :
            part[name] -= 1
    for key, value in part.items() :
        if value == 1 :
            return key

n = int(input())
a = []
for i in range(n) :
    a.append(input())
b = []
for i in range(n-1) :
    b.append(input())

print(solution(a, b))