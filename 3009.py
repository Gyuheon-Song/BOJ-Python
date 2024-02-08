x_coor = []
y_coor = []
for i in range(3) :
    x, y = map(int, input(). split())
    x_coor.append(x)
    y_coor.append(y)

for num in x_coor :
    if x_coor.count(num) == 1 :
        numx = num

for num in y_coor :
    if y_coor.count(num) == 1 :
        numy = num

print(numx, numy)