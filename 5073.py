
while True :
    a, b, c = map(int, input(). split())
    triangle = [a, b, c]
    max_length = max(triangle)

    if [a, b, c] == [0, 0, 0] :
        break

    if max(triangle) >= sum(triangle) - max(triangle) :
        print("Invalid")
    else :
        if len(set(triangle)) == 3 :
            print("Scalene")
        elif len(set(triangle)) == 2 :
            print("Isosceles")      
        elif len(set(triangle)) == 1 :
            print("Equilateral")
   
    
    

    