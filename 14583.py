import math
h, v = map(float, input(). split())

# 접을 세로변의 길이
a = (h * math.sqrt(math.pow(h, 2) + math.pow(v, 2)) - math.pow(h, 2)) / v

# 최종 포스터의 세로길이
vv = (h * (v - a)) / math.sqrt(math.pow(h, 2) + math.pow(a, 2))

# 최종 포스터의 가로길이
hh = math.sqrt(math.pow(h, 2) + math.pow(a, 2)) / 2

print(round(hh, 2))
print(round(vv, 2))