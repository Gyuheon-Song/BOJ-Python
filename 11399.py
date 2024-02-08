n = int(input())
timelst = list(map(int, input(). split()))

def solution(time, n) :
    timelst.sort()
    time = 0
    for i in range(1, n+1) :
        time += timelst[i-1]*(n+1-i)
    return time

print(solution(timelst, n))