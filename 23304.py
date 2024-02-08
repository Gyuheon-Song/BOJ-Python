s = input()

def AKRK(string) :
    if len(string) == 1 :
        return True
    elif string == string[::-1] and string[:len(string)//2] == string[len(string)//2-1::-1] :
        return AKRK(string[:len(string)//2])
    else :
        return False

if AKRK(s) :
    print("AKARAKA")
else :
    print("IPSELENTI")

