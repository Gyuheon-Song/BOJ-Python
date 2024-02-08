import sys
import heapq

input = sys.stdin.readline

# 연강 가능 강의들을 연결해간다
n = int(input())   # 수업의 개수
hq = []    # 연강의 마지막 강의의 종료시간을 저장할 최소힙
time = []   # 강의의 시간정보 저장 리스트

for _ in range(n) :   
    s, t = map(int, input(). split())
    time.append([s, t])    # 강의시간정보 저장

time.sort(key = lambda x: (x[0], x[1]))    # 강의들을 강의시작시간이 빠른 것부터 정렬, 같을 경우 종료시간이 빠른 순
heapq.heappush(hq, time[0][1])  # 종료시간만을 저장할 힙에 첫 강의를 일단 넣는다

for i in range(1, n) :   # 두번째 강의들부터
    if time[i][0] < hq[0] :   # 만약 강의의 시작시간이 최소힙의 첫 원소(가장 빠른 종료시간) 보다 작으면 연강불가하므로
        heapq.heappush(hq, time[i][1])   # 추가강의실이 필요하므로 종료시간을 최소힙에 추가해준다
    else :   # 강의의 시작시간이 현재 강의실들 중 가장 빠른 종료시간의 강의실 이후 시간대라면 그 강의실에서 연강가능하므로
        heapq.heappop(hq)   # 모든 강의실 중 가장 빠른 강의시간을 삭제하고
        heapq.heappush(hq, time[i][1])   # 방금 연강으로 인한 종료시간으로 변경시키기 위해 다시 최소힙에 추가해준다

print(len(hq))   # 최소힙에 있는 종료시간들 각각이 사용한 강의실들별 종료시간이므로
 # 최소힙의 길이가 곧 필요한 강의실의 갯수



