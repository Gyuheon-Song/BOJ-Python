n, m = map(int, input(). split())

hunkmin = 1001
indivmin = 1001

for _ in range(m) :
    a, b = map(int, input(). split())
    hunkmin = min(hunkmin, a)
    indivmin = min(indivmin, b)

print(min((n // 6) * hunkmin + (n % 6) * indivmin , (n//6 + 1) * (hunkmin), indivmin * n))

