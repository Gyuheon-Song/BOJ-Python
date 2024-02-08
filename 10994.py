n = int(input())
lst = [[" "]*(1+4*(n-1)) for _ in range(1+4*(n-1))]
cnt = 0
def star(n) :
    if n >= 1 :
        x = 1 + 4*(n-1)
        global cnt
        for i in range(2*cnt, 2*cnt + x) :
            for j in range(2*cnt, 2*cnt + x) :
                lst[i][j] = "*"
    
        for k in range(2*cnt+1, 2*cnt + x - 1) :
                for l in range(2*cnt+1, 2*cnt + x - 1) :
                     lst[k][l] = " "
        cnt += 1
        return star(n-1)
    
    return lst

for inner in star(n) :
    ans = "".join(str(item) for item in inner)
    print(ans)




    