import sys
input = sys.stdin.readline

n, k = map(int, input(). split())
knapsack = [[0 for _ in range(n+1)] for _ in range(k+1)]
subject = [[0, 0]]

for _ in range(k) :
    subject.append(list(map(int, input(). split())))

for i in range(1, k+1) :
    for j in range(1, n+1) :
        value = subject[i][0]
        time = subject[i][1]
        if j >= time :
            knapsack[i][j] = max(value + knapsack[i-1][j-time], knapsack[i-1][j])
        else :
            knapsack[i][j] = knapsack[i-1][j]

print(knapsack[k][n]) 
