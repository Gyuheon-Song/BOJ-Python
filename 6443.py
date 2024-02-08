import sys
input = sys.stdin.readline

def DFS(n, cnt) :
    if n == l :
        print(*ans, sep = "")
        return
    
    for i in word :
        if cnt[ord(i)-97] == 0 :
            continue
        ans.append(i)
        cnt[ord(i)-97] -= 1
        DFS(n+1, cnt)
        ans.pop()
        cnt[ord(i)-97] += 1
    return


t = int(input())

for _ in range(t) :
    word = input().strip()
    l = len(word)
    ans = []
    cnt = [0]*26
    for alph in word :
        cnt[ord(alph)-97] += 1
    word = set(word)
    word = list(sorted(word))
    DFS(0, cnt)

