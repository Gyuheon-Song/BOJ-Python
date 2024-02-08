
length = list(map(int, input(). split()))

if max(length) >= sum(length) - max(length) :
    print(2*(sum(length)-max(length))-1)

elif max(length) < sum(length) - max(length):
    print(sum(length))

