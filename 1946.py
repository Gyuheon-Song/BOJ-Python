import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t) :
    n = int(input())
    lst = []
    cnt = 1
    for _ in range(n) :
        lst.append(list(map(int, input().strip(). split())))
    lst.sort()
    cur_lowest_Rank = lst[0][1]
    for i in range(1, n) :
        if cur_lowest_Rank > lst[i][1] :
            cnt += 1
            cur_lowest_Rank = lst[i][1]
        else :
            cur_lowest_Rank = min(cur_lowest_Rank, lst[i][1])
    print(cnt)