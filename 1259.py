while True :
    lst = list(input())

    if lst == ["0"] :
        break        
    elif lst == lst[::-1] :
        print("yes")
    else :
        print("no")