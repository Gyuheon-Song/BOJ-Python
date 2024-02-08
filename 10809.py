word = input()
alphabet = []

for i in range(97, 123) :
    if chr(i) in word :
        alphabet.append(word.index(chr(i)))
    else :
        alphabet.append(-1)
print(*alphabet)
