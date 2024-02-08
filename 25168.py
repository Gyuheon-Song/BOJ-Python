import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input(). split())
indegree = [0]*(n+1)    # 진입차수 리스트
adjlst = [[] for _ in range(n+1)]   # 백신간 접종순서를 저장하는 인접리스트
vaccineDay = [0]*(n+1)   # 인덱스 번호의 백신을 몇일에 접종했는지를 저장하는 리스트


for _ in range(m) :   # 접종순서정보를 저장하며
    s, e, w = map(int, input(). split())
    adjlst[s].append((e, w))
    indegree[e] += 1   # 진입차수를 1씩 증가

def Topo_Sort() :   # 위상정렬

    Q = deque()   # 덱       

    for i in range(1, n+1) :
        if indegree[i] == 0 :    # 진입차수가 0인 백신들은 첫째날에 같이 접종가능
            vaccineDay[i] = 1    # 1일차 접종 표지
            Q.append(i)          # 덱에 진입차수 0인 백신들을 넣어준다

    while Q :  

        now = Q.popleft()    # 덱에서 진입차수가 0인 백신들을 꺼내온다

        for next, wait in adjlst[now] :   # n차로 맞아야 하는 백신과 대기기간
            if wait >= 7 :   # 만약 대기기간이 7일 이상인 경우
                # 7일 후에 재접종 후 다음백신을 바로 다음날 접종한다
                if vaccineDay[next] < (vaccineDay[now] + wait + 1) :
                    vaccineDay[next] = vaccineDay[now] + wait + 1
                    indegree[next] -= 1

            else :   # 대기기간이 7일보다 작을 경우
                # 대기기간만 정확히 기다린 후 접종한다
                if vaccineDay[next] < (vaccineDay[now] + wait) :
                    vaccineDay[next] = vaccineDay[now] + wait
                    indegree[next] -= 1

            if indegree[next] == 0 :   # 진입차수가 0이 된 백신은 덱에 넣어준다
                Q.append(next)

Topo_Sort()  

print(max(vaccineDay))   # 백신의 접종일 중 최대값
