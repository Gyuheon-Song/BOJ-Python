import sys
input = sys.stdin.readline
array = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
word, b = map(str, input(). split())
word = word[::-1]
result = 0

for i, n in enumerate(word) :
    result += array.index(n) * (int(b)**i)

print(result)
    



