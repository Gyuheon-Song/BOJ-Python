n = int(input())

text_li = []
result = str()

for i in range(n) :
    repeat, text = map(str, input(). split())
    repeat = int(repeat)
    result = ""
    
    for j in range(len(text)) :
        result += text[j]*repeat
    
    text_li.append(result)

for k in range(n) :
    print(text_li[k])

    



