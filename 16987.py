import sys
input = sys.stdin.readline

n = int(input())
egg = [list(map(int, input(). split())) for _ in range(n)]
ans = 0

# 계란의 인덱스, 깨진 계란의 개수를 매개변수로 하는 백트래킹 DFS
def DFS(eggnum, broken) :
    global ans

    if ans >= broken + (n-eggnum)*2 :   # 만약 남은 계란들을 서로 부딪혀서 서로가 같이 깨지는(최대로 깨져도) 수를 다 더해도,
        return                          # 현재 정답에 갱신되었는 값보다 작으면 굳이 해당 탐색은 진행할 필요가 없다

    if eggnum == n :    # 모든 계란에 대해서 서로 부딪힐 수 있는 하나의 경우의 수를 다 세었을 때
        ans = max(ans, broken)   # 정답 갱신
        return
    
    if egg[eggnum][0] <= 0 :    # 지금 손에 든 계란이 이미 깨진 계란이면 다음 계란으로 넘어가자
        DFS(eggnum+1, broken)
    else :            # 현재 손에 들고있는 계란이 안깨진 계란이라면
        flag = False    #  현재 계란과 다른 계란들을 한번이라도 부딪혔는지를 표지
        for i in range(n) :   # 상대 계란들에 대해 탐색
            if eggnum == i or egg[i][0] <= 0 :   # 자기자신을 부딪힐 수 없고, 상대 계란이 이미 깨져있으면 부딪히지 않는다
                continue

            flag = True    # 한번이라도 부딪혔으면 플래그 값을 참으로 표지
            egg[eggnum][0] -= egg[i][1]
            egg[i][0] -= egg[eggnum][1] 
            DFS(eggnum+1, broken + int(egg[eggnum][0]<=0) + int(egg[i][0] <= 0))   # 깨졌으면 해당 불연산의 값이 1일것이고 아니면 0일 것이다
            egg[eggnum][0] += egg[i][1]    # 백트래킹을 위해 방금 부딪힌 과정을 원상복구
            egg[i][0] += egg[eggnum][1] 
        
        if not flag :    # 중간에 다 깨졌어도 마지막 계란까지 탐색
            DFS(eggnum+1, broken)


DFS(0, 0)
print(ans)