import string
alphabet = list(string.ascii_lowercase)
dic = {letter : index+1 for index, letter in enumerate(alphabet)}
r = 31
m = 1234567891
n = int(input())
lst = list(input())
k = len(lst)
sum = 0
for i in range(k) :
    sum += dic[lst[i]] * (r**i)

print(sum % m)