problem = input(). split("-")
answer = 0
for i in problem[0].split("+") :
    answer += int(i)
for j in problem[1:] :
    for k in j.split("+") :
        answer -= int(k)

print(answer)



