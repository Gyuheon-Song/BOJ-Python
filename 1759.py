l, c = map(int, input(). split())

letter = sorted(list(map(str, input(). split())))
ans = []
vowel_ascii = [0]*128  # 모음을 판별하기 위한 리스트(모음=1, 자음=0)
for ch in "aeiou" :
    vowel_ascii[ord(ch)] = 1

# 입력받은 레터리스트의 인덱스, 모음의 개수, 조합문자열을 매개변수로 한다
def DFS(index, cnt, tmp) :

    if index == c :    # c개의 문자에 대해서 각각의 포함여부를 다 정했을 시
        # 만약 현재 조합한 문자열의 길이가 l과 같고, 자음의 개수가 2개 이상이며 모음의 개수가 1개 이상일 때 비밀번호로 사용가능
        if len(tmp) == l and cnt >= 1 and l-cnt >= 2 :
            ans.append(tmp)
        return 
    
    DFS(index+1, cnt+vowel_ascii[ord(letter[index])], tmp+letter[index])     # 포함하는경우 -> 모음이 포함되었을 경우 판별리스트 모음에는 1이 저장되어있으므로 카운트에 더한다
    DFS(index+1, cnt, tmp)      # 포함하지 않는 경우


DFS(0, 0, "")

for pw in ans :
    print(pw)
