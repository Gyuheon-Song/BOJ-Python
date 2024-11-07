import sys

def Area(x, y) :
    global pick_pt, area
    total = 0
    for i in range(3) :
        total += (abs(x*(pick_pt[i][0][1]-pick_pt[i][1][1]) + pick_pt[i][0][0]*(pick_pt[i][1][1] - y) + pick_pt[i][1][0]*(y-pick_pt[i][0][1])) / 2)
    
    return True if total <= area else False


tri_pt = []
apple_tree = []
pick_pt = []

for _ in range(3) :
    tri_pt.append(list(map(int, input(). split())))

n = int(input())

for _ in range(n) :
    apple_tree.append(list(map(int, input(). split())))

area = abs(tri_pt[0][0] * (tri_pt[1][1] - tri_pt[2][1]) + tri_pt[1][0] * (tri_pt[2][1] - tri_pt[0][1]) + tri_pt[2][0] * (tri_pt[0][1] - tri_pt[1][1])) / 2

for i in range(2) :
    for j in range(i+1, 3) :
        pick_pt.append([tri_pt[i], tri_pt[j]])

ans = 0
for apple in apple_tree :
    if Area(apple[0], apple[1]) :
        ans += 1

print("{:.1f}".format(area))
print(ans)

    