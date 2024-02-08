import sys
input = sys.stdin.readline
k = int(input())
for _ in range(k) :
    h, w, n = map(int, input(). split())
    if (n % h) != 0 :
        floor = (n % h) * 100
        room = 1 + n//h
    else :
        floor = h * 100    
        room = n//h
    ans = floor + room
    print(ans)