n = int(input())

for i in range (n) :
    width = n + i
    star = ("*"*(2*i + 1))
    print(star.rjust(width)) 
for i in range(n-1) :
    width = 2*(n-1) - i
    star = ("*"*((2*n -1)-(2*(i+1))))
    print(star.rjust(width))
       
