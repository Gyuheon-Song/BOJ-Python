n = int(input())
setword = set()

for i in range(n) :
    setword.add(input())

lst = list(setword)
lst.sort(key = lambda x : (len(x), x))

for item in lst :
    print(item)