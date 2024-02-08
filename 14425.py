import sys
input = sys.stdin.readline
std_lst = []
chk_lst = []
cnt = 0
n, m = map(int, input(). split())

for i in range(n) :
    std_lst.append(input())
for j in range(m) :
    chk_lst.append(input())
for word in chk_lst :
    if word in std_lst :
        cnt += 1
print(cnt)
