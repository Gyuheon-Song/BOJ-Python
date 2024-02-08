x = int(input())
y = int(input())

if x*y>0 and x>0:
    print(1)
elif x*y>0 and x<0:
    print(3)
if x*y<0 and x>0:
    print(4)
elif x*y<0 and x<0:
    print(2)
