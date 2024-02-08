n = int(input())
submit = []
for i in range(n) :
    ans = True
    stack = []
    problem = input()
    for k in problem:
        if k == ")" :
            if len(stack) == 0 :
                ans = False
            else :
                stack.pop()
        else :
            stack.append(k)
    if len(stack) == 0 and ans == True :
        submit.append("YES")
    elif len(stack) > 0 or ans == False :
        submit.append("NO")
for item in submit :
    print(item)