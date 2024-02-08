n = int(input())
lst = set()
cnt = 0
for _ in range(n) :
    chat = input()

    if chat == "ENTER" :
        cnt += len(lst)
        lst = set()
        continue
    else :
        lst.add(chat)

cnt += len(lst)

print(cnt)