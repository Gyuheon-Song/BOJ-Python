
fibo = [0,1]
n = int(input())

for i in range(0,n-1) : 
    num = fibo[-2] + fibo[-1]
    fibo.append(num)
print(fibo[-1])

