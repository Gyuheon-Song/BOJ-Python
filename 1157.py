word = input().upper()
unique_alphabet = list(set(word))
word_count = []

for i in unique_alphabet :
    word_count.append(word.count(i))

if word_count.count(max(word_count)) > 1 :
    print("?")
else :
    max_index = word_count.index(max(word_count))
    print(unique_alphabet[max_index])





