n, m = map(int, input(). split())
dic1 = dict()
dic2 = dict()

for i in range(n) :
    name = input()
    dic1[i+1] = name
    dic2[name] = i+1

for j in range(m) :
    ans = input()
    if ans.isdigit() :
        print(dic1[int(ans)])
    else :
        print(dic2[ans])
    

