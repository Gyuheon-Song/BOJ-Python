
score = []

for i in range(0,5) : 
    score.append(int(input()))
    if score[i] < 40 :
        score[i] = 40

average = sum(score)/len(score)
print(int(average))

