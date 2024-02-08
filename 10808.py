s = list(input())

lst = [0]*26

for i in s :
    lst[ord(i)-97] += 1

print(*lst)

