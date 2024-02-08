n = int(input())
a = list(map(int,input().split()))
x = int(input())
count = 0
for i in range(0,n) : 
    if a[i] == x :
        count = count + 1
print(count)

