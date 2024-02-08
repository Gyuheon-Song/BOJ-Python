import sys
import heapq

input = sys.stdin.readline
schedule = [0]*(1001)    # 실제로 풀 과제를 저장(인덱스가 과제를 하는 날)
hw = []     # 과제를 입력받을 리스트
ans = 0

n = int(input())

for _ in range(n) :
    tmp = list(map(int, input(). rstrip(). split()))
    hw.append(tmp)

hw.sort(key = lambda x : -x[1])    # 과제를 점수가 높은것부터 내림차순 정렬

for i in range(n) :
    [due, score] = hw[i]    # 과제들을 언패킹
    if schedule[due] == 0 :      # 기한에 가장 가까운 날에 해당 과제를 할것이므로
        # 만약 해당 날짜에 해야하는 과제가 아직 없다면 그 날짜가 기한인 과제를 한다
        schedule[due] = score
    else :
        due -= 1  # 최대한 기한에 가깝게 하기 위해 날짜를 하루씩 당겨가며 과제를 할 수 있는 날이 있는지 탐색
        while due > 0 :    # 첫째날까지 탐색해본다
            if score > schedule[due] :    # 어떠한 날에 하는 과제보다 더 높은 점수의 과제를 그 날짜에 하도록 갈아넣는다
                schedule[due] = score
                break
            else :    # 이미 더 높은 점수의 과제를 어떤 날에 해야하면 하루씩 더 당겨서 빈 날짜가 있는지 찾아본다
                due -= 1

print(sum(schedule))

