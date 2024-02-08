import math
d, h, w = map(int, input(). split())

height = math.sqrt((d**2 / ((h**2) + (w**2)))) * h
width = math.sqrt((d**2 / ((h**2) + (w**2)))) * w

print(int(height), int(width))
