n = int(input())
x_coor = []
y_coor = []
for i in range(n) :
    x, y = map(int, input(). split())
    x_coor.append(x)
    y_coor.append(y)

hori = max(x_coor)-min(x_coor)
vert = max(y_coor)-min(y_coor)

print(hori*vert)