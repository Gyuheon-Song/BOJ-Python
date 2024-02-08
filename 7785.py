n = int(input())
dic = {}
exs_li = []
for i in range(n) :
    name, exsist = map(str, input(). split())
    if exsist == "enter" :
        dic[name] = 1
    elif exsist == "leave" :
        dic[name] = 0 
for key, value in dic.items() :
    if value == 1 :
        exs_li.append(key)
exs_li.sort()
exs_li = exs_li[::-1]

for item in exs_li :
    print(item)