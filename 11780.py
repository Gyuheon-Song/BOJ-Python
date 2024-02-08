import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
adjmtrx = [[sys.maxsize] * (n+1) for _ in range(n+1)]   # 최단비용 인접행렬
prev = [[0]*(n+1) for _ in range(n+1)]           # 비로 직전 도시를 저장할 인접행렬
route = []  # 추후 각 경로별 이전경로들을 출력할 경로변수 미리 선언

for _ in range(m) :
    a, b, c = map(int, input(). split())
    if adjmtrx[a][b] > c :              #  비용이 작은 간선의 비용을 저장하고
        adjmtrx[a][b] = c
        prev[a][b] = a                  # 최소비용 간선의 출발도시가 곧 직전도시이므로 이를 직전도시 저장리스트에 저장한다
    
# 플로이드 워셜 알고리즘
for k in range(1, n+1) :
    for i in range(1, n+1) :
        for j in range(1, n+1) :
            # 출발지와 도착지가 같지 않으며 기존 출발도착 경로보다 다른 경유지를 경유하여 도착지로 가는 경우가 비용이 적을때
            if i != j and adjmtrx[i][j] > adjmtrx[i][k] + adjmtrx[k][j] :
                # 경유하는 경로를 기존경로에 최신화
                adjmtrx[i][j] = adjmtrx[i][k] + adjmtrx[k][j]
                # 그리고 그 경로의 직전도시는 경유지가 되므로 해당경로의 직전도시에 경유지 출발하여 도착지까지 가는 경로의 직전도시를 최신화
                prev[i][j] = prev[k][j]
            
for i in range(1, n+1) :
    for j in range(1, n+1) :
        if adjmtrx[i][j] == sys.maxsize : # 경로가 없는 경우 0
            adjmtrx[i][j] = 0
        print(adjmtrx[i][j], end = " ")
    print("")

for i in range(1, n+1) :
    for j in range(1, n+1) :
        if adjmtrx[i][j] == 0 :  # 경로가 없는 경우 0출력
            print(0)
        else :
            route = [j]     # 도착지가 올라가있는 경로리스트 초기화선언 
            temp = j        # 거꾸로 역행하여 탐색을 실시하기 위한 변수선언과 도착지부터 시작할 것
            while temp != i :     # 출발지까지 도달할때까지 역으로 탐색을 하자
                route.append(prev[i][temp])    # 역행경로에 출발지부터 도착지까지 경로에서의 직전도시를 저장한다
                temp = prev[i][temp]           # 출발지부터 방금 저장한 직전도시까지의 경로에서의 직전도시를 저장한다
            print(len(route), *route[::-1])    # 위의 역추적과정을 해당 경로리스트를 뒤집어 출력한다

    
