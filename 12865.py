import sys
input = sys.stdin.readline

n, k = map(int, input(). split())
# 가방의 개수(행)와 제한무게(열)를 배열로 구현
knapsack = [[0 for _ in range(k+1)] for _ in range(n+1)] 
# 0행 0열 생성
smth = [[0, 0]]
 #물건을 물건배열에 append
for _ in range(n) :
    smth.append(list(map(int, input(). split())))

# knapsack algorithm
# knapsack arr를 돌며 조건훑기 
for i in range(1, n+1) :
    for j in range(1, k+1) :
# 물건들에 대해 가방무게와 가치를 변수에 배정
        weight = smth[i][0]
        value = smth[i][1]
# 제한무게보다 가방의 무게가 작거나 같을 때 물건을 넣어야 하므로
# 해당 가방에는 현재물건과, 현재물건을 뺏을 때 남은 여유무게에 들어갈 수 있는 물건의 가치와  ///  
# 다른 물건들로 채웠을때의 가치 중 더 큰 가치를 골라야 한다        
        if j >= weight :
            knapsack[i][j] = max(value + knapsack[i-1][j-weight], knapsack[i-1][j])
# 제한무게보다 가방무게가 클 때는 다른 물건들로 채웠을 때의 가치인 바로 위 칸의 값을 가져온다
        else :
            knapsack[i][j] = knapsack[i-1][j]

print(knapsack[n][k])

