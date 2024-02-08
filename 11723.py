import sys
S = set()
n = int(input())
for _ in range(n) :
    com = sys.stdin.readline().strip(). split(" ")
    if com[0] == "add" :
        S.add(int(com[1]))
    elif com[0] == "remove" :
        S.discard(int(com[1]))
    elif com[0] == "empty" :
        S.clear()
    elif com[0] == "toggle" :
        if int(com[1]) in S :
            S.remove(int(com[1]))
        else :
            S.add(int(com[1]))
    elif com[0] == "check" :
        if int(com[1]) in S :
            print(1)
        else :
            print(0)
    elif com[0] == "all" :
        S = set([i for i in range(1, 21)])
    
