import sys
from collections import deque
input = sys.stdin.readline

alphdict = {}   # 알파벳 순서대로 1부터 26까지의 수를 지정
for letter in range(65, 91) :
    alphdict[chr(letter)] = letter-64

adjlst =[[] for _ in range(27)]   # 인접리스트
time = [0] * (27)    # 각 작업에 걸리는 시간 저장
indegree = ["INF"] * (27)   # 진입차수 초기화선언
dp = [0] * (27)   # 해당 인덱스를 밸류로 가지는 알파벳의 작업까지 끝내는데 걸리는 총 시간

while True :  # 입력이 없을때까지 반복
    lst = list(map(str, input(). split()))  # 입력을 리스트로 받기
    if lst :  
        if len(lst) == 2 :   # 선행되어야 하는 작업은 입력에 없어 입력의 매핑결과의 길이가 2라면
            time[alphdict[lst[0]]] = int(lst[1])   # 입력의 첫 요소인 알파벳의, 숫자로 환산한 값을 시간리스트의 인덱스로 하여 해당 작업의 단독 소요시간인 입력의 두번째 요소를 int형으로 변환하여 저장
            indegree[alphdict[lst[0]]] = 0   # 선행작업이 없는 입력이었으므로 진입차수를 숫자 0으로 바꾸어준다
        else :   # 선행되어야 하는 작업까지 입력되었다면 입력의 매핑결과의 길이는 3
            time[alphdict[lst[0]]] = int(lst[1])   # 해당 작업의 단독 소요시간 저장
            k = len(lst[2])  # 선행되어야 하는 작업들의 개수만큼 반복할것
            for i in range(k) :
                adjlst[alphdict[lst[2][i]]].append(alphdict[lst[0]])   # 선행작업과 나중작업을 잇는 엣지를 인접리스트에 저장
                if indegree[alphdict[lst[0]]] == "INF" :   # 진입차수 초기상태 그대로면
                    indegree[alphdict[lst[0]]] = 1  # 방금 선행작업이 있다고 했으므로 진입차수를 1로 바꾸어준다
                else :  # 친입차수가 초기 상태가 아닌 다른 숫자라면
                    indegree[alphdict[lst[0]]] += 1  # 진입차수를 하나 더 늘려준다
    else :  # 입력이 없으면 중단
        break

def Topo_sort() :   # 위상정렬 알고리즘
    q = deque()

    for i in range(1, 27) :   
        if indegree[i] == 0 :   # 전체 진입차수리스트 탐색하여 진입차수가 숫자 0인 작업만 큐에 넣는다
            q.append(i)
            dp[i] = time[i]    # 총 소요시간 리스트에 해당 작업의 단독소요시간 저장
    
    while q :
        now = q.popleft()
        for next in adjlst[now] :
            indegree[next] -= 1
            dp[next] = max(dp[next], dp[now] + time[next])   # 더 긴 소요시간 저장(그보다 짧은 시간이 소요되는 건물들은 병행건설이 가능하므로)
            if indegree[next] == 0 :  # 진입차수가 0이되면 해당 작업을 큐에 넣어준다
                q.append(next)

Topo_sort()

print(max(dp))   # 작업별 총 소요시간리스트에서 가장 오래 걸리는 시간을 출력
        

    


        
