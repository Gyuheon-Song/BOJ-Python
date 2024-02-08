a = int(input())
b = str(input())
digits = []

for char in b : 
    digit = int(char)
    digits.append(digit)

digit_num = len(digits)

for i in range(1,len(digits)+1) : 
    print(a*digits[-i])

print(a*int(b))


