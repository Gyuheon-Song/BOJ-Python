import math
stat = list(map(int, input(). split()))
visited = [False]*8
cnt = 0

def Solve(lst) :    # 양 옆의 두 스텟끼리만 이루는 직각삼각형의 넓이보다 양 옆의 스택 각각과 사이의 스텟이 이루는
                    # 두 직각삼각형의 넓이의 합이 큰 경우 볼록하다
    global cnt, stat
    if len(lst) == 8 :
        flag = True
        for i in range(8) :
            if i == 7 :
                if lst[0]*lst[i]/math.sqrt(2) + lst[i-1]*lst[i]/math.sqrt(2) > lst[0]*lst[i-1] :
                    continue
                else :
                    flag = False
                    break
            else :
                if lst[i-1]*lst[i]/math.sqrt(2) + lst[i+1]*lst[i]/math.sqrt(2) > lst[i-1]*lst[i+1]:
                    continue
                else :
                    flag = False
                    break
        if flag :
            cnt += 1
        return 
    for i in range(8) :
        if not visited[i] :
            lst.append(stat[i])
            visited[i] = True
            Solve(lst)     # 순열 생성 => 총 8!개
            lst.pop()
            visited[i] = False

d = []
Solve(d)
print(cnt)