n = int(input())
timelst = []
for i in range(n) :
    start, end = map(int, input(). split())
    timelst.append([start, end])

def solution(timelst) :
    timelst = sorted(timelst, key = lambda x:(x[1], x[0]))
    cnt = 0
    endtime = 0

    for time in timelst :
        if time[0] >= endtime :
            cnt += 1
            endtime = time[1]
    
    return cnt

print(solution(timelst))

