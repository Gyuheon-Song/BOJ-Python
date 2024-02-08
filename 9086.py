n = int(input())
word_li = []

for i in range(n) :
    word = str(input()) 
    word_li.append(word[0]+word[-1]) 

for j in range(n) :
    print(word_li[j])


