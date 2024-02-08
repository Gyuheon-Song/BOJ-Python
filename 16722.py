shape = []
haplst = []

def SameOrExclusive(var1, var2, var3) :
    if var1 == var2 and var2 == var3 and var1 == var3 :
        return True
    elif var1 != var2 and var2 != var3 and var1 != var3 :
        return True
    else :
        return False

def Hap(shape1, shape2, shape3) :
    for i in range(3) :
        if not SameOrExclusive(shape1[i], shape2[i], shape3[i]) :
            return False
    return True

for _ in range(9) :
    shape.append(list(map(str, input(). split())))

for i in range(7) :
    for j in range(i+1, 8) :
        for k in range(j+1, 9) :
            if Hap(shape[i], shape[j], shape[k]) :
                haplst.append([i+1, j+1, k+1])

n = int(input())
chk = [False]*(len(haplst))
score = 0
gyul = False

for i in range(n) :
    cmd = list(input(). split())
    if len(cmd) == 1 :
        flag = True 
        for j in range(len(chk)) :
            if not chk[j] :
                flag = False
                break
        if flag :
            if not gyul :
                score += 3
                gyul = True
            else :
                score -= 1
        else :
            score -= 1
    else :
        tmp = [int(num) for num in cmd[1::]]
        tmp.sort()
        if tmp in haplst :
            if not chk[haplst.index(tmp)] :
                score += 1
                chk[haplst.index(tmp)] = True
            else :
                score -= 1
        else :
            score -= 1

print(score)





