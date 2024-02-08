word_array = [["*" for j in range(15)] for i in range(5)]

for i in range(5) :
    word_list = input()

    for index, word in enumerate(word_list) :        
        word_array[i][index] = word

for j in range(15) :
    for i in range(5) :
        if word_array[i][j] == "*" :
            continue
        print(word_array[i][j], end = "")


