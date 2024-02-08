import sys
n = int(sys.stdin.readline())
stack =[]

for i in range(n) :
    ans = sys.stdin.readline().split()
    
    if ans[0] == "2" :
        if len(stack) > 0 :
            print(stack.pop())
        elif len(stack) == 0 :
            print(-1)
    elif ans[0] == "3" :
        print(len(stack))
    elif ans[0] == "4" :
        if len(stack) == 0 :
            print(1)
        else :
            print(0)
    elif ans[0] == "5" :
        if len(stack) > 0 :
            print(stack[-1])
        else :
            print(-1)
    elif ans[0] == "1" :
        stack.append(ans[1])

        
