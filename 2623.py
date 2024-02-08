import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input(). split())
adjlst = [[] for _ in range(n+1)]  
indegree = [0]*(n+1)   # 가수번호별 진입차수리스트
singer = []   # 노래부를 순서를 저장할 리스트

def topo_sort(n) :   # 위상정렬 알고리즘
    q = deque()

    for i in range(1, n+1) :  
        if indegree[i] == 0 :   # 진입차수가 0인 가수들을 큐에 먼저 집어넣는다
            q.append(i)
    
    while q :   # 큐에 노래부를 가수들이 있을때
        sing = q.popleft()   
        singer.append(sing)   # 해당 가수를 리스트에 넣고
        for next in adjlst[sing] :   # 다음 가수들의 진입차수를 1씩 감소
            indegree[next] -= 1
            if indegree[next] == 0 :   # 다음 가수들 중에 진입차수가 0인 가수가 있으면 큐에 집어넣는다
                q.append(next)


for _ in range(m) :   # PD별 가수순서를 입력받는다
    seq = list(map(int, input(). split()))
    for i in range(1, seq[0]) :
        for j in range(i+1, seq[0]+1) :
            adjlst[seq[i]].append(seq[j])
            indegree[seq[j]] += 1

topo_sort(n)  # 위상정렬

if len(singer) == n :   # 위상정렬을 진행한 후 가수의 목록이 총 가수의 수와 일치하면 정렬성공
    for i in singer :
        print(i)
else :   # 그렇지 않다면 정렬에 실패한 것이므로 0 출력
    print(0)
