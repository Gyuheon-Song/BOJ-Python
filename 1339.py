import sys
input = sys.stdin.readline
n = int(input())
lst = [0]*26    # 알파벳 별 차지하는 차지하는 각 단어의 자리의 10의 승수의 합(AAB-> A : 110 B : 1)
word = []       

for _ in range(n) :
    word.append(input().strip())   # 단어들 입력받기

for i in range(n) :
    for j in range(len(word[i])) :
        # 각 알파벳의 아스키 코드-65의 인덱스에 해당 알파벳이 의미하는 10의자리값을 입력
        lst[ord(word[i][j])-65] += 10**(len(word[i])-j-1)

lst.sort(reverse = True)   # 내림차순 정렬
ans = 0

#차지하는 자릿수의 합이 가장 큰 알파벳부터 9부터 0까지 각각 곱해준다
for k in range(10) :
    ans += k*lst[9-k]

print(ans)
