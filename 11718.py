word_li = []

while True:
    try :
        word = input()
        word_li.append(word)
        if not word :
            break
    except EOFError :
        break

for item in word_li :
    print(item)