word = input()
lst = []
for i in range(len(word)) :
    for j in range(i+1, len(word)+1) :
        lst.append(word[i:j])

print(len(set(lst)))