
a, b, c = map(int, input(). split())

if a == b == c :
    prize = 10000 + a*1000
elif a == b or b == c :
    prize = 1000 + b*100
elif a == c :
    prize = 1000 + a*100
else :
    prize = max(a,b,c)*100

print(prize)
