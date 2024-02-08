def DSF(a) :
    if a == 1 :
        return "-"
    else :
        left = DSF(a//3)
        mid = " "*(a//3)
        right = DSF(a//3)
        return left + mid + right



while True :
    try :
        n = int(input())
        ans = DSF(3**n)
        print(ans)

    except :
        break






