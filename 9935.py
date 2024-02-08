import sys
word = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()
k = len(bomb)
Q = []

for char in word :
    Q.append(char)
    if char == Q[-1] and "".join(Q[-k:]) == bomb :
        del Q[-k:]
            
    
print("".join(Q)) if Q else print("FRULA")   