import sys
input = sys.stdin.readline
n = int(input())
crane = list(map(int, input(). strip(). split()))
m = int(input())
box = list(map(int, input(). strip(). split()))

crane.sort(reverse = True)
box.sort(reverse = True)
if crane[0] < box[0] :
    print(-1)

else:
    cnt = 0
    while box:
        for c in crane:
            if box and c <=box[-1] :
                continue
            for b in box :
                if c >= b :
                    box.remove(b)
                    break
        cnt +=1
    print(cnt)









            



