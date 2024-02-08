import sys
input = sys.stdin.readline

n = int(input())
adjmtrx = [[sys.maxsize] * (n+1) for _ in range(n+1)]   # 인접행렬 최댓값으로 초기화
candidate = [[] for _ in range(n+1)]      # 후보자를 저장할 리스트 초기화


while True :
    a, b = map(int, input(). split())    # 친구관계를 양방향 간선, 가중치 1로 설정
    adjmtrx[a][b] = 1
    adjmtrx[b][a] = 1
    if a == -1 and b == -1 :     # -1 -1 을 입력받았을 시 입력사이클 중단
        break

# 플로이드 워셜 알고리즘 실행
for k in range(1, n+1) :
    for i in range(1, n+1) :
        for j in range(1, n+1) :
            adjmtrx[i][j] = min(adjmtrx[i][j], adjmtrx[i][k]+adjmtrx[k][j])

# 본인 스스로 친구관계일 수 없으므로 0으로 설정
for i in range(1, n+1) :     
    adjmtrx[i][i] = 0

# 점수가 낮아야 회장후보이므로 회원들 중의 최소점수를 저장할 변수를 최대회원수인 50으로 초기화
min_score = 50

# 최소점수를 가진 회원을 찾기 위해 회원들에 대해 탐색을 실행한다
for i in range(1, n+1) :
    score = 0   # i회원의 초기 점수는 0으로 설정
    for j in range(1, n+1) :
        score = max(score, adjmtrx[i][j])  # 가장 먼 친구점수가 그 회원의 점수이므로 max비교를 통해 점수를 산정
    candidate[score].append(i)    # 후보자 리스트에서 회원점수를 인덱스로 하는 공간에 회원의 번호를 저장
    min_score = min(min_score, score)   # 기존에 찾아놓았던 최소점수보다 현재 후보의 점수가 더 낮으면 현재 회원의 점수 저장

# 회원들 중 후보자들은 점수가 가장 낮을 것이므로 최소점수 출력
# 후보자 리스트에 본인의 점수가 인덱스인 공간에 회원번호가 올라가 있으므로
# 최소점수를 인덱스로 하는 공간의 길이가 해당 최소점수의 회원 수
# 최소점수를 가진 회원(회장후보자)의 리스트를 후보자리스트에서 인덱싱하여 출력
print(min_score, len(candidate[min_score]))
print(*candidate[min_score])

