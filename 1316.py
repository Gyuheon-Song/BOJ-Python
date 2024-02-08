n = int(input())
#입력받은 단어의 총 개수에서 차감하자
cnt = n

for i in range(n):
    word = input()
    # 연속해서 같은 문자가 나올때는 그룹단어이다, 그대로 진행
    for j in range(len(word)-1) :
        if word[j] == word[j+1] :
            pass
        # 연속해서 같은 문자가 오지 않지만 다른 문자 건너 같은 문자가 있을때 그룹단어 아니다
        elif word[j] in word[j+2:] :
            cnt -= 1
            break
print(cnt)

            
        


