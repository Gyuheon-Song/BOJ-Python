import math
x1, y1, r1, x2, y2, r2 = map(float, input(). split())

d = math.sqrt((x1-x2)**2 + (y1-y2)**2)

if r1 + r2 <= d :
    ans = 0.000
elif d + min(r1, r2) <= max(r1, r2) :
    ans = round(math.pi * (r2**2), 3)
else :
    alpha = abs(math.acos(((r1**2) + (d**2) - (r2**2)) / (2*r1*d)))
    beta = abs(math.acos(((r2**2) + (d**2) - (r1**2)) / (2*r2*d)))
    s1 = ((r1**2) * alpha) - ((r1**2) * math.sin(2*alpha) / 2)
    s2 = ((r2**2) * beta) - ((r2**2) * math.sin(2*beta) / 2)
    ans = round(s1 + s2, 3)

print(f"{round(ans, 3):.3f}")

