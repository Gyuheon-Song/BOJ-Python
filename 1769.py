import sys
input = sys.stdin.readline

number = input().strip()
cnt = 0
k = int(number)

while len(number) >= 2 :
    k = 0
    for i in range(len(number)) :
        k += int(number[i])
    number = []
    cnt += 1
    for digit in str(k) :
        number.append(digit)

print(cnt)
print("YES") if k % 3 == 0 else print("NO")
