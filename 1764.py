
n, m = map(int, input(). split())
not_heard = set()
not_seen = set()
for i in range(n) :
    name = str(input())
    not_heard.add(name)
for i in range(m) :
    name = str(input())
    not_seen.add(name)
never = not_heard.intersection(not_seen)
never = list(never)
never.sort()
print(len(never))
for item in never :
    print(item)
