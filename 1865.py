import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc) :
    n, m, w = map(int, input(). split())   
    edge = []      # 간선리스트
    time = [sys.maxsize] * (n+1)     # 걸리는 시간 리스트
    for _ in range(m) :       #  도로의 정보를 간선리스트에 넣자(양방향)
        s, e, t = map(int, input(). split())   
        edge.append((s, e, t))
        edge.append((e, s, t))
    for _ in range(w) :       #  웜홀의 정보를 가넌리스트에 넣자(단방향)
        s, e, t = map(int, input(). split())
        edge.append((s, e, -t))  # 웜홀은 시간이 거꾸로 가므로 음수부호 붙여서

    time[1] = 0     

    for i in range(n-1) :      # n-1번 탐색을 하면 최단시간이 무조건 구해진다
        for s, e, t in edge :
            if time[e] > time[s] + t :
                time[e] = time[s] + t     # 최단시간을 업데이트
    
    timetravel = False    # n-1번 했을 경우 최악의 상황에서도 최단거리가 구해진다
                          # 여기까지는 시간여행은 발생하지 않았다는 변수초기화

    for s, e, t in edge :      # 한번더 업데이트 발생시 
        if time[e] > time[s] + t :
            timetravel = True    # 시간여행은 발생한 것이라 할 수 있다
            break

    if not timetravel :
        print("NO")
    else :
        print("YES")