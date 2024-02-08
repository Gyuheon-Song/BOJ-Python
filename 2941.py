word = input()
croatian = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word_count_cr = 0


for i in croatian :
    
    if i in word :
        word_count_cr += word.count(i)
        
word_count_al = len(word) - 2*word_count_cr 

print(word_count_cr + word_count_al)
    
