white_paper = [[0 for i in range(100)] for j in range(100)]
n = int(input())
sum_row = 0

for k in range(n) :
    x, y = map(int, input(). split())
    for l in range(y, y+10) :
        for m in range(x,x+10) :
            white_paper[m][l] = 1

for n in range(100) :
    sum_row += sum(white_paper[n])
    
print(sum_row)
    

