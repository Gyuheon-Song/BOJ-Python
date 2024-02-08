while True :
    stack = []
    problem = input()
    if problem == "." :
        break
    for k in problem :
        if k == "(" or k == "[" :
            stack.append(k)
        elif k == ")" :
            if len(stack) != 0 and stack[-1] == "(" :
                stack.pop()
            else :
                stack.append(")")
                break
        elif k == "]" :
            if len(stack) != 0 and stack[-1] == "[" :
                stack.pop()
            else :
                stack.append("]")
                break
    if len(stack) == 0 :
        print("yes")
    else :
        print("no")



