import sys

while True :
    lst = list(sys.stdin.readline().split())
    lst = list(map(int, lst))
    lst.sort()
    if lst == [0, 0, 0] :
        break
    elif lst[0]**2 + lst[1]**2 == lst[2]**2 :
        print("right")
    else :
        print("wrong")
